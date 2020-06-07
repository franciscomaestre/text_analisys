#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class GooglePageSpeedRating(object):
    RATING_NAME = u'PAGE-SPEED-%s'
    
    def __init__(self, googleTestSpeed, mobile = False):
        self.googleTestSpeed = googleTestSpeed
        self.mobile = mobile
        self.name = GooglePageSpeedRating.RATING_NAME % (u'MOBILE' if mobile else u'DESKTOP')
        
    def getRating(self):
        try:
            score = self._getScore()
        except:
            score = -1
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if score == -1:
            message = u'No hemos podido realizar el Google Speed Test'
            level = Level.DANGER
            code = Code.UNDEFINED
        elif score < 50:
            message = u'Tienes varios problemas con el Google Speed Test'
            level = Level.DANGER
            code = Code.IMPROVE
        elif score < 80:
            message = u'Tu web tiene algunos problemas con el Google Speed Test'
            level = Level.WARNING
            code = Code.IMPROVE
        else:
            message = u'Tu web cumple los requisitos del Google Speed Test'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      self.name, 
                      score,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        if self.mobile:
            return self.googleTestSpeed['mobileResult']['pageSpeedScore']
        else:
            return self.googleTestSpeed['desktopResult']['pageSpeedScore']

   