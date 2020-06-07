#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import re
from config import settings
from concurrence.workers_pool_factory import WorkersPoolFactory
from concurrence.callback_wait import CallbackWait
from cache.file_storage_factory import FileStorageFactory
from seo.containers.seo_library import SeoLibrary
from seo.containers.seo_document import SeoDocument

from utils.logger import LoggerFactory
import random
from data_mining.search_engines.google.google_api_search import GoogleSearchEngine
from data_mining.search_engines.google import getGoogleHost
from data_mining.search_engines.google.google_scraper import GoogleScraper
from data_mining.search_engines.bing.bing_search import BingSearch
from data_mining.web_pages.scraper import Scraper

app_download_logger = LoggerFactory.getInstance('downloader')
app_logger = LoggerFactory.getInstance('app')


class SeoDocumentDownloader(object):
    
    CACHE_PATH = u'/queryDocumentsDownloaded'
    
    def __init__(self, query, language='es', country='ES', 
                       searchEngine = settings.DOWNLOADER_SEARCH_ENGINE, 
                       downloadLimit=settings.SEO_TERMS_DOWNLOAD_LIMIT, 
                       sameOrigin=False,
                       useProxy=False):
        
        self.query = query
        self.language = language
        self.country = country
        self.lock = threading.RLock()
        ##self.condition = CallbackWait()
        self.links = []
        self.searchEngine = searchEngine
        self.downloadLimit = downloadLimit
        self.sameOrigin = sameOrigin
        self.useProxy = useProxy
    
    def getSeoLibrary(self):
        seoLibrary = SeoLibrary(self.query, self.language, self.country)
        #Ordenamos los documentos respecto al orden de aparición en google
        seoLibrary.seoDocuments = self.getSeoDocuments()
        return seoLibrary
    
    def getSeoDocuments(self):
        '''
        seoDocuments es un Diccionario porque de esa forma podíamos eliminar aquellos enlaces que estuvieran
        fallando sin tener que esperar a que sonara el timeout del pool
        
        https://docs.python.org/2/library/multiprocessing.html
        http://stackoverflow.com/questions/3160909/how-do-i-deal-with-certificates-using-curl-while-trying-to-access-an-https-url
        
        '''
        fileStorage = FileStorageFactory.getFileStorage(SeoDocumentDownloader.CACHE_PATH)
        key = u'seoDocumentDownloader_%s_%s_%s_%s' % (self.query, self.language, self.country, self.downloadLimit)
        seoDocumentDict = fileStorage.get(key, default={})
        if not seoDocumentDict or not settings.CACHE or settings.SCRAPER_RELOAD_CONTENT:
            self.getLinks()
            
            downloadPool = WorkersPoolFactory.getPool()
            # print u'Urls to download: '
            # print self.links
            app_download_logger.info(u'Urls to download: ')
            app_download_logger.info(self.links)
            
            results = []
            
            regex = re.compile(settings.FORBIDDEN_URLS)
            
            for order, link in enumerate(self.links):
                #print u'%s --> %s' % (order, link)
                if not regex.search(link):
                    result = downloadPool.apply_async(getSeoDocumentConcurrence, 
                                                      args=(link, order, self.language, self.country, self.sameOrigin, self.useProxy))
                    results.append(result)
            
            seoDocumentDict = {}

            for result in results:
                try:
                    seoDocument = result.get(timeout=settings.SEO_TERMS_DOWNLOADER_TIMEOUT)
                    if seoDocument:
                        seoDocumentDict[seoDocument.link] = seoDocument
                    else:
                        app_download_logger.error(u"No seoDocument or timeout")
                except Exception as ex:
                    app_download_logger.error(u"%s" % ex)
                    pass
            # Con esto nos aseguramos que no haya url repetidas
            
            app_download_logger.info(u'Number of documents downloaded (AFTER): %s' % len(seoDocumentDict))
            app_download_logger.info(u'Max to download: %s' % len(self.links))
            # print u'Number of documents downloaded (AFTER): %s' % len(seoDocumentDict)
            # print u'Max to download: %s' % len(self.links)
            
            fileStorage.set(key, seoDocumentDict)
        
        return sorted(seoDocumentDict.values(), key=lambda x: x.order, reverse=False)[0:self.downloadLimit]

    def getLinks(self):
            
        if self.searchEngine == 'google':
            return self.getGoogleLinks()
        else:
            return self.getBingLinks()
            
    
    def getGoogleLinks(self):
        if not self.links:
            usePaidVersion = random.randint(0, 99) >= settings.GOOGLE_SCRAPER_PROBABILITY
            
            try:
                if usePaidVersion:
                    searchEngine = GoogleSearchEngine(self.query,
                                                      self.language,
                                                      self.country,
                                                      getGoogleHost(self.country),
                                                      max_results=self.downloadLimit)
                    self.links = searchEngine.search()
                else:
                    googleScrapper = GoogleScraper(query=self.query,
                                             language=self.language,
                                             country=self.country,
                                             googleHost=getGoogleHost(self.country),
                                             max_results=self.downloadLimit)
                    self.links = googleScrapper.search()
            except Exception, e:
                app_logger.info(u'%s' % e)
                app_logger.info(u'Google Scrapper and API failed. Trying Bing....')
                try:
                    bing = BingSearch()
                    self.links = bing.search_all(query=self.query, downloadLimit=self.downloadLimit, market=u'%s-%s' % (self.language, self.country))
                except Exception, e:
                    app_logger.info(u'%s' % e)
                    app_logger.info(u'Bing also failed, we are lost....')
                    self.links = []
            
        return self.links
        
    def getBingLinks(self):
        if not self.links:
            try:
                bing = BingSearch()
                self.links = bing.search_all(query=self.query, downloadLimit=self.downloadLimit, market=u'%s-%s' % (self.language, self.country))
            except Exception, e:
                app_logger.info(u'%s' % e)
                app_logger.info(u'Bing failed, trying google....')
                try:
                    searchEngine = GoogleSearchEngine(self.query,
                                                      self.language,
                                                      self.country,
                                                      getGoogleHost(self.country),
                                                      max_results=self.downloadLimit)
                    self.links = searchEngine.search()
                except Exception, e:
                    app_logger.info(u'%s' % e)
                    app_logger.info(u'Google Failed, we are lost....')
                    self.links = []
            
        return self.links
    
def getSeoDocumentConcurrence(link, order, language, country, sameOrigin, useProxy):
    try:
        googleScraper = Scraper(link, sameOrigin=sameOrigin, useProxy=useProxy)
        dataDocument = googleScraper.getDataDocument()
        if len(dataDocument.text) > settings.DOCUMENT_MIN_CHARACTERS:
            return SeoDocument(googleScraper.redirectedUrl, dataDocument, order, language, country)
        else:
            app_download_logger.error(u"%s lenght %s < %s chars" % (link, len(dataDocument.text), settings.DOCUMENT_MIN_CHARACTERS))
    except Exception as ex:
        app_download_logger.error(u"%s --> %s" % (link, ex))
        # print(ex)
        # print(u'_Error : %s' % link)
    return None
        
        


    
