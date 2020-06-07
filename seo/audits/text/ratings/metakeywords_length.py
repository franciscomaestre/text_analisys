#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class MetaKeyWordsLengthRating(object):
    
    RATING_NAME = u'METAKEYWORDS-LENGTH-SCORE'
    
    def __init__(self, textSeoDocument, bestSeoDocuments):
        self.textSeoDocument = textSeoDocument
        self.bestSeoDocuments = bestSeoDocuments
        
    def getRating(self):
        metaKeyWordsScore, _lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if metaKeyWordsScore > 100.00:
            message = _(u'Demasiados Metakeywords. Reduce la lista o quítala directamente')
            level = Level.DANGER
            code = Code.LONG
        else:
            message = _(u'Tus metakeywords tienen una longitud aceptable.')
            level = Level.SUCCESS
            code = Code.OK
            
        return TextAuditRating(
                      MetaKeyWordsLengthRating.RATING_NAME, 
                      metaKeyWordsScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )
    
    def _getScore(self):
        result = []
        counter = 0
        for seoDocument in self.bestSeoDocuments:
            lenMetaKeyWords = len(seoDocument.getMetaKeywordsTokens(unique=False))
            if lenMetaKeyWords > 0:
                counter += 1
                result.append(lenMetaKeyWords * 1.0)
        
        lowerLimit, _median, upperLimit = getMedianDistributionInfo(result)
        
        self.lowerLimit =  0
        self.rawScore = int(len(self.textSeoDocument.getMetaKeywordsTokens(unique=False)))
        self.upperLimit = int(upperLimit)
        
        metaKeyWordsScore =  self.rawScore * 100.00 / (upperLimit)
        metaKeyWordsScore = int(metaKeyWordsScore * 100) / 100.0
        
        lowerLimitScore = max(0, 100 * (lowerLimit) / (upperLimit))
        
        return metaKeyWordsScore, lowerLimitScore






