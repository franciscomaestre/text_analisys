#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class Html5Rating(object):
    RATING_NAME = u'HTML5'
    
    def __init__(self, seoDocument):
        self.seoDocument = seoDocument
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if not score:
            message = u'Tu web no utiliza el estándar de Html5'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Tu web usa el estándar de Html5'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      Html5Rating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        return bool(re.match(r'^<!doctype html>', self.seoDocument.dataDocument.rawHtml, re.I))


   