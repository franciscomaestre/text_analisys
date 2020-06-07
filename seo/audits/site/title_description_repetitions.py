#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import Counter

def getRepeatedTitlesAndMetaDescriptions(seoLibrary):
    
    titles = []
    descriptions = []
    titles_link = {}       # reverse search
    descriptions_link = {}
    
    for seoDocument in seoLibrary.seoDocuments:
        
        title = seoDocument.dataDocument.title
        meta_description = seoDocument.dataDocument.meta
        
        if not title in titles_link:
            titles_link[title] = []
        titles_link[title].append(seoDocument.link)
        
        if not meta_description in descriptions_link:
            descriptions_link[meta_description] = []
        descriptions_link[meta_description].append(seoDocument.link)
        
        titles.append(title)
        descriptions.append(meta_description)

    titles = Counter(titles)    
    descriptions = Counter(descriptions)    
    
    '''
    Una vez que tenemos la freq de cada titulo y cada descripción, nos quedamos con aquellos con freq > 1 y los ordenamos
    por número de apariciones
    '''
    
    # filter
    #   link
    #   title/description
    #   absolute frecuency 
    
    titles = [{'title':t, 'links': titles_link[t]} for t, frec in titles.items() if frec > 1 and t]
    titles.sort(key=lambda t: len(t['links']), reverse=True)
    descriptions = [{'description':d, 'links': descriptions_link[d]} for d, frec in descriptions.items() if frec > 1 and d]
    descriptions.sort(key=lambda d: len(d['links']), reverse=True)
    
    return titles, descriptions
    
if __name__ == '__main__':
    import tldextract
    import json
    from data_mining.seo_document_downloader import SeoDocumentDownloader
    from config import settings
    
    language = u'es'
    country = u'ES'
    startUrl = u'http://www.luciasecasa.com'
    
    extracted = tldextract.extract(startUrl)
    domain = u'%s.%s' % (extracted.subdomain, extracted.domain) if extracted.subdomain else extracted.domain
    query = u'site:{}.{}'.format(domain, extracted.suffix)
    
    print query
    
    seoLibrary = SeoDocumentDownloader(
                                       query=query,
                                       language=language,
                                       country=country,
                                       searchEngine=settings.DOWNLOADER_SEARCH_ENGINE,
                                       downloadLimit=400,
                                       sameOrigin=True
                                       ).getSeoLibrary()    
    

    print json.dumps(getRepeatedTitlesAndMetaDescriptions(seoLibrary))
