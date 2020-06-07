#!/usr/bin/python
# -*- coding: utf-8 -*-

#import requests
import urllib2
import tldextract
from urlparse import urlparse

from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code



class DomainRedirectRating(object):
    RATING_NAME = u'DOMAIN-REDIRECT'
    
    def __init__(self, siteUrl):
        self.siteUrl = siteUrl
        
    def getRating(self):
        
        try:
            score = self._getScore()

            # message
            if not score:
                message = u'No tienes redireccion entre la version WWW y sin WWW'
                level = Level.DANGER
                code = Code.IMPROVE
            else:
                message = u'Tu dominio redirecciona correctamente entre la version WWW y sin WWW'
                level = Level.SUCCESS
                code = Code.OK
        except:
            score = 0
            message = u'Error al comprobar la redirección entre la version WWW y sin WWW'
            level = Level.DANGER
            code = Code.UNDEFINED
        
                
        return SiteAuditRating(
                      DomainRedirectRating.RATING_NAME, 
                      score*100,
                      code,
                      level,
                      links=[],
                      domainRating=True,
                      message=message
                      )        
    
    def _getScore(self):
        extracted = tldextract.extract(self.siteUrl)
        parsedUrl = urlparse(self.siteUrl)
        
        siteWithWWW = u'%s://www.%s.%s' % (parsedUrl.scheme, extracted.domain, extracted.suffix)
        siteWithoutWWW = u'%s://%s.%s' % (parsedUrl.scheme, extracted.domain, extracted.suffix)
               
        """       
        requestWWW = requests.get(siteWithWWW, allow_redirects=False)
        requestNonWWW = requests.get(siteWithoutWWW, allow_redirects=False)
        
        # error 
        if requestWWW.status_code not in [200, 301] or requestNonWWW.status_code not in [200, 301]:
            raise Exception(u"Error als comprobar redirección")
        
        ## www --> no www
        if requestWWW.status_code == 301:
            redirectToUrl = requestWWW.headers['location']
            return redirectToUrl.strip('/') == siteWithoutWWW
        elif requestNonWWW.status_code == 301:
            redirectToUrl = requestWWW.headers['location']
            return redirectToUrl.strip('/') == siteWithWWW
        
        return False
        """
        
        requestWWW = urllib2.urlopen(siteWithWWW)
        requestNonWWW = urllib2.urlopen(siteWithoutWWW)

        return unicode(requestWWW.geturl().strip('/')) == unicode(requestNonWWW.geturl().strip('/'))
