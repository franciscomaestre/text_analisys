#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class UniqueMetaDescriptionRating(object):
    RATING_NAME = u'UNIQUE-METADESCRIPTION'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if not score:
            message = u'Tienes MetaDescripciones repetidas'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Tus MetaDescripciones son únicas'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      UniqueMetaDescriptionRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        metaDs = [seoDocument.dataDocument.meta for seoDocument in self.seoLibrary.seoDocuments]
        return len(set(metaDs)) > 0.9*len(metaDs)
