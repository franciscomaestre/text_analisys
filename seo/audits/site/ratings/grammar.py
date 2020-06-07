#!/usr/bin/python
# -*- coding: utf-8 -*-
from seo.audits.text.language_tool_checker import checkGrammar
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

GRAMMAR_MAX_PERCENTAJE_ERRORS = 10

class GrammarRating(object):
    RATING_NAME = u'GRAMMAR'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score, badLinks = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if score > GRAMMAR_MAX_PERCENTAJE_ERRORS:
            message = u'Tienes demasiadas faltas de ortografía por documento'
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = u'Tus documentos tienen buena ortografía'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      GrammarRating.RATING_NAME, 
                      score,
                      code,
                      level,
                      links=badLinks,
                      domainRating=False,
                      message=message
                      )        
    
    def _getScore(self):
        scores = []
        badLinks = []
    
        for seoDocument in self.seoLibrary.seoDocuments:
            badWords = checkGrammar(seoDocument, language=self.seoLibrary.language, country=self.seoLibrary.country)
            lenTokensUnicos = len(set(seoDocument.getTextTokens(lemmatize=True)))
            score = int(len(badWords) * 100.00 / lenTokensUnicos)
            if score > GRAMMAR_MAX_PERCENTAJE_ERRORS:
                badLinks.append(seoDocument.link)
            scores.append(score)    
            
        import numpy as np
        
        return int(np.mean(scores)), badLinks

