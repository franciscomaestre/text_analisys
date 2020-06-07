#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from core.seo.containers.ratings import TextAuditRating
from core.seo.containers.seo_document import _getMandatoryBlockTokens
from config import settings
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')
    
class MandatoryBlockTokensRating(object):
    
    RATING_NAME_TEMPLATE = u'%s-TOKENS-SCORE'
    
    def __init__(self, mandatoryField, seoLibrary, mandatoryTerms, textSeoDocument):
        self.mandatoryField = mandatoryField
        self.seoLibrary = seoLibrary
        self.mandatoryTerms = mandatoryTerms
        self.textSeoDocument = textSeoDocument
        self.RATING_NAME = MandatoryBlockTokensRating.RATING_NAME_TEMPLATE % self.mandatoryField.upper().replace(u'TOKENS',u'')
        
    def _getScore(self):
        commonsLenList = []
        
        for seoDocument in self.seoLibrary.seoDocuments[0:settings.MANDATORY_DOCUMENTS_LIMIT]:
            mandatoryTokens = _getMandatoryBlockTokens(seoDocument, self.mandatoryField, unique=True)
            commons = list(set(mandatoryTokens) & set(self.mandatoryTerms))
            commonsLenList.append(len(commons))

        lowerLimit, _median, upperLimit = getMedianDistributionInfo(commonsLenList)
        
        self.lowerLimit =  int(max(0,lowerLimit))
        
        mandatoryTokens = _getMandatoryBlockTokens(self.textSeoDocument, self.mandatoryField, unique=True)
        commons = list(set(mandatoryTokens) & set(self.mandatoryTerms))
        self.rawScore = int(len(commons))
        self.upperLimit = int(upperLimit)
        
        mandatoryBlockTokensScore = self.rawScore * 100.00 / max(1.00, upperLimit)
        lowerLimitScoreLen = max(0, (lowerLimit))
        
        return mandatoryBlockTokensScore, lowerLimitScoreLen
    
    def getRating(self):
        mandatoryBlockTokensScore, lowerLimitScore = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # interval = 100.00 - lowerLimitScore
        
        if self.upperLimit == 1:
            message = _(u'%s --> Datos insuficientes para evaluar') % self.mandatoryField
            level = Level.ACCEPTABLE
            code = Code.UNDEFINED
        elif mandatoryBlockTokensScore < lowerLimitScore:
            message = _(u'%s --> Muy pocos mandatory, revisa los terminos que te recomendamos') % self.mandatoryField
            level = Level.DANGER
            code = Code.ADD
        elif mandatoryBlockTokensScore <= 100:
            message = _(u'%s --> Mandatory suficiente') % self.mandatoryField
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'%s --> Demasiados mandatory terms en este bloque') % self.mandatoryField
            level = Level.DANGER
            code = Code.OVERUSED
            
        return TextAuditRating(
                      self.RATING_NAME, 
                      mandatoryBlockTokensScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )
