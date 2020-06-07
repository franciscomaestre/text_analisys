#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 1 de jul. de 2016

paths = [
        '/var/cache/seologies/semCPC',
        '/var/cache/seologies/seoTerms',
        
        '/var/cache/seologies/dataDocument',
        
        '/var/cache/seologies/readabilityText',
        '/var/cache/seologies/scoredTerms',
        '/var/cache/seologies/classifierData',
        '/var/cache/seologies/detailedTerms',
        '/var/cache/seologies/bingRelated',
        '/var/cache/seologies/semRush',
        '/var/cache/seologies/proxy',
        '/var/cache/seologies/bingSuggestion',
        '/var/cache/seologies/bingSearch ',
        '/var/cache/seologies/spellChecker ',
        '/var/cache/seologies/relatedTerms',
        
        '/var/cache/seologies/queryDocumentsDownloaded',
        '/var/cache/seologies/seoDocument',
        
        '/var/cache/seologies/googleSearchEngine',
         ]

SeoDocumentDownloader
CACHE_PATH = u'/var/cache/seologies/queryDocumentsDownloaded'

Scraper
CACHE_PATH = u'/dataDocument'

SeoDocument  --> getTextTokens()
CACHE_PATH = u'/seoDocument'    


SeoDocumentDownloader    CACHE_PATH = u'/queryDocumentsDownloaded'
    - getSeoDocuments()
        key = u'seoDocumentDownloader_%s_%s_%s' % (self.query, self.language, self.country)
        --> seoDocumentDict[seoDocument.link] = seoDocument
        
        Para cada documento:
        googleScraper = Scraper(link, sameOrigin=sameOrigin)
        dataDocument = googleScraper.getDataDocument() --> fileCache.set(self.url, dataDocument)
        

SeoDocument --> getTextTokens()  --> key = u'tokens_%s_%s_%s' % (self.link, self.language, self.country)        
    

1. Recalcular los tokens de los seodocuments


'''

from os import listdir
from os.path import isfile, join, isdir
import os

def main():
    pass

if __name__ == '__main__':
    main()