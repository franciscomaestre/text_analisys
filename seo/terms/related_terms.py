#!/usr/bin/python
# -*- coding: utf-8 -*-

import gensim
import operator
import math
from core.cache.file_storage_factory import FileStorageFactory
from config import settings

from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class RelatedTerms(object):

    CACHE_PATH = u'/relatedTerms'
    
    def __init__(self, seoLibrary):
        self.seoLibrary = seoLibrary
        self.terms = None
        
    def getTokens(self, window=3, minCount=5, lowerLimit=0.45, positiveQueries=[], numTotal=40, display=False):
        if not self.terms:
            fileStorage = FileStorageFactory.getFileStorage(RelatedTerms.CACHE_PATH)
            key = u'relatedTerms_%s_%s_%s' % (self.seoLibrary.query, self.seoLibrary.language, self.seoLibrary.country)
            self.terms = fileStorage.get(key)
            if not self.terms or not settings.CACHE:
                self.terms = self._getTerms(window, minCount, lowerLimit, positiveQueries, numTotal)
                fileStorage.set(key, self.terms)
        if display:
            for word, metric in self.terms.items():
                app_logger.debug(u'%s --> %s' % (word, metric))
        return self.terms
        
    def _getTerms(self, window=3, minCount=5, lowerLimit=0.45, positiveQueries=[], numTotal=40):
        '''
        Modificación del word2vect a la que en vez de pasarle la query, le pasamos los 
        mejores bigramas que hayamos obtenido para que nos de los similares
        
        Word2vect debe de ser entrenado con los token tal y como aparecían
        '''
        tokenList = self.seoLibrary.getTextTokens()
        
        model = gensim.models.Word2Vec(tokenList, size=10, window=window, min_count=minCount, workers=4)

        most = {}
        for positive in positiveQueries:
            try:
                temp = dict(model.most_similar(positive, topn=10))
                for token, value in temp.items():
                    if token in most.keys():
                        most[token] += value
                    else:
                        most[token] = value + 1.0
            except:
                pass
            
        maxValueNormalized = math.log(max(most.values()))
        
        result = {}
        
        for token in most.keys():
            value = math.log(most[token]) / maxValueNormalized
            if value > lowerLimit:
                result[token] = int(100 * value)
        
        return dict(sorted(result.items(), key=operator.itemgetter(1), reverse=True)[0:numTotal])
