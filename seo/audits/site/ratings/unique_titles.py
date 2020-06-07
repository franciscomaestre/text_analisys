#!/usr/bin/python
# -*- coding: utf-8 -*-
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class UniqueTitlesRating(object):
    RATING_NAME = u'UNIQUE-TITLES'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if not score:
            message = u'Tienes títulos repetidos'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Tus títulos son únicos'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      UniqueTitlesRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        titles = [seoDocument.dataDocument.title for seoDocument in self.seoLibrary.seoDocuments]
        return len(set(titles)) > 0.9*len(titles)
