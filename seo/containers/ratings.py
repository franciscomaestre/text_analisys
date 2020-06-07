#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.logger import LoggerFactory

app_logger = LoggerFactory.getInstance('app')  

def _addRating(ratingGetter, ratings):
    try:
        ratingList = ratingGetter.getRating()
        
        if not isinstance(ratingList, list):
            ratingList = [ratingList]
            
        for rating in ratingList:
            ratings[rating.title] = rating.getInfo()
            
    except Exception as ex:
        print(u"%s %s" % (ratingGetter.__class__ ,ex))
        app_logger.error(u"%s %s" % (ratingGetter.__class__ ,ex))


class Rating(object):
    
    def __init__(self, title, score, code, level, message = u''):
        self.title = title
        self.score = score
        self.code = code
        self.level = level
        self.message = message
        
    def getInfo(self):
        return self.__dict__


class TextAuditRating(Rating):
    
    def __init__(self, title, score, code, level, rawScore, lowerLimit, upperLimit, message = u''):
        super(TextAuditRating, self).__init__(title, score, code, level, message)
        self.rawScore = rawScore
        self.lowerLimit = max(1, lowerLimit)
        self.upperLimit = upperLimit
        

class SiteAuditRating(Rating):
    
    def __init__(self, title, score, code, level, links = [], domainRating = True, message = u''):
        super(SiteAuditRating, self).__init__(title, score, code, level, message)
        self.links = links
        self.domainRating = domainRating

    
    