#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating
from seo.containers.seo_document import _getMandatoryBlockTokens
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')
    
class MandatoryBlockLengthRating(object):
    
    RATING_NAME_TEMPLATE = u'%s-LENGTH-SCORE'
    
    def __init__(self, mandatoryField, seoLibrary, textSeoDocument):
        self.mandatoryField = mandatoryField
        self.seoLibrary = seoLibrary
        self.textSeoDocument = textSeoDocument
        self.RATING_NAME = MandatoryBlockLengthRating.RATING_NAME_TEMPLATE % self.mandatoryField.upper().replace(u'TOKENS',u'')
        
    def _getScore(self):

        lenList = []
        for seoDocument in self.seoLibrary.seoDocuments:
            tokens = _getMandatoryBlockTokens(seoDocument, self.mandatoryField, unique=False)
            if tokens:
                lenList.append(len(tokens))
        
        lowerLimit, _median, upperLimit = getMedianDistributionInfo(lenList)
        
        self.lowerLimit =  int(lowerLimit)
        self.rawScore = int(len(_getMandatoryBlockTokens(self.textSeoDocument, self.mandatoryField, unique=False)))
        self.upperLimit = int(upperLimit)
        
        mandatoryBlockLengthScore = self.rawScore * 100.00 / (upperLimit)
        lowerLimitScoreLen = max(0, (lowerLimit))
        
        return mandatoryBlockLengthScore, lowerLimitScoreLen
    
    def getRating(self):
        mandatoryBlockLengthScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # interval = 100.00 - lowerLimitScore
        
        if mandatoryBlockLengthScore < lowerLimitScore:
            message = _(u'%s --> Es demasiado corto, revisa los terminos que te recomendamos') % self.mandatoryField
            level = Level.DANGER
            code = Code.SHORT
        elif mandatoryBlockLengthScore <= 100:
            message = _(u'%s --> La longitud es la correcta') % self.mandatoryField
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'%s --> Es demasiado largo, la longitud es excesiva') % self.mandatoryField
            level = Level.DANGER
            code = Code.LONG
            
        return TextAuditRating(
                      self.RATING_NAME, 
                      mandatoryBlockLengthScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )
