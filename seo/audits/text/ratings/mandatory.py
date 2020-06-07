#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating
from seo.containers.seo_document import _getMandatoryBlockTokens
from config import settings
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')
    
class MandatoryRating(object):
    
    RATING_NAME = u'MANDATORY-SCORE'
    RATING_NAME_TOKENS = u'MANDATORY-TOKENS-SCORE'
    RATING_NAME_BLOCKS = u'MANDATORY-BLOCKS-SCORE'
    
    def __init__(self, seoLibrary, mandatoryTerms, textSeoDocument):
        self.seoLibrary = seoLibrary
        self.mandatoryTerms = mandatoryTerms
        self.textSeoDocument = textSeoDocument
        
    def getRating(self):
        ratings = []
        scores, lowerLimits = self._getScore()
        ratings.append(self._getMandatoryBlocksRating(scores['blocks'], lowerLimits['blocks']))
        ratings.append(self._getMandatoryTokensRating(scores['tokens'], lowerLimits['tokens']))
        return ratings
        
    def _getScore(self):
        tokensScore = []
        blocksScore = []
        for seoDocument in self.seoLibrary.seoDocuments[0:settings.MANDATORY_DOCUMENTS_LIMIT]:
            tokenScore, blockScore = self._getMandatoryTermsDocumentScores(seoDocument)
            if blockScore > 0:
            # Todo aquel documento que haya obtenido un 0 en blockScore, podemos dar por hecho que no está posicionado por
            # SEO de contenido
                tokensScore.append(tokenScore)
                blocksScore.append(blockScore)
            
        tokenScore, blockScore = self._getMandatoryTermsDocumentScores(self.textSeoDocument)
        
        
        lowerLimit, _median, upperLimit = getMedianDistributionInfo(tokensScore)
        self.lowerLimitTokens =  int(max(0,lowerLimit))
        self.rawScoreTokens = int(tokenScore)
        self.upperLimitTokens = int(upperLimit)
        
        
        lowerLimit, _median, upperLimit = getMedianDistributionInfo(blockScore)
        self.lowerLimitBlock =  int(max(0,lowerLimit))
        self.rawScoreBlock = int(blockScore)
        self.upperLimitBlock = int(upperLimit)
        
        mandatoryTokensScore = int(tokenScore * 100.00 / (max(1, self.upperLimitTokens)))
        mandatoryTokensLowerLimit = max(0, self.lowerLimitTokens)
        
        mandatoryBlocksScore = int(blockScore * 100.00 / (max(1, self.upperLimitBlock)))
        mandatoryBlocksLowerLimit = max(0, self.lowerLimitBlock)
        
        return {'tokens': mandatoryTokensScore, 'blocks': mandatoryBlocksScore}, {'tokens': mandatoryTokensLowerLimit, 'blocks': mandatoryBlocksLowerLimit}
    
    def _getMandatoryTermsDocumentScores(self, testSeoDocument):
        mandatoryFields = ['uriTokens', 'titleTokens', 'h1Tokens','h2Tokens','strongTokens', 'altTokens', 'metaDescriptionTokens']
        tokenScoreList = []
        blocksScoreList = []
        for seoDocument in self.seoLibrary.seoDocuments:
            scoreTokens = 0
            totalTokens = 0
            scoreBlocks = 0
            totalBlocks = 0
            for mandatoryField in mandatoryFields:
                tokens = _getMandatoryBlockTokens(seoDocument, mandatoryField, unique=True)
                intersection = list(set(tokens) & set(self.mandatoryTerms))
                if intersection:
                    totalBlocks += 1
                    scoreTokensStart = scoreTokens
                    for token in intersection:
                        totalTokens += 1
                        if token in _getMandatoryBlockTokens(testSeoDocument, mandatoryField, unique=True):
                            scoreTokens += 1
                    if scoreTokensStart < scoreTokens:
                        scoreBlocks += 1  
            
            tokenScoreList.append(int(scoreTokens * 100.00 / max(totalTokens, 1)))
            blocksScoreList.append(int(scoreBlocks * 100.00 / max(totalBlocks, 1)))
            
        _lowerLimit, median, _upperLimit = getMedianDistributionInfo(tokenScoreList)
        scoreTokens = int(max(1, median))
        _lowerLimit, median, _upperLimit = getMedianDistributionInfo(blocksScoreList)
        scoreBlocks = int(max(1, median))
        
        return scoreTokens, scoreBlocks
    
    def _getMandatoryTokensRating(self, mandatoryTokensScore, lowerLimitScore):
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if mandatoryTokensScore < lowerLimitScore:
            message = _(u'No usas mandatory Tokens, debes añadir más')
            level = Level.DANGER
            code = Code.ADD
        elif mandatoryTokensScore < 110:
            message = _(u'Usas suficientes mandatory tokens')
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'Estás usando demasiados mandatory tokes, google puede considerarlo SPAM y penalizarte')
            level = Level.DANGER
            code = Code.OVERUSED
            
        return TextAuditRating(
                      MandatoryRating.RATING_NAME_TOKENS, 
                      mandatoryTokensScore,
                      code,
                      level,
                      self.rawScoreTokens,
                      self.lowerLimitTokens,
                      self.upperLimitTokens,
                      message
                      )

    def _getMandatoryBlocksRating(self, mandatoryBlocksScore, lowerLimitScore):
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        interval = 100.00 - lowerLimitScore
        
        if mandatoryBlocksScore < lowerLimitScore:
            message = _(u'Usas muy pocos bloques de mandatory tokens, debes usar más, revisa las combinaciones recomendadas')
            level = Level.DANGER
            code = Code.ADD
        elif mandatoryBlocksScore < interval * 0.35:
            message = _(u'Deberías incluir algún bloque más de mandatory tokens, revisa las combinaciones recomendadas')
            level = Level.WARNING
            code = Code.ADD
        elif mandatoryBlocksScore < 125:
            message = _(u'Usas suficientes mandatory blocks')
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'Estás usando demasiados mandatory blocks, google puede considerarlo SPAM y penalizarte')
            level = Level.DANGER
            code = Code.OVERUSED
            
        return TextAuditRating(
                      MandatoryRating.RATING_NAME_BLOCKS, 
                      mandatoryBlocksScore,
                      code,
                      level,
                      self.rawScoreBlock,
                      self.lowerLimitBlock,
                      self.upperLimitBlock,
                      message
                      )

    
    