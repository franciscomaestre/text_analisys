#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class HTagsRating(object):
    RATING_NAME = u'HTAGS'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score, badLinks = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if not score:
            message = u'Algunos documentos de tu web tienen mal la jerarquía de H\'s'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'La jerarquía de tags H es correcta'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      HTagsRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=badLinks,
                      domainRating=False,
                      message=message
                      )        
    
    def _getScore(self):
        errors = []
    
        for seoDocument in self.seoLibrary.seoDocuments:
            rawHtml = seoDocument.dataDocument.rawHtml
            regex = r"<h([1-6])"
            matches = re.findall(regex, rawHtml)
            if matches:
                maxNumber = matches[0]
                if maxNumber > min(matches):
                    errors.append(seoDocument.link)
        
        return len(errors) == 0, errors


   