#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from collections import OrderedDict

from seo.audits.site.google_ranking.domain_google_ranking import DomainGoogleRankingInfo,\
    GoogleRankedUrl
from data_mining.search_engines.google.google_scraper import GoogleScraper
from data_mining.search_engines.google import getGoogleHost

MAX_COMPETENCE_URLS = 10

def getDomainRanking(siteDomain, seoLibrary, queries):
    from nltk.probability import FreqDist
    
    queriesRankingInfo = {}
    domainList = []
    '''
    Recopilamos la información para cada Query
    '''
    
    for query in queries:
        try:
            queriesRankingInfo[query] = getQueryRanking(query, seoLibrary.language, seoLibrary.country)
            domainList.extend(queriesRankingInfo[query].keys())
        except Exception as ex:
            print(ex)
            continue
    
    domainFreq = FreqDist(domainList)
    
    #lowerLimit = domainFreq[siteDomain]
    import numpy as np
    lowerLimit = np.percentile(domainFreq.values(), 25)
        
    '''
    Unificamos los resultados por dominio
    '''
    
    domainsInfo = {}
    
    for domain in domainFreq.keys():
        if domainFreq[domain] >= lowerLimit or domain==siteDomain:
            appearIn = {}
            notAppearIn = []
            for query, data in queriesRankingInfo.items():
                if domain in data:
                    appearIn[query] = data[domain]
                else:
                    notAppearIn.append(query)
                
            domainsInfo[domain] = DomainGoogleRankingInfo(domain, appearIn, notAppearIn)
            
    #Analisis del sitio a partir de las queries. Si no está .. malo
    # puede que pasemos sin www y se redirija a www
    try:
        siteDomainInfo = domainsInfo[siteDomain]
    except:
        # ponemos o quitamos www
        p = urlparse.urlparse(siteDomain)
        netloc = p.netloc or p.path
                
        if not netloc.startswith('www.'):
            siteDomain = 'www.' + netloc
        else:
            siteDomain = netloc[4:]
        siteDomainInfo = domainsInfo[siteDomain]
    
    #Competencia detectada en las queries analizadas
    del domainsInfo[siteDomain]
    domainCompetence = domainsInfo.values()
    
    #mas apariciones
    ##domainCompetence.sort(key=lambda x: x.avgPos, reverse=False)
    domainCompetence.sort(key=lambda x: len(x.appearIn), reverse=True)
    domainCompetence = domainCompetence[:MAX_COMPETENCE_URLS]
    domainCompetence.sort(key=lambda x: x.avgPos, reverse=False) # por posicion
    
    return siteDomainInfo, domainCompetence

def getDomainCompetence(siteDomain, language, country):
    
    query = u'related:%s' % siteDomain
    
    googleScrapper = GoogleScraper(query=query,
                                         language=language,
                                         country=country,
                                         googleHost=getGoogleHost(country),
                                         max_results=20)
    links = googleScrapper.search()
    
    #results = list(set([getDomainFromUrl(link) for link in links]))
    results = OrderedDict([(getDomainFromUrl(link),0) for link in links]).keys()
    
    return results[:MAX_COMPETENCE_URLS]
    

def getDomainFromUrl(url):
    import tldextract
    extracted = tldextract.extract(url)
    domain =  u'%s.%s' % (extracted.subdomain, extracted.domain) if extracted.subdomain else extracted.domain
    return domain + u'.%s' % extracted.suffix

def getQueryRanking(query, language, country):
    googleScrapper = GoogleScraper(query=query,
                                         language=language,
                                         country=country,
                                         googleHost=getGoogleHost(country),
                                         max_results=150)
    
    #Descargamos hasta 150 para dejarlos cacheados ya que luego los vamos a usar en la parte del text audit, pero solo nos quedamos con 50
    links = googleScrapper.search()[0:50]
    
    results = {}
    
    for order, link in enumerate(links):
        domain = getDomainFromUrl(link)
        if domain not in results:
            results[domain] = GoogleRankedUrl(link, order+1)
    
    return results    
    