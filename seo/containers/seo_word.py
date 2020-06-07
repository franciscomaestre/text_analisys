#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import settings
# from config import SEO_TERMS_DOWNLOAD_LIMIT

class SeoWord(object):
    
    def __init__(self, word):
        self.word = word
        self.seoDocuments = {}
        self.frequencies = {}
        self._globalFrecuency = None
        self._score = None
        self.length = len(word)
        self.scoreRelatedModel = None
        self.scoreRelatedQuery = None
    
    @property
    def score(self):
        if not self._score:
            self._score = self.calcScore()
        return self._score
    
    def calcScore(self):
        score = 15 * self.lengthScore()
        score += 35 * self.occurScore() * self.rankingScore()
        score += 50 * self.relatedScore()
        return int(score)
    
    '''
    Cada score está normalizado entre 0 y 100
    '''
    
    def occurScore(self):
        return Metrics.getOccurencesNormalized(self.seoDocuments.values())
    
    def relatedScore(self):
        result = 0
        for queryToken in self.scoreRelatedQuery:
            try:
                result += self.scoreRelatedModel.n_similarity([self.word], [queryToken])
            except:
                '''
                Se puede dar el caso de que este token no se encuentre en el bloque o que
                parte de la query no esté
                '''
                result += 0
        return result / len(self.scoreRelatedQuery)
        
    def lengthScore(self):
        return Metrics.getLengthNormalized(self.length)
    
    def rankingScore(self):
        return Metrics.getRankingNormalized(self.seoDocuments.values())  
    
    '''
    def freqScore(self):
        return Metrics.getFreqNormalized(self.frequencies.values())  
    '''
    
    def addSeoDocument(self, seoDocument):
        self.seoDocuments[seoDocument.order] = seoDocument
        # self.frequencies[seoDocument.order] = seoDocument.getFreqDist().get(self.word,0)/seoDocument.getLenRawTokens()
        
    def __str__(self, *args, **kwargs):
        return u'{word} --> {score} (Len:{len},Rank*Occur:{derivate},Rel={rel})'.format(
                                                                 word=self.word,
                                                                 score=self.score,
                                                                 len=self.lengthScore(),
                                                                 derivate=self.rankingScore() * self.occurScore(),
                                                                 rel=self.relatedScore())
    
    
class Metrics(object):
    
    LENGTH = [0.0, 0.03, 0.06, 0.11, 0.15, 0.22, 0.35, 0.41, 0.53, 0.65, 0.73, 0.85, 0.95, 1.00]
    
    @staticmethod
    def getLengthNormalized(wordLength):
        if len(Metrics.LENGTH) > wordLength:
            return Metrics.LENGTH[wordLength - 1]
        else:
            return Metrics.LENGTH[-1]
        
    @staticmethod
    def getRankingNormalized(seoDocuments):
        occurrences = len(seoDocuments)
        total = 0
        for seoDocument in seoDocuments:
            total += 1.0 - seoDocument.order * (1.0 - 0.6) / settings.SEO_TERMS_DOWNLOAD_LIMIT
        return total / occurrences
        
    @staticmethod
    def getFreqNormalized(frequencies):
        occurrences = len(frequencies)
        total = sum(frequencies)
        return float(total) / occurrences
    
    @staticmethod
    def getOccurencesNormalized(seoDocuments):
        occurences = len(seoDocuments)
        return min(1.0, 2.0 * float(occurences) / settings.SEO_TERMS_DOWNLOAD_LIMIT)
        
