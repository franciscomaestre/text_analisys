#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')


class GrammarScoreRating(object):
    RATING_NAME = u'GRAMMAR-SCORE'
    
    def __init__(self, textSeoDocument, badWords):
        self.textSeoDocument = textSeoDocument
        self.badWords = badWords

        
    def getRating(self):
        scoreBadWords = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if scoreBadWords < max(7, self.textSeoDocument.getLenRawTokens()*0.05):
            message = _(u'Tu texto tiene pocas faltas de ortografía')
            level = Level.SUCCESS
            code = Code.OK
        elif scoreBadWords < max(15, self.textSeoDocument.getLenRawTokens()*0.10):
            message = _(u'Tu texto tiene bastantes faltas de ortografía')
            level = Level.WARNING
            code = Code.IMPROVE
        else:
            message = _(u'Tu texto tiene demasiadas faltas de ortografía')
            level = Level.DANGER
            code = Code.IMPROVE
                
        
        return TextAuditRating(
                      GrammarScoreRating.RATING_NAME, 
                      scoreBadWords,
                      code,
                      level,
                      scoreBadWords,
                      lowerLimit=0,
                      upperLimit=int(max(7, self.textSeoDocument.getLenRawTokens()*0.05)),
                      message=message
                      )        
    
    def _getScore(self):
        lenTokensUnicos = len(set(self.textSeoDocument.getTextTokens(lemmatize=True)))
        if lenTokensUnicos <= 0:
            return 0
        return int(len(self.badWords) * 100.00 / lenTokensUnicos)        
        
