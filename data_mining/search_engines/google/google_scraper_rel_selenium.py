#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Use Selenium and open: 
    https://www.google.com
    https://www.google.es
    https://www.google.fr

"""

from utils.persistence.file_storage_factory import FileStorageFactory
from utils.logger import LoggerFactory
from utils.proxy_manager import ProxyManager
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import random
import time


app_logger = LoggerFactory.getInstance('app')

class GoogleScraperRelatedSelenium(object):
    # curl "https://www.google.com/complete/search?sclient=psy-ab&q=c&oq=&gs_l=&pbx=1&bav=on.2,or.r_cp.&bvm=bv.124088155,d.d2s&fp=9391b118d8a56416&biw=1920&bih=297&pf=p&gs_rn=64&gs_ri=psy-ab&tok=wSdima2QSRsPhPxH6zKkvA&pq=google"%"20autocomplete"%"20api&cp=1&gs_id=6&xhr=t&tch=1&ech=1&psi=mO1XV73TAob-aJ-bo0A.1465380250414.1" -H "Referer: https://www.google.com/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" --compressed
    CACHE_PATH = '/googleSearchEngineRelated'
    HOST_TEMPLATE = 'http://%s?pws=0'
    HOST_COM_TEMPLATE = 'http://%s/ncr?pws=0#'
    PAGE_LIMIT = 10
    
    CHANGE_MATRIX = {
        'a': ('s', 80),
        'b': ('v', 75),
        'v': ('b', 78),
        'm': ('n', 74),
        't': ('y', 78)
    }
    
    def __init__(self, query, language='es', country='ES', googleHost='google.es'):
        self.query = query
        self.language = language
        self.country = country
        if not 'http' in googleHost:
            if '.com' in googleHost:
                #El .com necesita el parametro No Country Redirect si la IP no es de US
                self.googleHost = GoogleScraperRelatedSelenium.HOST_COM_TEMPLATE % googleHost
            else:
                self.googleHost = GoogleScraperRelatedSelenium.HOST_TEMPLATE % googleHost
        else:
            self.googleHost = googleHost
        
    def search(self):
        fileStorage = FileStorageFactory.getFileStorage(GoogleScraperRelatedSelenium.CACHE_PATH)
        key = '%s.%s.%s.%s' % (self.query, self.language, self.country, self.max_results)
        related = fileStorage.get(key)
        if not related:
            related = []
            try:
                related.extend(self._search(0))
            except Exception as ex:
                app_logger.error(u"%s" % ex)
            
            if not related:
                raise Exception('Google Selenium Related Error')
            
            related = list(set(related))
            fileStorage.set(key, related)
        return related
    
    def _search(self, start, retries=0, visible=0):
        
        display = None
        results = []
        
        try:
            display = Display(visible=visible, size=(800, 600))
            display.start()
        except Exception as ex:
            pass
        try:
            proxyInfo = ProxyManager.getNextProxy()
            
            myProxy = '%s:%s' % (proxyInfo.host,proxyInfo.port)
    
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
                #params = urllib.urlencode(payload)
    
                browser.implicitly_wait(10)
    
                browser.get('%s' % (self.googleHost,))
                
                box = browser.find_element_by_id('lst-ib')
                
                app_logger.info(u"%s" % self.googleHost)
                
                typeQuery(box, self.query)  
                
                # <p class="_e4b"><a href="..">elefantes marinos <b>videos</b></a></p>
                paragraphList = browser.find_elements_by_xpath('//*[@class="_e4b"]')
                
                for p in paragraphList:
                    link = p.find_element_by_tag_name('a')
                    results.append(link.text)

                # fake typing    
                partialQuery = ' '.join(self.query.split()[1:])
                
                for _letter in partialQuery: 
                    box.send_keys(Keys.BACKSPACE)
                    randomSleep(0.03, 0.05)
                
                typeQuery(box, ' '.join(self.query.split()[1:]))      
    
                randomSleep(0.05, 0.25)
            
            finally:
                browser.close()
        
        except Exception as ex:
            raise ex
        
        finally:
            if display:
                display.stop()
        
        if not results:
            ProxyManager.invalidateProxy()
            if retries > 0:
                print 'Reintentando... %s' % self.query
                return self._search(start, retries=retries-1, visible=visible)
        
        return results
 
def randomSleep(minTime, maxTime):
    meanTime = (maxTime + minTime) * 0.50
    sigma = (maxTime + meanTime) * 0.33  
    timetoSleep = max(min(random.normalvariate(meanTime, sigma), maxTime),minTime)
    time.sleep(timetoSleep)

def typeLetter(box, letter, mistakes = True):
    if letter in GoogleScraperRelatedSelenium.CHANGE_MATRIX:
        if random.uniform(1, 100) > GoogleScraperRelatedSelenium.CHANGE_MATRIX[letter][1] and mistakes:
            #Si la letra está en la matriz, evaluamos que
            #pueda equivocarse
            box.send_keys('%s' % GoogleScraperRelatedSelenium.CHANGE_MATRIX[letter][0])
            if random.uniform(1, 100) > 65:
                #Corregir ahora o después
                randomSleep(0.2, 0.4)
                box.send_keys(Keys.BACKSPACE) 
                randomSleep(0.1, 0.2)
                box.send_keys('%s' % letter)
                return letter
            else:
                return GoogleScraperRelatedSelenium.CHANGE_MATRIX[letter][0]
        else:
            box.send_keys('%s' % letter)
            randomSleep(0.04, 0.08)
            return letter
    else:
        box.send_keys('%s' % letter)
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
   
    google = GoogleScraperRelatedSelenium('coches',
                           language='es',
                           country='ES',
                           googleHost='google.es')
    
    results = google._search(0, retries=2)
    
    print(len(results))
    for result in results:
        print(result)

if __name__ == '__main__':
    main()


