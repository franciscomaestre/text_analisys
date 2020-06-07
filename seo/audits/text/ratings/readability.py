#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from core.seo.containers.ratings import TextAuditRating
from utils.median_distribution import getMedianDistributionInfo
from core.seo.audits.text.readability_text import ReadabilityText

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class ReadabilityRating(object):
    
    RATING_NAME = u'READABILITY-SCORE'
    
    def __init__(self, textSeoDocument, bestSeoDocuments):
        self.textSeoDocument = textSeoDocument
        self.bestSeoDocuments = bestSeoDocuments
        
    def getRating(self):
        readabilityScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        interval = 100.00 - lowerLimitScore
        
        if readabilityScore < lowerLimitScore:
            message = _(u'Tu texto es demasiado confuso')
            level = Level.DANGER
            code = Code.IMPROVE
        elif readabilityScore < lowerLimitScore + interval * 0.85:
            message = _(u'Tu texto es normal, se entiende bien')
            level = Level.ACCEPTABLE
            code = Code.OK
        else:
            message = _(u'Tu texto es fácil de comprender')
            level = Level.SUCCESS
            code = Code.OK
        
        return TextAuditRating(
                      ReadabilityRating.RATING_NAME, 
                      readabilityScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )
    
    def _getScore(self):
        result = []
        
        for seoDocument in self.bestSeoDocuments:
            result.append(self._getDocumentScore(seoDocument))
        
        lowerLimit, _median, upperLimit = getMedianDistributionInfo(result)
        
        self.lowerLimit =  int(max(0,lowerLimit))
        self.rawScore = int(self._getDocumentScore(self.textSeoDocument))
        self.upperLimit = int(upperLimit)
        
        readabilityScore = self._getDocumentScore(self.textSeoDocument) * 100.00 / (upperLimit)
        readabilityScore = int(readabilityScore * 100) / 100.0
        
        lowerLimitScore = max(0, 100 * (lowerLimit) / (upperLimit))
        
        return readabilityScore, lowerLimitScore
        
    
    def _getDocumentScore(self, textSeoDocument):
        readabilityText = ReadabilityText(textSeoDocument.getLanguage())
        sentences = textSeoDocument.getSentences()
        completeText = u' . '.join(sentences)
        scoreText = readabilityText.textReadabilityScore(completeText) 
        scoreText = max(0, min(100, scoreText))
        
        return scoreText


    







