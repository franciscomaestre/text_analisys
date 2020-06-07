#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code
from data_mining.seo_document_downloader import SeoDocumentDownloader
from config import settings

class RichSnippetsRating(object):
    RATING_NAME = u'RICHSNIPPETS'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if not score:
            message = u'No utilizas Rich Snippets'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Usas Rich Snippets'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      RichSnippetsRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        for seoDocument in self.seoLibrary.seoDocuments:
            rawHtml = seoDocument.dataDocument.rawHtml
            regex = r"itemscope|itemprop"
            matches = re.findall(regex, rawHtml)
            if matches:
                return True
        return False



if __name__ == '__main__':
    
    query = 'site:dinersclub.com.ec'
    language = 'es'
    country = 'ES'

    seoLibrary = SeoDocumentDownloader(
                                               query=query,
                                               language=language,
                                               country=country,
                                               searchEngine=settings.DOWNLOADER_SEARCH_ENGINE,
                                               downloadLimit=100,
                                               sameOrigin=False
                                               ).getSeoLibrary()
                                               
    rating = RichSnippetsRating(seoLibrary)
    
    print(rating.getRating().getInfo())                                       
    