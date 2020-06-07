#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from config import settings
# from config import BING_API_KEY, CACHE
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
import urllib3
from utils.logger import LoggerFactory
from urllib3.util.retry import Retry
app_download_logger = LoggerFactory.getInstance('downloader')

class BingException(Exception):
    pass

class BingRelatedSearch(object):
    
    CACHE_PATH = '/bingRelated'

    QUERY_URL = u'https://api.datamarket.azure.com/Bing/Search/v1/RelatedSearch'

    def __init__(self, api_key=settings.BING_API_KEY):
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getSameOriginPool()

    def search(self, query, limit=50, offset=0, market='es-ES'):
        try:
            query = query.encode('utf8')
        except:
            pass
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        fileStorage = FileStorageFactory.getFileStorage(BingRelatedSearch.CACHE_PATH)
        key = 'bingRelated_%s_%s' % (query, market)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search(query, limit, offset, market)
            result = [ u'%s' % query.title for query in result]
            fileStorage.set(key, result)
        return result
    
    def search_all(self, query, limit=50, market='es-ES'):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        fileStorage = FileStorageFactory.getFileStorage(BingRelatedSearch.CACHE_PATH)
        key = u'bingRelated_all_%s_%s' % (query, market)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search_all(query, limit, market)
            result = [ u'%s' % query.title for query in result]
            fileStorage.set(key, result)
        return result
    
    def _search_all(self, query, limit=50, market='es-ES'):
        ''' Returns a single list containing up to 'limit' Result objects'''
        results, next_link = self._search(query, limit, 0, market)
        while next_link and len(results) < limit:
            maxValue = limit - len(results)
            more_results, next_link = self._search(query, maxValue, len(results), market)
            if not more_results:
                break
            results += more_results
            
        app_download_logger.info(u"Bing search query: %s" % query)    
        return results

    def _search(self, query, limit, offset, market):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        fields = {
            '$skip':offset,
            '$format': 'json',
            'Market': u"'%s'" % market,
            'Options':"'DisableLocationDetection'"
        }
        
        try:
            fields['Query'] = query.encode('utf8')  # query to lookup
        except:
            fields['Query'] = query  # query to lookup
        
        headers = urllib3.util.make_headers(basic_auth='%s:%s' % ("", self.api_key))

        request = self.pool.request('GET', BingRelatedSearch.QUERY_URL, fields=fields, headers=headers, retries=Retry(connect=2, read=2, redirect=2))
        response = request.data        
        json_results = json.loads(response)        
        try:
            next_link = json_results['d']['__next']
        except:
            next_link = ''
        
        if not json_results:
            return [], ''
        return [Result(single_result_json) for single_result_json in json_results['d']['results']], next_link

class Result(object):
    '''
    The class represents a SINGLE search result.
    Each result will come with the following:
    #For the actual results#
    title: title of the result
    url: the url of the result
    description: description for the result
    id: bing id for the page
    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part WebResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):
        self.url = result['BingUrl']
        self.title = result['Title']
        self.id = result['ID']

        self.meta = self._Meta(result['__metadata'])
        
    def __str__(self, *args, **kwargs):
        return u'%s' % (self.title)
