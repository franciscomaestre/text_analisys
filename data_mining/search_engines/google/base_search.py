#!/usr/bin/python
# -*- coding: utf-8 -*-


class BaseSearchEngine(object):
    """
    Search Base class
    """
    
    def __init__(self, query, country, language, dateRestrict, max_results=40):
        self.query = query
        self.country = country
        self.language = language
        self.dateRestrict = dateRestrict
        self.url = ''
        self.query_string = ''
        self.items = []
        self.max_results = max_results
 

        # _initialize data
        self._initialize()
    
    def _initialize(self):
        raise NotImplementedError()

    def search(self):
        raise NotImplementedError()
    
    def get_search(self):
        raise NotImplementedError()    
