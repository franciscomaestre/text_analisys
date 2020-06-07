#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from config import settings
# from config import BING_API_KEY, CACHE
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
import urllib3
from urllib3.util.retry import Retry
from utils.logger import LoggerFactory

app_download_logger = LoggerFactory.getInstance('downloader')

class BingException(Exception):
    pass

class BingSearch(object):
    
    CACHE_PATH = '/bingSearch'

    QUERY_URL = u'https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web' 

    def __init__(self, api_key=settings.BING_API_KEY):
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getSameOriginPool()

    def search(self, query, limit=50, offset=0, market='es-ES'):
        try:
            query = query.encode('utf8')
        except:
            pass
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        fileStorage = FileStorageFactory.getFileStorage(BingSearch.CACHE_PATH)
        key = u'bingSearch_%s_%s' % (query, market)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search(query, limit, offset, market)
            result = [ u'%s' % query.url for query in result]
            fileStorage.set(key, result)
        return result
    
    def search_all(self, query, downloadLimit=50, market='es-ES'):
        try:
            query = query.encode('utf8')
        except:
            pass
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        fileStorage = FileStorageFactory.getFileStorage(BingSearch.CACHE_PATH)
        key = u'bingSearch_all_%s_%s' % (query, market)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search_all(query, downloadLimit, market)
            result = [ u'%s' % query.url for query in result]
            fileStorage.set(key, result)
        return result
    
    def _search_all(self, query, downloadLimit=50, market='es-ES'):
        ''' Returns a single list containing up to 'limit' Result objects'''
        results, next_link = self._search(query, downloadLimit, 0, market)
        while next_link and len(results) < downloadLimit:
            maxValue = downloadLimit - len(results)
            more_results, next_link = self._search(query, maxValue, len(results), market)
            if not more_results:
                break
            results += more_results
            
        app_download_logger.info(u"Bing search query: %s" % query)    
        return results

    def _search(self, query, downloadLimit, offset, market):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''

        fields = {
            'Query': u"'%s'" % query,
            '$skip':offset,
            '$format': 'json',
            'Market': u"'%s'" % market,
            'Options':"'DisableLocationDetection'"
        }
        
        
        headers = urllib3.util.make_headers(basic_auth='%s:%s' % ("", self.api_key))

        request = self.pool.request('GET', BingSearch.QUERY_URL, fields=fields, headers=headers, retries=Retry(connect=2, read=2, redirect=2))
        response = request.data

        json_results = json.loads(response)        
        try:
            next_link = json_results['d']['__next']
        except:
            next_link = ''
        
        if not json_results:
            return [], ''
        return [Result(single_result_json) for single_result_json in json_results['d']['results'][0:downloadLimit]], next_link

class Result(object):

    def __init__(self, result):
        self.url = result['Url']
        self.title = result['Title']
        self.id = result['ID']

    def __str__(self, *args, **kwargs):
        return u'%s' % (self.url)
