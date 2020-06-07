#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Mirar:
 https://github.com/buriy/python-readability
 https://github.com/timbertson/python-readability/blob/master/readability/readability.py
 
 https://github.com/MHordecki/readability-redux/blob/master/readability/readability.js
"""

import re
import urllib
import chardet

from bs4 import BeautifulSoup
from gremlims import cp1252

from config import settings
from core.cache.file_storage_factory import FileStorageFactory
from core.seo.containers.seo_document import DataDocument
from bs4.element import NavigableString
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from urlparse import urlparse
from core.data_mining.web_pages.scrapers.readability import Readability
from core.concurrence.request_factory import RequestFactory

try:
    import magic
except:
    magic = None # Windows

from utils.logger import LoggerFactory
app_download_logger = LoggerFactory.getInstance('downloader')


class DownloadException(Exception):
    def __str__(self):
        return 'Download url error'

class UserAgent(object):
    chrome = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    firefox = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    safari = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    seologies = 'Seologies/0.1 Bot'
    old = 'Mozilla/11.0'


DEFAULT_SCAPING_FILTER = Readability
class Scraper(object):
    
    CACHE_PATH = u'/dataDocument'
    
    def __init__(self, url, 
                       userAgent=UserAgent.seologies, 
                       sameOrigin=False, 
                       debug=False,
                       scrapingFilterClass=DEFAULT_SCAPING_FILTER,
                       useProxy=False):
        self.url = url
        self.redirectedUrl = None
        self.userAgent = userAgent
        self.DEBUG = debug
        self.rawHtml = None
        self.sameOrigin = sameOrigin
        self.scrapingFilterClass = scrapingFilterClass
        self.useProxy = useProxy
    
    def getDataDocument(self):
        fileCache = FileStorageFactory.getFileStorage(Scraper.CACHE_PATH)
        dataDocument = fileCache.get(self.url)
        if dataDocument and settings.SCRAPER_RELOAD_CONTENT:
            self.rawHtml = dataDocument.rawHtml
            dataDocument = self._getDataDocument()
            fileCache.set(self.url, dataDocument)
        if not dataDocument or not settings.CACHE:
            dataDocument = self._getDataDocument()
            fileCache.set(self.url, dataDocument)
        return dataDocument
    
    def _getDataDocument(self):
        if not self.rawHtml:
            self.download()
        
        dataDocument = DataDocument()   
        
        dataDocument.rawHtml = self.rawHtml
        
        dataDocument.uri = urlparse(self.url).path
        
        try:
            dataDocument.uri = urllib.unquote(dataDocument.uri)
        except:
            pass
        
        # get last uri part
        dataDocument.uri = dataDocument.uri.rstrip('/') # remove last slash
        dataDocument.uri = dataDocument.uri.rsplit('/', 1)[-1]
        
        dataDocument.uri = dataDocument.uri.replace('+', ' ')
        dataDocument.uri = dataDocument.uri.replace('-', ' ')
        dataDocument.uri = dataDocument.uri.replace('.', ' ')
        dataDocument.uri = dataDocument.uri.replace('/', ' ')
        dataDocument.uri = dataDocument.uri.replace('_', ' ')
        dataDocument.uri = u'%s' % dataDocument.uri.replace('htm', '')
        
        soup = BeautifulSoup(self.rawHtml, 'lxml')
        
        title = soup.head.title if soup.head else None
        titleText = title.get_text(separator=u' ', strip=True, types=[NavigableString]).strip().lower() if title else ''
        dataDocument.title = titleText
        
        #title = soup.head.title if soup.head else None
        #titleText = title.get_text(separator=u' ', strip=True, types=[NavigableString]).strip().lower().replace(u'-', u' ') if title else ''
        
        meta = soup.head.find(attrs={"name":"description"}) if soup.head else None
        dataDocument.meta = u'%s' % meta.attrs['content'].strip().lower() if meta and 'content' in meta.attrs else ''
        
        keywords = soup.head.find(attrs={"name":"keywords"}) if soup.head else None
        dataDocument.keywords = u'%s' % keywords.attrs['content'].strip().lower() if keywords and 'content' in keywords.attrs else ''

        dataDocument.h1 = [h1.get_text(separator=u' ', strip=True, types=[NavigableString]).strip().lower().replace(u'-', u' ') for h1 in soup.find_all('h1')]
        dataDocument.h2 = [h2.get_text(separator=u' ', strip=True, types=[NavigableString]).strip().lower().replace(u'-', u' ') for h2 in soup.find_all('h2')]
        dataDocument.strong = [strong.get_text(separator=u' ', strip=True, types=[NavigableString]).strip().lower().replace(u'-', u' ') for strong in soup.find_all(['strong', 'b'])]
        dataDocument.alt = [u'%s' % image.get('alt').strip().lower().replace(u'-', u' ') for image in soup.find_all('img')  if image.get('alt')]
        
        #facebook = soup.head.find(property='og:description') if soup.head else None
        #facebookText = facebook.attrs['content'].strip().lower().replace(u'-', u' ') if facebook and 'content' in facebook.attrs else ''
        
        try:
            bodyText, soup = self.scrapingFilterClass().getFilteredText(self.rawHtml)
            bodyText = bodyText.strip() ####.lower()
            dataDocument.bodyWords = self._getNumWords(soup.body)
        except Exception, e:
            app_download_logger.error(u'_scrapping %s' % e)
            bodyText = ''
        
        dataDocument.text = bodyText
        
        return dataDocument
    
    def _getNumWords(self, soupTag):
        innerText = soupTag.get_text(separator='', strip=True, types=[NavigableString])
        return len(innerText.split())
    
    def download(self):
        try:
            if self.useProxy:
                pool = RequestFactory.getProxyPool()
            if self.sameOrigin:
                pool = RequestFactory.getSameOriginPool()
            else:
                pool = RequestFactory.getPool()
            
            response = pool.request('GET', self.url, headers={"User-Agent": self.userAgent, "Accept" : "text/html" })
            
            self.redirectedUrl = response.url
            
            print self.url
            print self.redirectedUrl
            
            if response.status_code > 399:
                raise Exception(u"status: %s" % response.status_code)
            
            if 'content-type' in response.headers:
                content_type = response.headers['content-type']
            else:
                content_type = None
            
            if self._checkValidContent(content_type, response.text):
                self.rawHtml = response.text
            else:
                self.rawHtml = ''
                # print '_scraper: Filetype not compatible --> Removed from the app'
                app_download_logger.error('_scraper: Filetype not compatible: %s --> Removed from the app' % self.url)
        except Exception as ex:
            app_download_logger.error(u'_download %s' % ex)
            raise DownloadException
        try:
            self.rawHtml = self.rawHtml.decode('utf8')
        except:
            try:
                self.rawHtml = Encoder.toUTF8(self.rawHtml)
            except:
                pass
        app_download_logger.info(u"Downloaded: %s" % self.url)
        return Encoder.killgremlins(self.rawHtml)
    
    def _checkValidContent(self, content_type, data):
        
        if not magic: return True
        
        mimeType = magic.from_buffer(data, mime=True)
        if 'text' in content_type and ('text' in mimeType or 'octet-stream' in mimeType):
            return True
        if 'application' not in content_type and ('text' in mimeType or 'octet-stream' in mimeType):
            return True
        if not content_type and ('text' in mimeType):
            return True
        
        app_download_logger.info(u'content-type: %s , data-mimetype: %s ' % (content_type, magic.from_buffer(data, mime=True)))
        return False
    
class Encoder(object):        
    
    @staticmethod
    def toUTF8(html, limit=0):
        """
        Use chardet to detect enconding. Slow process and not perfect.
        Limit processed characters limit
        """
        # Detect encoding and convert if necessary
        # encoding = 'UTF-8'
        characters = len(html)
        
        if limit > 0:
            characters = min(characters, limit)
        
        encoding = chardet.detect(html[:characters])['encoding']
        
        if encoding and 'UTF-8' != encoding.upper():  # change encoding
            html = html.decode(encoding, html)  # #.encode('UTF-8')
        else:
            pass
        
        return html
    
    @staticmethod
    def killgremlins(text):
        # map cp1252 gremlins to real unicode characters
        if re.search(u"[\x80-\xff]", text):
            def fixup(m):
                s = m.group(0)
                return cp1252.get(s, s)
            if isinstance(text, type("")):
                # make sure we have a unicode string
                text = unicode(text, "iso-8859-1")
            text = re.sub(u"[\x80-\xff]", fixup, text)
        return text



if __name__ == '__main__':

    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')

    urls = [u'http://www.zooplus.es/shop/tienda_perros/pienso_perros/royal_canin_club_selection/royal_canin_special_club/56533',
            u'http://www.animalclan.com/es/16739-scalibor-65cm-royal-canin-club-adult-special-performance.html',
            
            u'http://www.elmundo.es',
            
            u'http://www.animalclan.com/es/15295-royal-canin-gatos-norweian-forest.html?%20search_query=norw&results=1',
            u'https://3acd-descargar.phpnuke.org/es/c09262/microsoft-office-2010',
            
            u'https://serps.com/library/',
           
            u'http://www.publico.es/sociedad/liberado-madrid-joven-al-padre.html',
            u'http://www.publico.es/',
            u'http://www.elmundo.es/',
            u'http://www.zooplus.es/shop/tienda_perros/pienso_perros/taste_of_the_wild/taste_of_the_wild_adult/409340',
            u'http://www.decathlon.es/zapatillas-de-running-hombre-kalenji-ekiden-one-gris--id_8351755.html',

            u'http://www.luciasecasa.com/',
            u'http://www.luciasecasa.com/boda-de-la-semana/la-boda-la-semana-marta-jaime/',
            
            u'http://www.helicopternewyorkcity.com/',
            #u'http://www.animalclan.com/es/6310-collar-scalibor-oferta.html',            
            ]



    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'

    for url in urls[-1:]:
        print(80*'-')
        print url
        scraper = Scraper(url, scrapingFilterClass=Readability)
        dataDocument = scraper._getDataDocument()
        
        htmlText = u"<html><head><meta charset='UTF-8' /></head><body>"
        htmlText += u'<div><strong><a href="%s">%s' % (url, url) + u'</a></strong></div><hr><br/><br/>'
        
        htmlText += u'<div>' + u"uri:      %s" % dataDocument.uri + u'</div><hr>'
        htmlText += u'<div>' + u"title:    %s" % dataDocument.title + u'</div><hr>'
        htmlText += u'<div>' + u"meta:     %s" % dataDocument.meta + u'</div><hr>'
        htmlText += u'<div>' + u"keywords: %s" % dataDocument.keywords + u'</div><hr>'
        htmlText += u'<div>' + u"h1:       %s" % dataDocument.h1 + u'</div><hr>'
        htmlText += u'<div>' + u"h2:       %s" % dataDocument.h2 + u'</div><hr>'
        htmlText += u'<div>' + u"strong:   %s" % dataDocument.strong + u'</div><hr>'
        htmlText += u'<div>' + u"alt:      %s" % dataDocument.alt + u'</div><hr>'
        htmlText += u'<div>' + dataDocument.text + u'</div><hr>'
        htmlText += u'</body></html>'
        
        f=open(path, 'w')
        f.write(htmlText.encode('utf8'))
        f.close()
        webbrowser.open('file://' + path)
