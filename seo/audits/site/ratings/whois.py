#!/usr/bin/python
# -*- coding: utf-8 -*-
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code
from utils.whois_domain import WhoisDomain

class WhoisRating(object):
    RATING_NAME = u'WHOIS'
    
    def __init__(self, siteDomain):
        self.siteDomain = siteDomain
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if score == -1:
            message = u'No hemos podido comprobar la antiguedad de tu dominio'
            level = Level.DANGER
            code = Code.UNDEFINED
        elif score < 2:
            message = u'A Google no le gusta que un dominio tenga un tiempo de vida inferior a 2 años. Debes aumentar la fecha de caducidad'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'La antiguedad de tu dominio es suficiente'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      WhoisRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        return WhoisDomain(self.siteDomain).getDomainAge()

    