#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    https://console.developers.google.com/apis/library?project=seologies-1131

    https://developers.google.com/custom-search/json-api/v1/reference/cse/list
    
    cr             string     Restricts search results to documents originating in a particular country. --> countryCA
                              https://developers.google.com/adwords/api/docs/appendix/geotargeting?csw=1      
    gl             string     Geolocation of end user. 
    hl             string     Sets the user interface language
    googlehost     string     The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search. 
    num            unsigned integer     Number of search results to return. Valid values are integers between 1 and 10, inclusive. 
                                        If the total number of search results is less than the requested number of results, all available search results will be returned.
    start          unsigned integer     The index of the first result to return    
    
    dateRestrict   string     Restricts results to URLs based on date. Supported values include:
                d[number]: requests results from the specified number of past days.
                w[number]: requests results from the specified number of past weeks.
                m[number]: requests results from the specified number of past months.
                y[number]: requests results from the specified number of past years.
                
    cx            string    The custom search engine ID to use for this app.
                            If both cx and cref are specified, the cx value is used.
    cref          string    The URL of a linked custom search engine specification to use for this app.  
    
    googlehost    string    The local Google domain (for example, google.com, google.de, or google.fr) to use to perform the search. 
    siteSearch    string    Specifies all search results should be pages from a given site.

    filter        string     Controls turning on or off the duplicate content filter. "1": Turns on duplicate content filter. 
    sort          string     The sort expression to apply to the results.
 
