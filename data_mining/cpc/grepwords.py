#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from urllib3.util.retry import Retry
from core.cache.file_storage_factory import FileStorageFactory
from config import settings
from utils.logger import LoggerFactory

#---------------------------

DISPLAY = True

app_download_logger = LoggerFactory.getInstance('downloader')  

# -----------------------------------------------------------------
# -- GrepWord
# -----------------------------------------------------------------
GREPWORD_COUNTYRY_LOCATION = {
                              'AU': 'australia',
                              'IE': 'ireland',
                              'NZ': 'newzealand',
                              'CA': 'canada',
                              'IN': 'india',
                              'IS': 'israel',
                              'MX': 'mexico',
                              'AR': 'argentina',
                              'UK': 'united_kingdom',
                              'GB': 'united_kingdom',
                              'IT': 'italy',
                              'FR': 'france',
                              'ES': 'spain',
                              'DE': 'germany',
                              'US': '',
                              }
class GrepWordsApi(object):
    """
    url = http://api.grepwords.com/related
    paramsUrl
        'apikey' => 'f4e40c3f83ab1fd',
        'loc' => $loc,
        'results' => 1000,
        'output' => 'json',
        'start' => $start * 900
        
        // en us se puede ver la competencia (está mal escrito pero es así)
        if country == 'us':
            'sort' = 'competetion'
        }                
        
        if len($keyword) <= MIN_KEYWORDS_LEN:
            'regex' = '1'
            'q' = ' ^query$ '
        else:
            'q' = keyword
                
    Result:
         keyword
         cpc
         cmp  competencia [0-1.0] ??
         ams  ¿volumen medio?          
         
         m1 - m12  (volumen por mes??)
         ud  2015-06-27
         country
    """
    
    URL_TEMPLATE = u'http://api.grepwords.com/related'
    CACHE_PATH = u'/grepWordsApi'    
    
    MIN_KEYWORDS_LEN = 3
    
    def __init__(self, max_results=10, step_size=1000, api_key=settings.GREPWORD_API_KEY):
        self.max_results = max_results
        self.step_size = step_size
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getProxyPool()

    def search(self, query, country, competence_limit=settings.GREPWORD_CMP_LOWER_LIMIT, max_steps=settings.GREPWORD_MAX_STEPS):
        self.step = 1
        self.items = {}
        country = country.upper()
        fileStorage = FileStorageFactory.getFileStorage(GrepWordsApi.CACHE_PATH)
        key = u'grepWords_%s_%s' % (query, country)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            location = GREPWORD_COUNTYRY_LOCATION.get(country, '')
            self._search(query, location, 0, competence_limit=competence_limit, max_steps=max_steps)
            self.items = self.items.values()
            self.items.sort(key=lambda x: x.cpc, reverse=True)
            result = self.items[0:self.max_results]
            fileStorage.set(key, result)
        return result
    
    def _search(self, query, location, position, competence_limit, max_steps):
        try:
            fields = {}
            fields['apikey'] = self.api_key
            fields['q'] = query.encode('utf8')
            fields['loc'] = location
            fields['results'] = self.step_size
            fields['output'] = 'json'
            fields['start'] = position
            if not location:
                fields['sort'] = 'competetion'

            request = self.pool.request('GET', GrepWordsApi.URL_TEMPLATE, fields=fields, retries=Retry(connect=2, read=2, redirect=2))
            print request.data
            data = json.loads(request.data)   
            
            counter = 0
            previousSize = len(self.items)
            for item in data:
                try:
                    grep_word = GrepWordsResult(item)
                    if grep_word.cmp > competence_limit and len(grep_word.keyword.split()) >= GrepWordsApi.MIN_KEYWORDS_LEN and grep_word.cpc > 0:
                        counter += 1
                        self.items[grep_word.keyword] = grep_word
                except Exception as ex:
                    print u'%s' % ex
                    pass
            
            if DISPLAY:
                print u'GrepWordsApi: Recibidas....', (len(data))
                print u'GrepWordsApi: Incremento....', (len(self.items) - previousSize)
            
            # check end
            if len(self.items) < self.max_results * self.step_size and (len(self.items) - previousSize) > 0 and self.step < max_steps:
                self.step += 1
                if DISPLAY:
                    print u'Repetimos...', counter
                try:
                    self._search(query, location, self.step * self.step_size, competence_limit, max_steps)
                except Exception, e:
                    print e
                    pass
            
        except Exception as ex:
            app_download_logger.error(u"GrepWordsApi --> ex:%s" % (ex,))
            raise ex
        
class GrepWordsResult(object):
    """
         keyword
         cpc
         cmp  competencia [0-1.0] ??
         ams  ¿volumen medio?          
         
         m1 - m12  (volumen por mes??)
         ud  2015-06-27
         country    
    """
    
    def __init__(self, json_data):
        self.keyword = u'%s' % json_data['keyword']
        self.score = 0
        
        self.cpc = float(json_data['cpc'])
        self.cmp = float(json_data.get('cmp', json_data.get('competition', 0)))
        self.ams = int(json_data['ams'])
        
        self.country = json_data.get('country', 'US')
        self.ud = json_data.get('ud')
        
        self.m1 = json_data.get('m1')
        self.m2 = json_data.get('m2')
        self.m3 = json_data.get('m3')
        self.m4 = json_data.get('m4')
        self.m5 = json_data.get('m5')
        self.m6 = json_data.get('m6')
        self.m7 = json_data.get('m7')
        self.m8 = json_data.get('m8')
        self.m9 = json_data.get('m9')
        self.m10 = json_data.get('m10')
        self.m11 = json_data.get('m11')
        self.m12 = json_data.get('m12')
        
        
    @property
    def query(self):
        return self.keyword
    
    def getInfo(self):
        return {
                'query': self.query,
                'cpc': self.cpc,
                'competition': self.cmp,
                'score': self.score,
                }
    
    def __repr__(self, *args, **kwargs):
        return u'%s --> cpc: %s competition: %s score = %s' % (self.query, self.cpc, self.cmp, self.score)
        
    def __str__(self, *args, **kwargs):
        return u"%-60s cpc:%s cmp:%s" % (self.keyword, self.cpc, self.cmp)
