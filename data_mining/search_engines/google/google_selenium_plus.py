#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import math
from core.cache.file_storage_factory import FileStorageFactory
from utils.logger import LoggerFactory
from config import settings
from utils.proxy_manager import ProxyManager
from pyvirtualdisplay import Display
from selenium import webdriver
import urllib
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import random
import time


app_logger = LoggerFactory.getInstance('app')

class GoogleSeleniumPlus(object):
    
    CACHE_PATH = u'/googleSearchEngine'
    HOST_TEMPLATE = u'http://%s/#'
    HOST_COM_TEMPLATE = u'http://%s/ncr#'
    PAGE_LIMIT = 100
    
    CHANGE_MATRIX = {
        'a': ('s', 80),
        'b': ('v', 75),
        'v': ('b', 78),
        'm': ('n', 74),
        't': ('y', 78)
    }
    
    def __init__(self, query, language=u'es', country=u'ES', googleHost=u'google.es', max_results=10):
        self.query = query
        self.language = language
        self.country = country
        if not u'http' in googleHost:
            if u'.com' in googleHost:
                #El .com necesita el parametro No Country Redirect si la IP no es de US
                self.googleHost = GoogleSeleniumPlus.HOST_COM_TEMPLATE % googleHost
            else:
                self.googleHost = GoogleSeleniumPlus.HOST_TEMPLATE % googleHost
        else:
            self.googleHost = googleHost
        self.max_results = max_results
        
    def search(self, jump=True):
        fileStorage = FileStorageFactory.getFileStorage(GoogleSeleniumPlus.CACHE_PATH)
        key = u'%s.%s.%s.%s' % (self.query, self.language, self.country, self.max_results)
        links = fileStorage.get(key)
        if not links:
            pages = int(math.ceil(self.max_results * 1.0 / GoogleSeleniumPlus.PAGE_LIMIT))
            links = []
            
            try:
                for start in range(pages):
                    links.extend(self._search(start * GoogleSeleniumPlus.PAGE_LIMIT))
            except Exception as ex:
                app_logger.error(u"%s" % ex)
            
            if not links and jump:
                from core.data_mining.search_engines.google.google_api_search import GoogleSearchEngine
                app_logger.error(u"Google Selenium Failed. Trying with SearchEngine")
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
    
    def _search(self, start, visible=0):
        payload = {}
        try:
            payload['q'] = self.query.encode('utf8')  # query to lookup
        except:
            payload['q'] = self.query  # query to lookup
        payload['start'] = start  # start point
        payload['gl'] = self.country  # query from country
        payload['hl'] = self.language  # user query language
        payload['lr'] = 'lang_%s' % self.language  # restrict language pages
        payload['num'] = GoogleSeleniumPlus.PAGE_LIMIT
        payload['safe'] = 'off'
        
        params = urllib.urlencode(payload)
        
        display = Display(visible=visible, size=(800, 600))
        display.start()
        try:
            proxyInfo = ProxyManager.getNextProxy()
            
            myProxy = u'%s:%s' % (proxyInfo.host,proxyInfo.port)
    
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': '' # set this value as desired
                })
    
            browser = webdriver.Firefox(proxy=proxy)
            browser.set_page_load_timeout(30)
            try:
                params = urllib.urlencode(payload)
    
                browser.implicitly_wait(10)
    
                browser.get(u'%s#%s' % (self.googleHost,params))
                
                app_logger.info(u"%s" % browser.current_url)
                
                h3List = browser.find_elements_by_xpath("//h3[@class='r']")
                
                results = []
                
                for h3 in h3List:
                    link = h3.find_element_by_tag_name('a')
                    results.append(link.get_attribute("href"))
                        
                box = browser.find_element_by_id('lst-ib')
                
                partialQuery = u' '.join(self.query.split()[1:])
                
                for _letter in partialQuery: 
                    box.send_keys(Keys.BACKSPACE)
                    randomSleep(0.03, 0.05)
                
                typeQuery(box, partialQuery)      
    
                randomSleep(0.05, 0.25)
                print u'-'*80
            
            finally:
                browser.close()
        
        except Exception as ex:
            raise ex
        
        finally:
            display.stop()
        
        if not results:
            ProxyManager.invalidateProxy()
        
        return results
 
def randomSleep(minTime, maxTime):
    meanTime = (maxTime + minTime) * 0.50
    sigma = (maxTime + meanTime) * 0.33  
    timetoSleep = max(min(random.normalvariate(meanTime, sigma), maxTime),minTime)
    time.sleep(timetoSleep)

def typeLetter(box, letter, mistakes = True):
    if letter in GoogleSeleniumPlus.CHANGE_MATRIX:
        if random.uniform(1, 100) > GoogleSeleniumPlus.CHANGE_MATRIX[letter][1] and mistakes:
            #Si la letra está en la matriz, evaluamos que
            #pueda equivocarse
            box.send_keys(u'%s' % GoogleSeleniumPlus.CHANGE_MATRIX[letter][0])
            if random.uniform(1, 100) > 65:
                #Corregir ahora o después
                randomSleep(0.2, 0.4)
                box.send_keys(Keys.BACKSPACE) 
                randomSleep(0.1, 0.2)
                box.send_keys(u'%s' % letter)
                return letter
            else:
                return GoogleSeleniumPlus.CHANGE_MATRIX[letter][0]
        else:
            box.send_keys(u'%s' % letter)
            randomSleep(0.04, 0.08)
            return letter
    else:
        box.send_keys(u'%s' % letter)
        randomSleep(0.04, 0.08)
        return letter
            
def typeWord(box, word, mistakes = True, lastWord=False):
    typed = ''
    for letter in word:    
        typed += typeLetter(box, letter, mistakes)
    if word == typed:
        if not lastWord:
            randomSleep(0.05, 0.15)
            box.send_keys(Keys.SPACE)
    else:
        reTypeWord(box, word, typed)
    
def reTypeWord(box, word, typed):
    index = 0
    for i in range(0,len(word)):
        if word[i] != typed[i]:
            index = i
            break
    
    secondType = word
    
    if random.uniform(1, 100) > 30:
        secondType = word[index:]
        
    for _letter in secondType: 
        box.send_keys(Keys.BACKSPACE)
        randomSleep(0.03, 0.05)
        
    randomSleep(0.04, 0.08)
    typeWord(box, secondType, mistakes = False)
    
def typeQuery(box, query):
    words = query.split()
    for idx,word in enumerate(words):
        typeWord(box, word, lastWord=(idx==len(words)-1))
    box.send_keys(Keys.ENTER)

def main():
    
    google = GoogleSeleniumPlus(u'buy balls',
                           language='en',
                           country='GB',
                           googleHost='google.co.uk',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    google = GoogleSeleniumPlus(u'comprar pelotas',
                           language='es',
                           country='ES',
                           googleHost='google.es',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    google = GoogleSeleniumPlus(u'mangare spagetti',
                           language='it',
                           country='IT',
                           googleHost='google.it',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    google = GoogleSeleniumPlus(u'acheter eau',
                           language='fr',
                           country='FR',
                           googleHost='google.fr',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    google = GoogleSeleniumPlus(u'cristiano ronaldo',
                           language='pt',
                           country='PT',
                           googleHost='google.pt',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    google = GoogleSeleniumPlus(u'buy balls',
                           language='en',
                           country='US',
                           googleHost='google.com',
                           max_results=40)
    
    results = google._search(0)
    
    print len(results)
    
    
    
    #for result in results:
    #    print result

if __name__ == '__main__':
    main()
