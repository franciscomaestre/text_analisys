#!/usr/bin/python
# -*- coding: utf-8 -*-

import gensim
import operator
from seo.containers.seo_word import SeoWord
from cache.file_storage_factory import FileStorageFactory
from config import settings

from utils.logger import LoggerFactory
from nlp import wordListLemmatizer
app_logger = LoggerFactory.getInstance('app')

class ScoredTerms(object):
    
    CACHE_PATH = u'/scoredTerms'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        self.terms = None
        
    def getTokens(self, window=2, minCount=5, ntotal=30, display=False):
        if not self.terms:
            fileStorage = FileStorageFactory.getFileStorage(ScoredTerms.CACHE_PATH)
            key = u'scoredTerms_%s_%s_%s' % (self.seoLibrary.query, self.seoLibrary.language, self.seoLibrary.country)
            self.terms = fileStorage.get(key)
            if not self.terms or not settings.CACHE:
                self.terms = self._getTerms(window, minCount, ntotal)
                fileStorage.set(key, self.terms)
        if display:
            for word, metric in self.terms.items():
                app_logger.debug(u'%s --> %s' % (word, metric))
        return self.terms
        
    def _getTerms(self, window, minCount, ntotal):
        '''
        En este método, word2vec se entrena con las palabras en el orden en el que aparecen
        filtrando su longitud para asegurar que superan un mínimo
        
        Una vez entrenado, ahora si que si ordenamos con una función de scoring mejor
        '''
        
        querySplit, _resultDict = wordListLemmatizer(self.seoLibrary.query.split(), self.seoLibrary.language)
        
        '''
        Creación del modelo de Word2Vect
        '''
        
        model = gensim.models.Word2Vec(self.seoLibrary.getTextTokens(lemmatize=True), size=10, window=window, min_count=minCount, workers=4)    
        
        ##model.accuracy(questions, restrict_vocab, most_similar)
        
        '''
        Creación de los seoWord
        '''
        
        seoWordsList = {}
        
        for seoDocument in self.seoLibrary.seoDocuments:
               
            for token in seoDocument.getTextTokens(lemmatize=True):
                if token not in seoWordsList:
                    seoWord = SeoWord(token)
                    seoWord.scoreRelatedModel = model
                    seoWord.scoreRelatedQuery = querySplit
                    seoWordsList[token] = seoWord
                seoWordsList[token].addSeoDocument(seoDocument)
        
        '''
        --------------------------------
        def calcScore(self):
            score  = 15 * self.lengthScore()
            score += 35 * self.occurScore() * self.rankingScore()
            score += 50 * self.relatedScore()
            return score
        '''
    
        tokenResult = {}
        
        for seoWord in sorted(seoWordsList.values(), key=operator.attrgetter('score'), reverse=True)[0:ntotal]:
            tokenResult[seoWord.word] = seoWord.score
            
        return tokenResult
