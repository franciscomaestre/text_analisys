#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import settings
# from config import CACHE, SEMRUSH_KEY,\
#    SEMRUSH_CPC_LOWER_LIMIT, SEMRUSH_CO_LOWER_LIMIT, SEMRUSH_REAL_IP

from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
from urllib3.util.retry import Retry
import StringIO
import csv

from utils.logger import LoggerFactory
app_download_logger = LoggerFactory.getInstance('app')

DISPLAY = False

class SemRushApi(object):
    
    CACHE_PATH = u'/semRush'

    URL_TEMPLATE = u'http://api.semrush.com'

    def __init__(self, api_key=settings.SEMRUSH_KEY):
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getSameOriginPool()

    def search(self, query, country='es', requestType='phrase_fullsearch', limit=settings.SEMRUSH_DISPLAY_LIMIT):
        ''' 
        Returns the result list,
        requestType = 'phrase_related' | 'phrase_fullsearch' 
        '''
        fileStorage = FileStorageFactory.getFileStorage(SemRushApi.CACHE_PATH)
        key = 'SemRush_%s_%s_%s' % (query, country, requestType)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search(query, country, requestType, limit)
            fileStorage.set(key, result)
        return result

    def _search(self, query, country, requestType, limit):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        
        """
        try:
            # conver to str object. No es necesario, lo hace el pool al hacer el urlencode de los fields...
            query = query.encode('utf8')
        except:
            pass
        """
        
        fields = {
            'type': requestType,
            'key': self.api_key,
            'export_colums': 'Ph,Nq,Cp,Co,Nr,Td',
            'phrase': query.encode('utf-8'),
            'database': country,
            'display_filter': '-|Co|Lt|%s|-|Cp|Lt|%s' % (settings.SEMRUSH_CO_LOWER_LIMIT, settings.SEMRUSH_CPC_LOWER_LIMIT),
            'display_sort': 'cp_desc',
            'display_limit': limit
        }
        headers = {
                   'X-Real-IP': settings.SEMRUSH_REAL_IP,
        }
        
        request = self.pool.request('GET', SemRushApi.URL_TEMPLATE,
                                           fields=fields,
                                           headers=headers)
        response = request.data        
        
        # CSV to Data
        # Keyword;Search Volume;CPC;Competition;Number of Results
        
        results = {}
        
        f = StringIO.StringIO(response)
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)  # Skips the headers line
        for row in reader:
            semRushResult = SemRushResult(headers, row, requestType)
            results[semRushResult.data['query']] = semRushResult
            
        return results


class SemRushResult(object):

    HEADER_TRANSLATOR = {
           'Keyword': 'query',
           'Number of Results': 'results',
           'CPC': 'cpc',
           'Competition': 'competition',
           'Average vol.': 'average',
           'Trends': 'trends',
           'Current vol.': 'volume'             
    }
    
    def __init__(self, headers, data, requestType):
        self.requestType = requestType
        self.score = 0
        self.data = {}
        counter = 0
        for header in headers:
            
            h = SemRushResult.HEADER_TRANSLATOR.get(header, header.lower())
            if h == 'query' or h == 'trends':
                self.data[h] = u'%s' % (data[counter].decode('utf8'),)
            else:
                try:
                    self.data[h] = float(data[counter])
                except:
                    self.data[h] = data[counter]
            counter += 1
    
    @property
    def query(self):
        return self.data['query']
    
    @property
    def cpc(self):
        return self.data['cpc']
    @property
    def competition(self):
        return self.data['competition']
    
    @property
    def volume(self):
        return self.data.get('volume', 0)
    
    def getInfo(self):
        return {
                'query': self.query,
                'cpc': self.cpc,
                'competition': self.competition,
                'score': self.score,
                'volume': self.volume
                }
    
    def __repr__(self, *args, **kwargs):
        return u'%s --> cpc: %s competition: %s score = %s' % (self.query, self.cpc, self.competition, self.score)


    

    
    
