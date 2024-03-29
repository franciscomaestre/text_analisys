#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class TwitterRating(object):
    RATING_NAME = u'TWITTER'
    
    def __init__(self, seoDocument):
        self.seoDocument = seoDocument
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if not score:
            message = u'Tu dominio no está preparado para compartir enlaces en Twitter'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Tu dominio está preparado para compartir enlaces en Twitter'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      TwitterRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        rawHtml = self.seoDocument.dataDocument.rawHtml
        regexList = [r"twitter:card"]
        for regex in regexList:
            matches = re.findall(regex, rawHtml)
            if not matches:
                return False
        return True
