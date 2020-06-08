#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from utils.persistence.file_storage_factory import FileStorageFactory
from utils.logger import LoggerFactory
import time
import random
from config import settings
from utils.proxy_manager import ProxyManager
import json
from data_mining.web_pages.scraper import UserAgent

app_logger = LoggerFactory.getInstance('app')

class GoogleScraperRelated(object):
    
    # https://www.google.com/complete/search?sclient=psy-ab&q=r&oq=&gs_l=&pbx=1&bav=on.2,or.r_cp.&bvm=bv.124272578,d.d24&fp=e8390a58f788cfaa&biw=1920&bih=470&pf=p&gs_rn=64&gs_ri=psy-ab&tok=vjGv10Jg7D8H4Cwy9lW1uA&pq=ff&cp=1&gs_id=3&xhr=t&tch=1&ech=1&psi=hZNeV9DONIHoUquznYgL.1465815943354.1
    
    CACHE_PATH = '/googleRelated'
    HOST_TEMPLATE = 'https://www.%s/complete/search'  # direct scrapping
    
    # API WARNING: Aug-2015 deprecation :)
    # hay que poner el lenguage en la query: hl='es'
    HOST_TEMPLATE = 'http://suggestqueries.google.com/complete/search' # ?client=firefox&q=YOURQUERY   --> 
    
    def __init__(self, query, language='es', country='ES', googleHost='google.es'):
        # change str to unicode
        #try:
        #    self.query = query.decode('utf8')  # query to lookup
        #except:
        self.query = query  # query to lookup
        
        
        self.language = language
        self.country = country
        if not 'http' in googleHost:
            self.googleHost = GoogleScraperRelated.HOST_TEMPLATE # % googleHost
        else:
            self.googleHost = googleHost
        
    def search(self):
        fileStorage = FileStorageFactory.getFileStorage(GoogleScraperRelated.CACHE_PATH)
        key = '%s.%s.%s' % (self.query, self.language, self.country)
        related = fileStorage.get(key)
        if not related:
            related = []
            
            try:
                related = self._search(retries=settings.GOOGLE_SCRAPER_RETRIES)
            except Exception as ex:
                app_logger.error(u"_googleRelated %s" % ex)
            
            if not related:
                raise Exception('Google Scrapper Related Empty')
            
            fileStorage.set(key, related)
            
        return related
    
    def _search(self, retries=0):
        payload = {}
        try:
            payload['q'] = self.query.encode('utf8')  # query to lookup
        except:
            payload['q'] = self.query  # query to lookup
        #payload['sclient'] = 'psy-ab'
        
       
        payload['gl'] = self.country   # query from country
        payload['hl'] = self.language  # user query language
        payload['lr'] = 'lang_%s' % self.language  # restrict language pages        
        payload['pws'] = 0       # no custom
        payload['gws_rd'] = 'cr' # country select
        
        # old API
        payload['client'] = 'firefox'  # --> json result
        
        pool = Urllib3PoolFactory.getProxyPool()
        
        # Getting the response in an Object r
        time.sleep(random.uniform(0.0, 0.2))
        try:  
            r = pool.request('GET', self.googleHost, fields=payload, headers={"User-Agent": UserAgent.old, "Accept" : "text/html" })
        except Exception as ex:
            app_logger.error(u"_requestError %s" % ex)
            raise ex
         
        # ['repelente', [['repelente<b> mosquitos</b>', 0, [131]], ['repelente<b> para gatos</b>', 0, [131]], ['repelente<b> para perros</b>', 0], ['repelente', 0]], ... 
        results = [] 

        data = json.loads(r.data) 
        if len(data) > 1:
            for itemsData in data[1]:
                ##related_query = BeautifulSoup(itemsData[0], "lxml").getText() 
                related_query = itemsData
                if related_query != self.query:
                    results.append(related_query)

        if not data and not results:
            ProxyManager.invalidateProxy()
            if retries > 0:
                print 'Reintentando(%s)... %s' % (retries, self.query)
                return self._search(retries-1)
        
        return results
    

def main():
    google = GoogleScraperRelated('saltar en parapente',
                                   language='es',
                                   country='ES',
                                   googleHost='google.es')
    
    results = google._search(0)
    
    for result in list(set(results)):
        print(result)

if __name__ == '__main__':
    main()


