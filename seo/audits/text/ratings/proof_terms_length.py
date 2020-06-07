#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from config import settings
from core.seo.containers.ratings import TextAuditRating
from utils.code import Code
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class ProofTermsLengthRating(object):
    
    RATING_NAME = u'PROOFTERMS-LENGTH-SCORE'
    
    def __init__(self, textSeoDocument, bestSeoDocuments):
        self.textSeoDocument = textSeoDocument
        self.bestSeoDocuments = bestSeoDocuments
    
    def getRating(self):
        
        proofTermsLengthScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if proofTermsLengthScore < lowerLimitScore:
            message = _(u'La longitud del texto es insuficiente')
            level = Level.DANGER
            code = Code.SHORT
        else:
            message = _(u'Tu texto es suficientemente largo')
            level = Level.SUCCESS
            code = Code.OK
        
        return TextAuditRating(
                      ProofTermsLengthRating.RATING_NAME, 
                      proofTermsLengthScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )

    def _getScore(self, documentMinWords=settings.DOCUMENT_MIN_CHARACTERS):
        result = []
        
        # bestDocuments = sorted(bestSeoDocuments.items(), key=operator.attrgetter('getLenRawTokens'), reverse=True)[0:]
        
        for seoDocument in self.bestSeoDocuments:
            if seoDocument.getLenRawTokens() > documentMinWords:
                if DISPLAY:
                    app_logger.info(u'Numero tokens %s' % seoDocument.getLenRawTokens())
                result.append(max(0.0, seoDocument.getLenRawTokens() * 1.0 - len(seoDocument.getTitleTokens())))
        
        lowerLimit, median, upperLimit = getMedianDistributionInfo(result)
        
        self.lowerLimit = int(max(0,lowerLimit))
        self.rawScore = max(0, int(self.textSeoDocument.getLenRawTokens()) - len(self.textSeoDocument.getTitleTokens()))
        self.upperLimit = int(upperLimit)
        
        proofTermsLengthScore = self.textSeoDocument.getLenRawTokens() * 100.00 / (upperLimit)
        proofTermsLengthScore = int(proofTermsLengthScore * 100) / 100.0
        
        lowerLimitScore = max(0, 100 * (lowerLimit) / (upperLimit))
        
        if DISPLAY:
            app_logger.info(u'Median Length %s' % median)
            app_logger.info(u'Lower Limit %s' % lowerLimitScore)
            app_logger.info(u'Score Final Length %s' % proofTermsLengthScore)
        
        return proofTermsLengthScore, lowerLimitScore
    
    




