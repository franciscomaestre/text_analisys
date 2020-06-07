#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import math
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
from utils.logger import LoggerFactory
import time
import random
from config import settings
from utils.proxy_manager import ProxyManager
import urllib
from core.data_mining.web_pages.scraper import UserAgent


app_logger = LoggerFactory.getInstance('app')

class GoogleScraper(object):
    
    CACHE_PATH = u'/googleSearchEngine'
    HOST_TEMPLATE = u'http://%s/search'
    PAGE_LIMIT = 80
    
    def __init__(self, query, language=u'es', country=u'ES', googleHost=u'www.google.es', max_results=10):
        self.query = query
        self.language = language
        self.country = country
        self.googleHost = GoogleScraper.HOST_TEMPLATE % googleHost
        self.max_results = max_results
        
    def search(self, jump=True, retries=settings.GOOGLE_SCRAPER_RETRIES, exactSearch = False):
        """
        jump: use GoogleSearchEngine if fails
        """
        fileStorage = FileStorageFactory.getFileStorage(GoogleScraper.CACHE_PATH)
        key = u'%s.%s.%s.%s' % (self.query, self.language, self.country, self.max_results)
        links = fileStorage.get(key)
        if not links or not settings.CACHE:
            pages = int(math.ceil(self.max_results * 1.0 / GoogleScraper.PAGE_LIMIT))
            links = []
            
            try:
                for start in range(pages):
                    #links.extend(self._search(start * GoogleScraper.PAGE_LIMIT, retries=retries, exactSearch=exactSearch))
                    previousLen = len(links)
                    links.extend(self._search(len(links), retries=retries, exactSearch=exactSearch))
                    if previousLen == len(links):
                        break
            except Exception as ex:
                app_logger.error(u"%s" % ex)
            
            if not links and jump:
                app_logger.error(u"GoogleScrapper Failed. Trying with SearchEngine")
                from core.data_mining.search_engines.google.google_api_search import GoogleSearchEngine
                searchEngine = GoogleSearchEngine(self.query,
                                                  self.language,
                                                  self.country,
                                                  self.googleHost,
                                                  max_results=self.max_results)
                links = searchEngine.search(jump=False, exactSearch=exactSearch)
            
            if not links:
                raise Exception('Google Scrapper Error')
            
            uniqueLinks = []
            forbidden_regex = re.compile(settings.FORBIDDEN_URLS)
            for link in links:
                if link not in uniqueLinks:
                    if not forbidden_regex.search(link):                    
                        uniqueLinks.append(link)
                        
            links = uniqueLinks
            fileStorage.set(key, links)
            
        return links[0:self.max_results]
    
    def _search(self, start, retries=0, exactSearch=False):
        payload = {}
        try:
            query = self.query.encode('utf8')  # query to lookup
        except:
            query = self.query  # query to lookup
            
        if exactSearch:             
            payload['as_epq'] = query
        else:
            payload['q'] = query
        
        payload['start'] = start  # start point
        payload['gl'] = self.country  # query from country
        payload['hl'] = self.language  # user query language
        payload['lr'] = 'lang_%s' % self.language  # restrict language pages
        payload['num'] = GoogleScraper.PAGE_LIMIT
        payload['safe'] = 'off'
        payload['pws'] = 0
        payload['gws_rd'] = 'cr'
        
        pool = Urllib3PoolFactory.getProxyPool()
        
        # Getting the response in an Object r
        
        time.sleep(random.uniform(0.0, 0.2))
        try:
            r = pool.request('GET', self.googleHost, fields=payload, headers={"User-Agent": UserAgent.old, "Accept" : "text/html" })
        except Exception as ex:
            app_logger.error(u"%s" % ex)
            raise ex
        
        # Create a Beautiful soup Object of the response r parsed as html
        try:
            soup = BeautifulSoup(r.data, 'lxml')
         
            # Getting all h3 tags with class 'r'
            h3tags = soup.find_all('h3', class_='r')
        except Exception as ex:
            print(ex)
            raise ex
         
        results = []
        # Finding URL inside each h3 tag using regex.
        # If found : Print, else : Ignore the exception
        for h3 in h3tags:
            try:
                results.append(urllib.unquote(u'http' + (re.search('http(.+)', h3.a['href']).group(1)).split('&')[0]))
                ##results.append(u'http' + (re.search('http(.+)', h3.a['href']).group(1)).split('&')[0])
            except Exception as ex:
                app_logger.error(u"%s" % ex)
        
        if not results:
            
            # comprobamos si es verdad que no hay resultados
            '''
            <p>Your search - <b>"Microsoft office 2010 has renovated features for all the applications.Some of them and the purpose" OR "even editing there images and even more important to manage and also to work with"</b> - did not match any documents. </p>
            '''
            try:
                search_query = "<b>%s</b>"%query
                if not search_query in r.data:
                    ProxyManager.invalidateProxy()
                    if retries > 0:
                        print u'Reintentando... %s' % self.query
                        time.sleep(random.uniform(0.0, 0.2))
                        return self._search(start, retries-1, exactSearch)
            except Exception as ex:
                print(ex)
                print u'Google Scrapper Error'
        
        return results
    

def main():
    google = GoogleScraper(u'músculos oblicuos',
                           language='es',
                           country='ES',
                           googleHost='google.es',
                           max_results=35)
    
    results = google._search(0)
    
    for result in list(set(results)):
        print result

if __name__ == '__main__':
    main()


