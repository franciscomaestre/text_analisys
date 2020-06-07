#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import math
from cache.file_storage_factory import FileStorageFactory
from utils.logger import LoggerFactory
from config import settings
from utils.proxy_manager import ProxyManager
from pyvirtualdisplay import Display
from selenium import webdriver
import urllib
from selenium.webdriver.common.proxy import Proxy, ProxyType

app_error_logger = LoggerFactory.getInstance('app')

class GoogleSelenium(object):
    
    CACHE_PATH = '/googleSearchEngine'
    HOST_TEMPLATE = 'http://%s/search'
    PAGE_LIMIT = 100
    
    def __init__(self, query, language='es', country='ES', googleHost='google.es', max_results=10):
        self.query = query
        self.language = language
        self.country = country
        if not 'http' in googleHost:
            self.googleHost = GoogleSelenium.HOST_TEMPLATE % googleHost
        else:
            self.googleHost = googleHost
        self.max_results = max_results
        
    def search(self, jump=True):
        fileStorage = FileStorageFactory.getFileStorage(GoogleSelenium.CACHE_PATH)
        key = '%s.%s.%s.%s' % (self.query, self.language, self.country, self.max_results)
        links = fileStorage.get(key)
        if not links:
            pages = int(math.ceil(self.max_results * 1.0 / GoogleSelenium.PAGE_LIMIT))
            links = []
            
            try:
                for start in range(pages):
                    links.extend(self._search(start * GoogleSelenium.PAGE_LIMIT))
            except Exception as ex:
                app_error_logger.error(u"%s" % ex)
            
            if not links and jump:
                app_error_logger.error(u"Google Selenium Failed. Trying with SearchEngine")
                from search_engines.google.google_api_search import GoogleSearchEngine
                searchEngine = GoogleSearchEngine(self.query,
                                                  self.language,
                                                  self.country,
                                                  self.googleHost,
                                                  max_results=self.max_results)
                links = searchEngine.search(jump=False)
            
            if not links:
                raise Exception('Google Selenium Error')
            
            uniqueLinks = []
            forbidden_regex = re.compile(settings.FORBIDDEN_URLS)
            for link in links:
                if link not in uniqueLinks:
                    if not forbidden_regex.search(link):                    
                        uniqueLinks.append(link)
                        
            links = uniqueLinks[0:self.max_results]
            fileStorage.set(key, links)
        return links
    
    def _search(self, start):
        payload = {}
        try:
            payload['q'] = self.query.encode('utf8')  # query to lookup
        except:
            payload['q'] = self.query  # query to lookup
        payload['start'] = start  # start point
        payload['gl'] = self.country  # query from country
        payload['hl'] = self.language  # user query language
        payload['lr'] = 'lang_%s' % self.language  # restrict language pages
        payload['num'] = GoogleSelenium.PAGE_LIMIT
        payload['safe'] = 'off'
        
        params = urllib.urlencode(payload)
        
        display = Display(visible=0, size=(800, 600))
        try:
            display.start()
            
            proxyInfo = ProxyManager.getNextProxy()
            
            myProxy = '%s:%s' % (proxyInfo.host, proxyInfo.port)
    
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': '' # set this value as desired
                })
            
            driver = webdriver.Firefox(proxy=proxy)
            
            try:
                '''
                Cualquier fallo aquí, revisar que la ip está dada de alta
                en buyproxies.com
                '''
                driver.implicitly_wait(10)
                
                driver.get('%s?%s' % (self.googleHost,params))
                
                app_error_logger.info(u"%s" % driver.current_url)
                
                results = []
                
                h3List = driver.find_elements_by_xpath("//h3[@class='r']")
                
                for h3 in h3List:
                    link = h3.find_element_by_tag_name('a')
                    results.append(link.get_attribute("href"))
                    
            except Exception as ex:
                raise ex
            
            finally:
                driver.close()
                
        except Exception as ex:
            raise ex
        
        finally:
            display.stop()
        
        if not results:
            ProxyManager.invalidateProxy()
        
        return results
    

def main():
    
    google = GoogleSelenium('buy balls',
                           language='en',
                           country='GB',
                           googleHost='google.co.uk',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    google = GoogleSelenium('comprar pelotas',
                           language='es',
                           country='ES',
                           googleHost='google.es',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    google = GoogleSelenium('mangare spagetti',
                           language='it',
                           country='IT',
                           googleHost='google.it',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    google = GoogleSelenium('acheter ea',
                           language='fr',
                           country='FR',
                           googleHost='google.fr',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    google = GoogleSelenium('cristiano ronaldo',
                           language='pt',
                           country='PT',
                           googleHost='google.pt',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    google = GoogleSelenium('buy balls',
                           language='en',
                           country='US',
                           googleHost='google.com',
                           max_results=40)
    
    results = google._search(0)
    
    print(len(results))
    
    
    
    #for result in results:
    #    print(result)

if __name__ == '__main__':
    main()
