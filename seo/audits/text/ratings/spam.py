#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from config import settings
from utils.code import Code
from core.seo.containers.ratings import TextAuditRating
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class SpamScore(object):
    
    RATING_NAME = u'SPAM-SCORE'
    
    def __init__(self, textSeoDocument, bestSeoDocuments):
        self.textSeoDocument = textSeoDocument
        self.bestSeoDocuments = bestSeoDocuments
    
    def getRating(self):
        spamScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # interval = 100.00 - lowerLimitScore
        
        if spamScore < lowerLimitScore:
            message = _(u'Tu texto repite demasiadas veces los mismos términos')
            level = Level.DANGER
            code = Code.OVERREPETITION
        else:
            message = _(u'Tienes suficiente diversidad de términos')
            level = Level.SUCCESS
            code = Code.OK
        
        return TextAuditRating(
                      SpamScore.RATING_NAME, 
                      spamScore,
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
            if seoDocument.getLenRawTokens() > settings.DOCUMENT_MIN_CHARACTERS:
                lenTokensUnicos = len(set(seoDocument.getTextTokens(lemmatize=True)))
                density = lenTokensUnicos * 1.0 / seoDocument.getLenRawTokens()
                if DISPLAY:
                    app_logger.info(u'Density %s' % density)
                result.append(density)
        
        lowerLimit, median, upperLimit = getMedianDistributionInfo(result)
    
        lenTokensUnicos = len(set(self.textSeoDocument.getTextTokens(lemmatize=True)))
        score = lenTokensUnicos * 1.0 / self.textSeoDocument.getLenRawTokens()
        spamScore = min(100, score * 100 / (upperLimit))
        spamScore = int(spamScore * 100) / 100.0
        
        lowerLimitScore = max(0, (lowerLimit) * 100.0 / (upperLimit))

        self.lowerLimit =  int(max(0,lowerLimit))
        self.rawScore = int(score)
        self.upperLimit = int(upperLimit)
        
        if DISPLAY:
            app_logger.info(u'Text Density %s' % score)
            app_logger.info(u'Media Density %s' % median)
    
        return spamScore, lowerLimitScore




