#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from config import settings
# from config import CACHE, BING_AUTOSUGGEST_KEY

from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
from urllib3.util.retry import Retry

from utils.logger import LoggerFactory
app_download_logger = LoggerFactory.getInstance('downloader')

class BingException(Exception):
    pass

class BingSuggestionSearch(object):
    
    CACHE_PATH = u'/bingSuggestion'

    QUERY_URL = u'https://api.cognitive.microsoft.com/bing/v5.0/suggestions/'

    def __init__(self, api_key=settings.BING_AUTOSUGGEST_KEY):
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getSameOriginPool()

    def search(self, query, market='es-ES'):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        fileStorage = FileStorageFactory.getFileStorage(BingSuggestionSearch.CACHE_PATH)
        key = u'BingSuggestion_%s_%s' % (query, market)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._search(query, market)
            fileStorage.set(key, result)
        return result

    def _search(self, query, market):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        
        try:
            query = query.encode('utf8')  # query to lookup
        except:
            pass        
        
        fields = {
            'q': query,
            'Market': market
        }
        
        headers = {
                   'Ocp-Apim-Subscription-Key': self.api_key,
        }
        request = self.pool.request('GET', BingSuggestionSearch.QUERY_URL, fields=fields, headers=headers, retries=Retry(connect=2, read=2, redirect=2))
        response = request.data        
        json_results = json.loads(response)
        suggestions = []        
        try:
            searchSuggestionsList = json_results['suggestionGroups'][0]['searchSuggestions']
            for searchSuggestion in searchSuggestionsList:
                suggestions.append(searchSuggestion['query'])
            return suggestions
        except Exception, e:
            return []
