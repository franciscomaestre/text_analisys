#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 12 de jul. de 2016

Partiendo de las sentencias de seoDocument:

  1. Partimos cada sentencia si es muy grande (fingerPrints)
  2. Para cada fingerPrint, buscamos de forma "exacta" en google (hasta un máximo de MAX_FINGER_PRINTS)
  3. Descargamos hasta MAX_LINKS_PER_QUERY de los devueltos por google
  4. Buscamos en el seodocument de estas descargas el texto del fingerPrint    

MAX_FINGER_PRINTS llamadas a google
MAX_LINKS_PER_QUERY*MAX_FINGER_PRINTS descargas de documentos

MAX_FINGER_PRINTS   = 5
MAX_LINKS_PER_QUERY = 3
5 llamadas a google
15 descargas de webs 

TODO: paralelizar google

'''

__all__ = ["Plagiarism"]

# Test -----------------------------------------
if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')
# Test -----------------------------------------

import re
import numpy as np
from bs4.element import NavigableString


from core.concurrence.workers_pool_factory import WorkersPoolFactory
from core.data_mining.web_pages.scrapping_rules import SPLITTER
from config import settings
from core.data_mining.search_engines.google.google_scraper import GoogleScraper
from core.data_mining.search_engines.google import getGoogleHost
from core.data_mining.web_pages.scraper import Scraper
from core.seo.containers.seo_document import SeoDocument

from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

MAX_FINGER_PRINTS = 5     # max queries a google
MAX_LINKS_PER_QUERY = 4   # numero de urls a descargar por cada query a google
MIN_SENTENCE_WORDS = 10   # numero minimo de letras para procesar una sentencia
MAX_WORDS_EXACT_SEARCH = 32  # longitud máxima de la sentencia usada impuesta por la busqueda exacta de google

class Plagiarism(object):
    
    CACHE_PATH = u'/plagiarism'
    
    def __init__(self, seoDocument):
        
        self.seoDocument = seoDocument
        self.link = seoDocument.link
        self.language = seoDocument.language
        self.country = seoDocument.country
        
        self.numWords = len(seoDocument.dataDocument.text.replace(SPLITTER, '').split())
        
        self.fingerPrints = self._getFingerPrints() 
    
    def check(self):
        # CACHE ??
        
        return self._check()
    
    def _check(self):
        
        self._processFingerPrints() ## google search
        
        # collect links
        linkCandidates = []
        for fingerPrint in self.fingerPrints:
            linkCandidates.extend(fingerPrint.links)
        linkCandidates = list(set(linkCandidates))
        
        # ----------------------------------------------------------
        # download pages. paralelize
        plagiarismDict = {} # {linh: []}
        workersPool = WorkersPoolFactory.getPool()
        reponsePool = []
        for link in linkCandidates:
            resp = workersPool.apply_async(_downloadUrl, args=(link, self.language, self.country))
            reponsePool.append(resp)
        
        # wait pool
        seoDownloadedDocument = {}
        for result in reponsePool:
            try:
                seoDocument = result.get(timeout=settings.SEO_TERMS_DOWNLOADER_TIMEOUT)
                if seoDocument:
                    seoDownloadedDocument[seoDocument.link] = seoDocument
            except Exception, ex:
                app_logger.error(u"ERROR: plagiarims_download %s" % ex)
                pass        
        # ----------------------------------------------------------

        for link in linkCandidates:
            try:
                if link in seoDownloadedDocument:
                    seoDocument = seoDownloadedDocument[link]
                    rawHtml = seoDocument.dataDocument.rawHtml
                    # check all fingerPrints
                    for fingerPrint in self.fingerPrints:
                        
                        # find substrings
                        
                        search_string = u' '.join(fingerPrint.fingerPrint.split()[:MAX_WORDS_EXACT_SEARCH])
                        
                        foundPosition = rawHtml.find(search_string) 
                        if foundPosition > -1:
                            plagiarismData = PlagiarismData(link, fingerPrint, foundPosition, seoDocument)     
                            if not link in plagiarismDict:
                                plagiarismDict[link] = []     
                            if not plagiarismData in plagiarismDict[link]: 
                                plagiarismDict[link].append(plagiarismData)                    
            except Exception, ex:
                app_logger.error(u"_checkPlagiarism: %s %s" % (link, ex))            

        return plagiarismDict
        
    def _getFingerPrints(self):
        """
        Partimos las sentencias en bloques de al menos MIN_SENTENCE_SIZE letras para buscar en google.
        """
        fingerPrints = []
        
        sentences = sorted(self.seoDocument.getSentences(), key=len, reverse=True)
        sentences = [s for s in sentences if len(s.split()) > MIN_SENTENCE_WORDS]
        self.seoDocument.sentences = sentences # DEBUG
        
        
        # si hay muchas sentences cogemos MAX_FINGER_PRINTS de forma aleatoria dando mas peso a las mas largas
        if len(sentences) > MAX_FINGER_PRINTS:
            # select random
            np.random.seed(33)
            prob = [np.sqrt(len(s)) for s in sentences]
            sentences = np.random.choice(sentences, 10, prob).tolist()
            sentences.sort(key=len, reverse=True)
        
        for sentence in sentences:
            senteceLength = len(sentence)
            sentence_split = sentence.split()
            numWords = len(sentence_split)
            chunk_size = Plagiarism._getChunkSize(numWords)
            for chunk in Plagiarism._chunks(sentence_split, chunk_size):
                if len(chunk) >= chunk_size:
                    fingerPrint = FingerPrint(senteceLength, self.seoDocument, u' '.join(chunk))
                    if not fingerPrint in fingerPrints:
                        fingerPrints.append(fingerPrint)

        # remove duplicates and sort
        #fingerPrints.sort(key=lambda k: k.senteceLength, reverse=True)

        for index, fingerPrint in enumerate(fingerPrints):
            print index, fingerPrint    

        return fingerPrints

    def _processFingerPrints(self):
        """
        Search fingerPrint in google.
        add link to fingerPrint 
        """
        
        # no guardamos links del dominio
        import tldextract
        parsed_uri = tldextract.extract(self.link)
        domain = u"{}.{}".format(parsed_uri.domain, parsed_uri.suffix)
        
        plagiarismLinks = []
        print 80*'-'
        STEPS = 1  # sentencias buscadas con OR. Funciona mal si las sentencias son largas
        num_fingerPrints = len(self.fingerPrints)
        for index in range(0, num_fingerPrints, STEPS):
        #for fingerPrint in self.fingerPrints:
            fingerPrint = self.fingerPrints[index]
            search_string = u' '.join(fingerPrint.fingerPrint.split()[:MAX_WORDS_EXACT_SEARCH])
            search_string=search_string.strip()
            if STEPS > 1:
                search_string = u'"%s"' % search_string # exact search
            print search_string
            
            ## --- OR search ----
            step = 1
            while step < STEPS and index + step < num_fingerPrints:
                fingerPrint = self.fingerPrints[index + step]
                OR_string = u' '.join(fingerPrint.fingerPrint.split()[:MAX_WORDS_EXACT_SEARCH])
                OR_string=OR_string.strip()
                OR_string = u'"%s"' % OR_string # exact search
                search_string += u' OR %s' % OR_string
                step += 1
            ## --- OR search ----
            
            google = GoogleScraper(search_string,
                                   language=fingerPrint.seoDocument.language,
                                   country=fingerPrint.seoDocument.country,
                                   googleHost=getGoogleHost(fingerPrint.seoDocument.country),
                                   max_results=10)
            
            links = []
            try:
                exactSearch = True if len(search_string.split()) <  MAX_WORDS_EXACT_SEARCH/2 else False
                links = google.search(jump=False, exactSearch=exactSearch)
            except Exception, ex:
                print ex
            
            counter = 0
            for link in links:
                if domain not in link and link not in plagiarismLinks:
                    plagiarismLinks.append(link)
                    fingerPrint.links.append(link)
                    counter += 1
                if counter > MAX_LINKS_PER_QUERY:
                    break

    MIN_CHUNK_SIZE = 25
    @staticmethod
    def _chunks(l, n):
        """Yield successive n-sized chunks from l."""
        
        init_pos = n
        if len(l) > Plagiarism.MIN_CHUNK_SIZE:
            init_pos = Plagiarism.MIN_CHUNK_SIZE 
        yield l[0:init_pos]
            
        for i in range(init_pos, len(l), n):
            yield l[i:i+n]
    
    
    @staticmethod
    def _getChunkSize(numWords):
        """ 
            25   palabras = 1 chunk 
            50   palabras = 2
            100  palabras = 2
            500  palabras = 6
            1000 palabras = 8
        """
        
        parts = int(- 0.00000616*numWords*numWords+0.0128*numWords+1.297)
        return int(numWords/max(1, parts))

def _downloadUrl(url, language, country):
    
    try:
        googleScraper = Scraper(url, sameOrigin=True)
        dataDocument = googleScraper.getDataDocument()
        seoDocument = SeoDocument(url, 
                                  order=1, 
                                  language=language, 
                                  country=country, 
                                  dataDocument=dataDocument, 
                                  cache=False,
                                  initialize=False)    

        return seoDocument
    except Exception, ex:
        app_logger.error(u'plagiarims _downloadUrl: %s' % ex)


class FingerPrint(object):
    def __init__(self, senteceLength, seoDocument, fingerPrint):
        self.senteceLength = senteceLength
        self.seoDocument = seoDocument
        self.fingerPrint = fingerPrint
        self.links = []

    def __eq__(self, other):
        return self.fingerPrint == other.fingerPrint

    def __unicode__(self, *args, **kwargs):
        return u'%s %s' % (self.senteceLength, self.fingerPrint)
    def __str__(self):      # tries to "look nice"
        return unicode(self).encode(sys.stdout.encoding or 'UTF-8', 'replace')    
    def __repr__(self):     # must be unambiguous
        return repr(self.__unicode__(self))


class PlagiarismData(object):
    def __init__(self, link, fingerPrint, position, seoDownloadedDocument):
        
        self.link = link
        self.fingerPrint = fingerPrint
        self.fingerPrintText = fingerPrint.fingerPrint
        self.position = position
        self.length = len(fingerPrint.fingerPrint)
        self.rawHtml = seoDownloadedDocument.dataDocument.rawHtml
        self.numWords = seoDownloadedDocument.dataDocument.bodyWords
        self.fingerNumWords = len(fingerPrint.fingerPrint.split())

    @property
    def key(self):
        return hash(u'%s_%s_%s' % (self.link, self.position, self.fingerPrintText))

    def __eq__(self, other):
        return self.key == other.key

    def __unicode__(self, *args, **kwargs):
        return u'(%s/%s) %s %s' % (self.fingerNumWords, self.numWords, self.link, self.fingerPrintText)
    def __str__(self):      # tries to "look nice"
        return unicode(self).encode(sys.stdout.encoding or 'UTF-8','replace')    
    def __repr__(self):     # must be unambiguous
        return repr(self.__unicode__(self))


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# Test -----------------------------------------

def _getSeodocument(url, rawHtml=None, language=u'es', country=u'ES'):
    if url:
        seoDocument = _downloadUrl(url, language, country)
    else:
        # Get title, h1 ...
        scraper = Scraper(url='http://fake.url.com')
        scraper.rawHtml = rawHtml
        dataDocument = scraper._getDataDocument()
        
        seoDocument = SeoDocument(link='seoTextAudit', order=1, language=language, country=country, dataDocument=dataDocument, cache=False)    
    return seoDocument

def removeEmptyTags(soup):
    empty_tags = []
    parent_tags = []
    for tag in soup.find_all():
        if not tag.contents:
            if tag.name != 'body':
                empty_tags.append(tag)
                parent_tags.append(tag.parent)
    [tag.extract() for tag in empty_tags]

def main():
    """
    language = u'es'
    country = u'ES'
    url = u'https://www.pet-supermarket.co.uk/Dog/Dog-Collars,-Tags-and-Leashes/c/PSGB00054'
    url = u'http://www.tiendanimal.es/comedero-acero-para-gatitos-cachorros-royal-canin-p-12744.html'
    
    """
    language = u'en'
    country = u'US'
    query = u'microsoft office 2010'
    url = u'http://windows-discounter.com/office-2010/'
    url = u'http://getfastdownload.blogspot.com/2014/09/microsoft-office-2010.html'
    url = u'https://2a1-blog.phpnuke.org/en/c388140/php-returning-values-by-reference'
    url = u'https://2a1-downloads.phpnuke.org/en/c388143/five-nights-at-freddy-s-4'
    url = u'https://2msoffice-downloads.phpnuke.org/en/c09262/microsoft-office-2010'    


    language = u'es'
    country = u'ES'
    
    url = u'http://www.europapress.es/murcia/noticia-consumur-revisara-coste-alguno-prestamos-hipotecarios-consumidores-no-conozcan-si-tienen-clausula-suelo-20160716102947.html'
    url = u'https://es.wikipedia.org/wiki/Adolf_Hitler'    

    seoDocument = _getSeodocument(url, textExample, language=language, country=country)
    plagiarismData = Plagiarism(seoDocument).check()
    rawHtml = seoDocument.dataDocument.rawHtml
    
    
    # --------------------------------------------------------------------------------------------
    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'
    
    htmlText = u"<html><head><meta charset='UTF-8' /></head><body>"
    htmlText += u'<div><strong><a href="%s">%s' % (url, url) + u'</a></strong></div><br/>'

    htmlText += u'<div>Sentencias</div><br/>'
    for index, sentence in enumerate(seoDocument.sentences):
        htmlText += u'<div>%-2s %s' % (index, sentence) + u'</div>'
        if index > 50: break
    htmlText += u'<hr><br/><br/>'
    
    
    # sort plagiarismData
    # count ocurrences
    from collections import OrderedDict
    plagiarismDataFrec = [(link, len(dataList)) for link, dataList in plagiarismData.items()]
    plagiarismDataFrec = OrderedDict(sorted(plagiarismDataFrec, key=lambda t: t[1], reverse=True))
    
    for link in plagiarismDataFrec.keys():
        
        dataList = plagiarismData[link]
        
        htmlText += u'<div><a href="%s">%s' % (link, link) + u'</a></div><hr><br/>'
        print link
        htmlText += u'<table><tr>'
        for d in dataList:
            # htmlText += u'<td> %s' % (d.position,) + u'</td>'
            htmlText += u'<td> %s' % (d.fingerPrintText,) + u'</td>'
            print d
        htmlText += u'</tr></table><br/>'
        print 80*'-'
    
    
    from lxml.html.diff import htmldiff
    from bs4 import BeautifulSoup
    for link, data in plagiarismData.items():
    
        ## diff rawHtml <--> data.rawHtml
        ## pone <ins></ins> y <del></del> en lo que no coincide
        style_string = u''''
        <style>
            .diff *{background-color: #fff !important; }
            ins {background-color: #fff !important; text-decoration: none;}
            ins *{background-color: #fff !important; }
            del {background-color: #d99 !important;  text-decoration: none;}
            del *{background-color: #d99 !important; text-decoration: none;}
        </style>
        '''
        
        htmlText += style_string
        
        soupFirstDoc = BeautifulSoup(rawHtml, 'lxml')

        diff_text = htmldiff(rawHtml,data[0].rawHtml)
        soup = BeautifulSoup(diff_text, 'lxml')
        [elem.extract() for elem in soup.find_all('ins')]
        
        # cambiamos con las diferencias
        import copy
        soupFirstDoc.body.extract()
        soupFirstDoc.html.append(copy.copy(soup.body))
        ##soupFirstDoc.body.string = unicode(soup.body.contents[0])
        
        # ----------------------------------
        from experiments.others.local_web import get_local_web
        final_soup = get_local_web(url, soupFirstDoc)
        style = final_soup.new_tag('style', type='text/css')
        style.string = style_string
        final_soup.head.append(style)
        
        """
        removeEmptyTags(final_soup)
        removeEmptyTags(final_soup)
        removeEmptyTags(final_soup)
        """
        
        htmlText = unicode(final_soup)
        break
        # ----------------------------------

        # absolute urls
        iframe_text = u'<br/><hr><br/><div>%s</div><br/>'        
        import urlparse
        base_path = soup.base['href'] if soup.base and 'href' in soup.base else url
        for tag in soup.findAll(['a', 'link'], href=True):
            if not bool(urlparse.urlparse(tag['href']).netloc):
                tag['href'] = urlparse.urljoin(base_path, tag['href'])
        for tag in soup.findAll(['img'], src=True):
            if not bool(urlparse.urlparse(tag['src']).netloc):
                tag['src'] = urlparse.urljoin(base_path, tag['src'])
        
        copy_elements = [elem for elem in soup.find_all(re.compile("[^(ins)]"))]
        for element in copy_elements:
            if not isinstance(element, NavigableString):
                continue
            
            element = element.parent
            if 'style' in element:
                element['style'] += ";background-color: #d99 !important;"
            else:
                element['style']="background-color: #d99 !important;"

        #import base64
        #data = u'data:text/html;base64,%s' % base64.b64encode(str(soup))  # firefox ...
        iframe_text = iframe_text % unicode(soup)
        htmlText += iframe_text
        break
        
    f=open(path, 'w')
    f.write(htmlText.encode('utf8'))
    f.close()
    webbrowser.open('file://' + path)

textExample = '''
Microsoft Office 2010 is a productivity suite which integrates office tools for personal and professional use. It includes a wide range of basic and advanced features that can help you to perform any task in a fast, efficient and productive way. Microsoft Office 2010 has come with renovated and new features for all the applications included in this package. Among Word, PowerPoint and Excel this pack integrates some other utilities such as Outlook, Access, Publisher or OneNote. All the programs come with a renovated ribbon interface and a backstage view which are particularly of this version. However, one of the most interesting features of Microsoft Office 2010 is the online live collaboration feature, which allows the different users to work on the same document simultaneously. Microsoft Office 2010 Features The main features of Microsoft Office 2010 are the 
'''

if __name__ == '__main__':
    main()
    
    