
import os
import sys
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')

import urllib
from urllib.parse import urlparse


from data_mining.search_engines.google.google_scraper import GoogleScraper
from data_mining.search_engines.google import getGoogleHost
from seo.audits.site.google_ranking import getDomainFromUrl
from data_mining.web_pages.scraper import Scraper
from bs4 import BeautifulSoup


if __name__ == '__main__':
    
    siteDomain = u'http://www.dinersclub.com.ec'
    language = u'es'
    country = u'ES'
    max_results = 600
    
    query = u'site:%s' % getDomainFromUrl(siteDomain)
    googleScrapper = GoogleScraper(query=query, language=language, country=country, googleHost=getGoogleHost(country), max_results=max_results)
    internalLinks = googleScrapper.search()
    
    queries = []
    queriesTemplates = [u'%s', u'link:%s', u'"%s"', u'"* %s"']
    
    for qTemplate in queriesTemplates:
        queries.append(qTemplate % getDomainFromUrl(siteDomain))
    
    for link in internalLinks:
        try:
            scraper = Scraper(link)
            dataDocument = scraper.getDataDocument()
        except:
            for qTemplate in queriesTemplates:
                queries.append(qTemplate % link)
    
    
    backLinks = []
    
    for query in queries:
        query = u'%s' % getDomainFromUrl(siteDomain)
        googleScrapper = GoogleScraper(query=query, language=language, country=country, googleHost=getGoogleHost(country), max_results=max_results)
        backLinks.extend(googleScrapper.search())
        
    backLinks = list(set(backLinks))
    
    results = {}
    
    for origin in backLinks:
        
        if getDomainFromUrl(siteDomain) != getDomainFromUrl(origin):
        
            try:
            
                scraper = Scraper(origin)
                dataDocument = scraper.getDataDocument()
                soup = BeautifulSoup(dataDocument.rawHtml, 'lxml')
                aTags = soup.findAll('a')
                
                if aTags:
                
                    for aTag in aTags:
                    
                        url = aTag['href'].strip().lower().replace('ext://','http://')
                        p = urlparse.urlparse(url)
                        if not p.scheme:
                            url = 'http://' + url
                        
                        if getDomainFromUrl(siteDomain).strip().lower() == getDomainFromUrl(url).strip().lower():
                            if u'%' in url:
                                url =  urllib.unquote(url)
                            if origin not in results:
                                results[origin] = []
                            results[origin].append(url.replace('&quot;',''))
            
            except Exception as ex:
                continue
    
    for origin, links in results.items():
        for link in links:
            try:
                scraper = Scraper(link)
                dataDocument = scraper.getDataDocument()
                #print u'URL ORIGEN: %s OK' % origin    
            except:
                print(u'URL ORIGEN: %s \nENLACE ROTO:  %s\n' % (origin, link))
    
