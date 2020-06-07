#!/usr/bin/python
# -*- coding: utf-8 -*-
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code
from data_mining.geolocation_tool import GeoLocationTool

class GeolocationRating(object):
    RATING_NAME = u'GEOLOCATION'
    
    def __init__(self, siteDomain, country):
        self.siteDomain = siteDomain
        self.country = country
        
    def getRating(self):
        score = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if not score:
            message = u'A Google no le gusta que un dominio se quiera posicionar para un pais con una Ip de otro pais'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'La IP de tu web pertenece al país en el que te quieres posicionar'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      GeolocationRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        return GeoLocationTool().getHostnameCountryIsoCode(self.siteDomain) == self.country


   