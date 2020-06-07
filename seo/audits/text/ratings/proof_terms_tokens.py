#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from seo.containers.ratings import TextAuditRating
from utils.code import Code
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')


class ProofTermsTokensRating(object):
    
    RATING_NAME = u'PROOFTERMS-TOKENS-SCORE'
    
    def __init__(self, rankedDataTokens, textLemmas, referencedLemmas):
        self.rankedDataTokens = rankedDataTokens
        self.textLemmas = list(set(textLemmas))
        self.referencedLemmas = referencedLemmas
        
    def getRating(self):
        
        proofTermsScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        interval = 100.00 - lowerLimitScore
        
        if proofTermsScore < lowerLimitScore:
            message = _(u'Este texto no tiene los terminos necesarios para posicionarse en esta Query')
            level = Level.DANGER
            code = Code.ADD
        elif proofTermsScore < lowerLimitScore + interval:
            message = _(u'El contenido semántico de tu texto es óptimo para esta Query')
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'Estás abusando de las palabras más utilizadas para esta Query. Para que Google considere que un texto versa sobre una temática, no es necesario que pongas todas las palabras que se te ocurran')
            level = Level.DANGER
            code = Code.OVERUSED
        
        return TextAuditRating(
                      ProofTermsTokensRating.RATING_NAME, 
                      proofTermsScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )
    
    def _getScore(self):
        results = []
        
        if DISPLAY:
            print 'Ranked vs WebData'
        proofTermsScore = self._stadistic(self.rankedDataTokens, self.textLemmas)
        for dataTokens in self.referencedLemmas:
            if DISPLAY:
                # print '-'*20
                # print 'Ranked vs BestData'
                app_logger.info('-' * 20)
                app_logger.info('Ranked vs BestData')
            results.append(self._stadistic(self.rankedDataTokens, dataTokens))
        
        lowerLimit, median, upperLimit = getMedianDistributionInfo(results)
        
        self.lowerLimit =  int(max(0,lowerLimit))
        self.rawScore = int(proofTermsScore)
        self.upperLimit = int(upperLimit)
        
        if DISPLAY:
            app_logger.info(u'Mediana %s' % median)
            app_logger.info(u'LowerLimit %s' % lowerLimit)
        
        proofTermsScore = (proofTermsScore) * 100 / (upperLimit)
        proofTermsScore = int(proofTermsScore * 100) / 100.0
        
        lowerLimitScore = max(0, (lowerLimit) * 100.0 / (upperLimit))
        
        return proofTermsScore, lowerLimitScore
    
    def _stadistic(self, data, data2Compare):
        
        commonTerms = (set(data) & set(data2Compare))
        
        similitude = int(len(commonTerms) * 100 / len(data))
        
        if DISPLAY:
            app_logger.info(u'%% de Similitud %s %%' % similitude)
            app_logger.info(u'Total First %s' % len(data))
            app_logger.info(u'Total Second %s' % len(data2Compare))
        
        return similitude
    
    
