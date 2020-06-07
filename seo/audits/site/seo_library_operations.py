#!/usr/bin/python
# -*- coding: utf-8 -*-

def _getSeoLibraryExtended(sentences, seoLibrary, useProxy=False):
    from data_mining.seo_document_downloader import SeoDocumentDownloader
    from config import settings
    
    seoDocuments = []
    for sentence in sentences:
        try:
            seoDocuments.extend( SeoDocumentDownloader(
                                           query=sentence,
                                           language=seoLibrary.language,
                                           country=seoLibrary.country,
                                           searchEngine=settings.DOWNLOADER_SEARCH_ENGINE,
                                           downloadLimit=15,
                                           sameOrigin=False,
                                           useProxy=useProxy
                                           ).getSeoDocuments()
                            )
        except:
            continue
    
    seoDocuments.extend(seoLibrary.seoDocuments)
    seoDocumentsDict = {seoDocument.link:seoDocument for seoDocument in seoDocuments}
        
    from seo.containers.seo_library import SeoLibrary    
    seoLibraryExtended = SeoLibrary(seoLibrary.query+u' extended', seoLibrary.language, seoLibrary.country)
    seoLibraryExtended.seoDocuments = seoDocumentsDict.values()
    
    return seoLibraryExtended

def _getSeoLibraryFiltered(startUrl, language, country, useProxy=False):
    
    import tldextract
    from data_mining.seo_document_downloader import SeoDocumentDownloader
    from config import settings

    '''
    Montamos la query y descargamos los documentos
    '''
    
    extracted = tldextract.extract(startUrl)
    domain = u'%s.%s' % (extracted.subdomain, extracted.domain) if extracted.subdomain else extracted.domain
    domain = u'%s.%s' % (domain, extracted.suffix)

    # buscamos si hay un path después del dominio
    import urlparse
    urlpath = [u for u in  urlparse.urlsplit(startUrl).path.split('/') if u and u!=domain ]
    path=[]
    if urlpath:
        for index, subpath in enumerate(urlpath):
            if subpath:
                if index<len(urlpath)-1 or not u'.' in subpath:
                    path.append(subpath)
    if path:
        query = u'site:{}/{}'.format(domain, '/'.join(path))
    else:
        query = u'site:{}'.format(domain,)
    
    print query
    
    seoLibrary = SeoDocumentDownloader(
                                       query=query,
                                       language=language,
                                       country=country,
                                       searchEngine=settings.DOWNLOADER_SEARCH_ENGINE,
                                       downloadLimit=settings.SITE_AUDIT_DOWNLOAD_LIMIT,
                                       sameOrigin=True,
                                       useProxy=useProxy
                                       ).getSeoLibrary()    
    
    print u'Número de documentos originales: %s' % (len(seoLibrary.seoDocuments))

    if len(seoLibrary.seoDocuments) < 20:
        raise Exception(u'Error: Not enough documents to get stats')
    
    '''
    Eliminamos aquellos enlaces que son considerados paginaciones
    '''
    
    DIFFERENCE_LIMIT = 6
    
    paginator = {}
    links2Remove = []
    
    import re
    for seoDocument in seoLibrary.seoDocuments:
        applied = re.sub(u'\d', u'', seoDocument.link)
        difference = len(seoDocument.link) - len(applied)
        if difference != 0 and difference <= DIFFERENCE_LIMIT:
            if applied not in paginator:
                paginator[applied] = []
            paginator[applied].append(seoDocument.link)
    
    for _shortUrl, origins in paginator.items():
        if len(origins) > 1:
            links2Remove.extend(origins)
            #print u'-'*15
            #print u'%s' % _shortUrl
            #for origin in origins:
            #    print u'\t\t%s' % origin
    
    seoLibrary.seoDocuments = [seoDocument for seoDocument in seoLibrary.seoDocuments if seoDocument.link not in links2Remove]
    
    print u'Número de documentos tras Filtrado de Paginaciones: %s' % (len(seoLibrary.seoDocuments))
    
    '''
    Descartamos aquellos documentos que no tengan una longitud mínima
    '''
    
    import numpy as np
    lengths = [seoDocument.getLenRawTokens() for seoDocument in seoLibrary.seoDocuments]
    percentilLengthText = np.percentile(lengths, 25)
    lowerLimit = max(percentilLengthText, settings.SITE_AUDIT_MIN_DOCUMENT_LENGTH)
    seoLibrary.seoDocuments = [seoDocument for seoDocument in seoLibrary.seoDocuments if seoDocument.getLenRawTokens() > lowerLimit]
    
    print u'Número de documentos tras PRIMER filtrado por Longitud: %s' % (len(seoLibrary.seoDocuments))
    
    allSentences = {}
    
    for seoDocument in seoLibrary.seoDocuments:
        sentences = seoDocument.getSentences()
        for sentence in sentences:
            if sentence not in allSentences:
                allSentences[sentence] = 0
            allSentences[sentence] += 1
    
    
    for seoDocument in seoLibrary.seoDocuments:
        sentences = seoDocument.getSentences()
        sentencesFiltered = []
        for sentence in sentences:
            if allSentences[sentence] < 2:
                sentencesFiltered.append(sentence)
                
        seoDocument.dataDocument.text = u' . '.join(sentencesFiltered)
        seoDocument.resetPreloads()
    
    
    lengths = [seoDocument.getLenRawTokens() for seoDocument in seoLibrary.seoDocuments]
    lowerLimit = np.percentile(lengths, 25)
    seoLibrary.seoDocuments = [seoDocument for seoDocument in seoLibrary.seoDocuments if seoDocument.getLenRawTokens() > lowerLimit]
    
    print u'Número de documentos tras SEGUNDO filtrado por Longitud: %s' % (len(seoLibrary.seoDocuments))

    return seoLibrary

