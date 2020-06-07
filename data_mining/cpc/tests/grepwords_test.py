#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.sem_cpc import _getGrepWordsCPC

if __name__ == '__main__':
    
    query = u'comprar coche'
    country = u'ES'
    language = u'es'
    
    print _getGrepWordsCPC(query, language, country)
        
