#!/usr/bin/python
# -*- coding: utf-8 -*-
from seo.audits.text.readability_text import ReadabilityText
from seo.containers.ratings import SiteAuditRating
from utils.level import Level
from utils.code import Code

class ReadabilityRating(object):
    RATING_NAME = u'READABILITY'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        
    def getRating(self):
        score, badLinks = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        if score < 25:
            message = u'Los documentos de tu web son demasiado confusos'
            level = Level.DANGER
            code = Code.IMPROVE
        elif score < 85:
            message = u'Los documentos de tu web se entienden bien'
            level = Level.ACCEPTABLE
            code = Code.OK
        else:
            message = u'Los documentos de tu web se entienden fácilmente'
            level = Level.SUCCESS
            code = Code.OK
                
        return SiteAuditRating(
                      ReadabilityRating.RATING_NAME, 
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
            readabilityText = ReadabilityText(seoDocument.getLanguage())
            sentences = seoDocument.getSentences()
            completeText = u' . '.join(sentences)
            scoreText = readabilityText.textReadabilityScore(completeText) 
            scoreText = max(0, min(100, scoreText))
            if scoreText < 25:
                badLinks.append(seoDocument.link)
            scores.append(scoreText)
            
        import numpy as np
        
        return int(np.mean(scores)), badLinks

    