"""
import urllib
import json
import time

from config import settings
from core.cache.file_storage_factory import FileStorageFactory
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from urllib3.util.retry import Retry

from utils.logger import LoggerFactory
from core.data_mining.search_engines.google.base_search import BaseSearchEngine
app_download_logger = LoggerFactory.getInstance('downloader')
app_error_logger = LoggerFactory.getInstance('app')

# scraper_performance
# #GOOGLE_SEARCH_ENGINE_ID = '002362144926838910221:xepc2glp4sq'

class GoogleSearchEngine(BaseSearchEngine):
    
    URL_TEMPLATE = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s'
    CACHE_PATH = u'/googleSearchEngine'

    def __init__(self, query,
                       language='es',
                       country='ES',
                       googleHost='google.es',
                       dateRestrict=None,
                       max_results=settings.SEO_TERMS_DOWNLOAD_LIMIT,
                       api_key=settings.GOOGLE_SEOLOGIES_API_KEY,
                       search_engine_id=settings.GOOGLE_SEARCH_ENGINE_ID):
        
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self.googleHost = googleHost
        self.pool = Urllib3PoolFactory.getSameOriginPool()

        super(GoogleSearchEngine, self).__init__(query, country, language, dateRestrict, max_results)
    
    def _initialize(self):
        self.url = GoogleSearchEngine.URL_TEMPLATE % (self.api_key, self.search_engine_id)

    def search(self, jump=True, exactSearch=False):
        fileStorage = FileStorageFactory.getFileStorage(GoogleSearchEngine.CACHE_PATH)
        key = u'%s.%s.%s.%s' % (self.query, self.language, self.country, self.max_results)
        links = fileStorage.get(key)
        if not links or not settings.CACHE:
            app_error_logger.error(80 * '-')
            app_error_logger.error('EO EO Estamos usando el metodo de pago $$$$$$')
            app_error_logger.error(80 * '-')
            try:
                self._search(
                             self.dateRestrict,
                             1)
                links = [item.link for item in self.items]
            except Exception as ex:
                app_error_logger.error(u'%s' % ex)
            
            if not links and jump:
                app_error_logger.error(u"GoogleSearchEnginge Failed. Trying with Google Scrapper")
                from core.data_mining.search_engines.google.google_scraper import GoogleScraper
                googleScrapper = GoogleScraper(query=self.query,
                                         language=self.language,
                                         country=self.country,
                                         googleHost=self.googleHost,
                                         max_results=self.max_results)
                links = googleScrapper.search(jump=False, exactSearch=exactSearch)
                    
                    
            if not links:
                raise Exception('Google Download Error')
                
            uniqueLinks = []
            for link in links:
                if link not in uniqueLinks:
                    uniqueLinks.append(link)
            links = uniqueLinks
             
            fileStorage.set(key, links)
        
        return links
    
    def _search(self, dateRestrict=None, startIndex=1, exactSearch=False):
        
        # check response limit
        if len(self.items) >= self.max_results:
            return 

        # 1. add query
        query_string = {}
        
        try:
            query = self.query.encode('utf8')  # query to lookup
        except:
            query = self.query  # query to lookup
        
        if exactSearch:             
            query_string['as_epq'] = query
        else:
            query_string['q'] = query        
        
        
        # 2. country
        if self.country:
            query_string['gl'] = self.country  # query from country
            # query_string['cr'] = "country"%country.upper() # restrict country pages

        # 3. language
        if self.language:
            query_string['hl'] = self.language  # user query language
            query_string['lr'] = 'lang_%s' % self.language  # restrict language pages
            query_string['googlehost'] = self.googleHost  # specify Google Host google.com google.es google.fr...
        
        # 4. date restrict [y1=last year m2==last 2 months  d5==last 5 days ...]
        if dateRestrict:
            query_string['dateRestrict'] = dateRestrict
            # sort by relevance!!!
            # query_string['sort'] = 'rating-stars'
            query_string['sort'] = '' 
        
        # 5. startIndex
        query_string['start'] = startIndex 
        
        # 6. Filter Not duplicate Content
        # query_string['filter'] = 1
        
        # 7. Excluding youtube from results
        query_string['siteSearch'] = '*.youtube.*'
        query_string['siteSearchFilter'] = 'e'
        
        # 8. File Type Filter

        params = urllib.urlencode(query_string)
        
        try:
            request = self.pool.request('GET', "%s&%s" % (self.url, params), retries=Retry(connect=2, read=2, redirect=2))
            response = request.data
        except:
            # print 'First Try Error'
            app_download_logger.error(u"First Try Error %s&%s" % (self.url, params))
            time.sleep(1)
            try:
                request = self.pool.request('GET', "%s&%s" % (self.url, params), retries=Retry(connect=2, read=2, redirect=2))
                response = request.data
            except Exception as ex:
                app_download_logger.error(u"%s&%s  --> ex:%s" % (self.url, params, ex))
                raise ex
    
        data = json.loads(response)

        if data.get("error", False):
            app_error_logger.error(u"%s" % (request.data))
            raise Exception(u'Google Api Error - Check app.log to get more info')
 
        # searchInformation = GoogleSearchEngine.SearchInformation(data.get("searchInformation"))

        GoogleSearchEngine.SearchInformation(data.get("searchInformation"))
        
        # Como vemos arriba, podemos almacenar la información y tratarla
        
        items = data.get("items")
        if items:
            for item in items:
                item = GoogleSearchEngine.Item(item)
                self.items.append(item)
        
        nextPage = None
        if 'queries' in data and 'nextPage' in data['queries']:
            nextPage = GoogleSearchEngine.NextPage(data['queries'].get("nextPage")[0])
            
        if nextPage:  # parallel ...
            self._search(dateRestrict, nextPage.startIndex, exactSearch)        

    class SearchInformation(object):
        def __init__(self, data):
            self.searchTime = float(data["searchTime"])
            self.formattedSearchTime = data["formattedSearchTime"]
            self.totalResults = int(data["totalResults"])
            self.formattedTotalResults = data["formattedTotalResults"]

   
    class NextPage(object):
        def __init__(self, data):
            self.title = data["title"]
            self.totalResults = int(data["totalResults"])
            self.searchTerms = data["searchTerms"]
            self.count = int(data["count"])
            self.startIndex = int(data["startIndex"])
            self.inputEncoding = data["inputEncoding"]
            self.outputEncoding = data["outputEncoding"]
            self.safe = data["safe"]
            self.cx = data["cx"]

            self.hl = data["hl"] if "hl" in data else ''
            self.gl = data["gl"] if "gl" in data else '' 
            
   
    class CseImage(object):
        def __init__(self, data):
            self.has_data = False
            if not data: return
            self.has_data = True
            self.src = data.get("src")
                
        def to_json(self):
            if not self.has_data:
                return { 'has_data':False }
            return { 'has_data':True,
                     'src':self.src,
                    }
                
    class CseThumbnail(object):
        def __init__(self, data):
            self.has_data = False
            if not data: return
            self.has_data = True
            self.width = data.get("width")
            self.height = data.get("height")
            self.src = data.get("src")
        
        def to_json(self):
            if not self.has_data:
                return { 'has_data':False }
            return { 'has_data':True,
                     'width':self.width,
                     'height':self.height,
                     'src':self.src,
                    }
                    
    class Metatags(object):
        def __init__(self, data):
            self.has_data = False
            if not data: return
            self.has_data = True
            self.og_site_name = data.get("og:site_name")
            self.og_type = data.get("og:type")
            self.fb_app_id = data.get("fb:app_id")
            self.og_title = data.get("og:title")
            self.og_image = data.get("og:image")
            self.og_url = data.get("og:url")
            
        def to_json(self):
            if not self.has_data:
                return { 'has_data':False }
            return { 'has_data':True,
                     'og:site_name':self.og_site_name,
                     'og:type':self.og_type,
                     'fb:app_id':self.fb_app_id,
                     'og:title':self.og_title,
                     'og:image':self.og_image,
                     'og:url':self.og_url,
                    }
        
    class PageMap(object):
        def __init__(self, data):
                
            self.cse_image = []
            self.cse_thumbnail = []
            self.metatags = []
 
            if data.get("cse_image"): 
                for cse_image in data.get("cse_image"):
                    self.cse_image.append(GoogleSearchEngine.CseImage(cse_image))
                    
            if data.get("cse_thumbnail"):
                for cse_thumbnail in data.get("cse_thumbnail"):
                    self.cse_thumbnail.append(GoogleSearchEngine.CseThumbnail(cse_thumbnail))
            
            if data.get("metatags"):
                for metatag in data.get("metatags"):
                    self.metatags.append(GoogleSearchEngine.Metatags(metatag))
                    
        def to_json(self):
            return {
                    "cse_image": [cse_image.to_json() for cse_image in self.cse_image],
                    "cse_thumbnail": [cse_thumbnail.to_json() for cse_thumbnail in self.cse_thumbnail],
                    "metatags": [metatags.to_json() for metatags in self.metatags],
                   }
            
    class Item(object):
        
        def __init__(self, data):
            self.kind = data.get("kind")
            self.title = data.get("title")
            self.htmlTitle = data.get("htmlTitle")
            self.link = data.get("link")
            self.displayLink = data.get("displayLink")
            self.snippet = data.get("snippet")
            self.htmlSnippet = data.get("htmlSnippet")
            self.cacheId = data.get("cacheId")
            
            self.formattedUrl = data.get("formattedUrl")
            self.htmlFormattedUrl = data.get("htmlFormattedUrl")
            
            self.pagemap = None
            if data.get("pagemap"):
                try:
                    self.pagemap = GoogleSearchEngine.PageMap(data.get("pagemap"))
                except Exception as ex:
                    app_download_logger.error(u"GoogleSearchEngine.PageMap: %s" % ex)
                    

        def to_json(self):
            return {'kind': self.kind,
                    'title': self.title,
                    'htmlTitle': self.htmlTitle,
                    'link': self.link,
                    'displayLink': self.displayLink,
                    'snippet': self.snippet,
                    'htmlSnippet': self.htmlSnippet,
                    'cacheId': self.cacheId,
                    
                    'formattedUrl': self.formattedUrl,
                    'htmlFormattedUrl': self.htmlFormattedUrl,
                    'pagemap': self.pagemap.to_json() if self.pagemap else None ,
                    }
            
        @staticmethod
        def from_json(data):
            return GoogleSearchEngine.Item(data)

        """
        Output string. Change this if necessary !!!!!!!!!!!!!!!!
        """                    
        def __repr__(self):
            
            return u"%s ||| %s" % (self.link, self.title)
    
    
