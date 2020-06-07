#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code
from utils.https_protocol_checker import HttpsProtocolChecker,\
    HttpsProtocolResponses

class HttpsRating(object):
    RATING_NAME = u'HTTPS'
    
    def __init__(self, siteDomain):
        self.siteDomain = siteDomain
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if score == HttpsProtocolResponses.NOT_AVAILABLE:
            message = u'Google confía más en aquellos dominios que tienen certificado SSL instalado'
            level = Level.DANGER
            code = Code.IMPROVE
        elif score == HttpsProtocolResponses.ERROR:
            message = u'Problemas con la verificación del certificado SSL'
            level = Level.DANGER
            code = Code.FIX
        else:
            message = u'Tu certificado SSL es válido'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      HttpsRating.RATING_NAME, 
                      100 if score == HttpsProtocolResponses.AVAILABLE else 0,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        return HttpsProtocolChecker(self.siteDomain).isHttpsActive()


   