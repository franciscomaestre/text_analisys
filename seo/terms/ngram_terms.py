#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import operator
from nlp.word2vec import word2vecScored
from nltk import ngrams as nltk_ngrams
from nlp.wdfIdf import wdfIdf

from utils.logger import LoggerFactory
from nlp import wordListLemmatizer
from config import settings
from collections import Counter
app_logger = LoggerFactory.getInstance('app')


class NgramTerms(object):
    """
    Use lemmatized terms
    """
    
    CACHE_PATH = u'/ngramfTerms'
    
    def __init__(self, seoLibrary):
        
        self.seoLibrary = seoLibrary
        self.ngrams = {}
    
    def getNgramTerms(self, ngrade=2, sortedTokens=True, sizeWord2Vec=12, lowerLimit=0.45, display=settings.DEBUG):
        if not ngrade in self.ngrams:
            self.ngrams[ngrade] = self._getNgramTerms(ngrade=ngrade, sortedTokens=sortedTokens, sizeWord2Vec=sizeWord2Vec, lowerLimit=lowerLimit, display=display)
        return self.ngrams[ngrade]
    
    def _getNgramTerms(self, ngrade, sortedTokens, sizeWord2Vec, lowerLimit, display):
        
        result = []
        
        '''
        Obtenemos los tokens. Estos pueden estár ordenados o no
        '''
        
        ngramsTokenList = self._getNgramTokenList(ngrade, sortedTokens)
        
        '''
        Obtenemos los más comunes. Para ello primero debemos convertir en una 
        única lista el conjunto de listas que tenemos (unificar los documentos en uno sólo)
        '''

        mostCommons = self._getMostCommons(ngramsTokenList, lowerLimit)
        
        result.extend(mostCommons.items())
        
        if display:
            app_logger.debug(u"{space} MostCommons {space}".format(space='-' * 30, ngram=ngrade))
            for token, freq in sorted(mostCommons.items(), key=operator.itemgetter(1), reverse=True):
                app_logger.debug(u'%s --> %s' % (token, freq))
                # print u'%s --> %s' % (token,freq)
        
        '''
        Obtenemos las queries positivas a partir de los mostCommons
        '''
          
        positiveQueries = self._getPositiveQueries(mostCommons, ngrade)
        
        '''
        Obtenemos los más similares a los mostCommons obtenidos
        '''
        
        mostSimilars, mostSimilarOrigin = word2vecScored(ngramsTokenList, size=sizeWord2Vec, resultNumber=10, positiveQueries=positiveQueries)
        
        mostSimilarFiltered = {}
        if mostSimilars:
            resultTokens = dict(result).keys()
            
            maxMostSimilarFreq = max(mostSimilars.values())
            mostSimilarFiltered = dict([(token, min(100, value * 100.00/ maxMostSimilarFreq)) 
                                        for token, value in mostSimilars.items() 
                                            if value / maxMostSimilarFreq > lowerLimit
                                                and token not in resultTokens])
            
            result.extend(mostSimilarFiltered.items())
             
        if display:
            app_logger.debug(u"{space} Word2Vec Similars {space}".format(space='-' * 20, ngram=ngrade))
            for ngraMToken, value in sorted(mostSimilarFiltered.items(), key=operator.itemgetter(1), reverse=True):
                app_logger.debug(u'[%s] %s --> %s' % (mostSimilarOrigin[ngraMToken], ngraMToken, value))
                # print u'[%s] %s --> %s' % (mostSimilarOrigin[ngraMToken], ngraMToken, value)
                
        return dict(result)
    
    def _getNgramTokenList(self, ngrade=2, sortedTokens=True):
        if ngrade == 1:
            #Los tokens devueltos están lematizados
            ngramsTokenList = self.seoLibrary.getTextTokens(lemmatize=True)
        elif ngrade == 2:
            ngramsTokenList = self.seoLibrary.getBigramsTokens(sortedTokens)
        else:
            ngramsTokenList = self.seoLibrary.getTrigramsTokens(sortedTokens)
            
        return ngramsTokenList
    
    def _getMostCommons(self, ngramsTokenList, lowerLimit=0.45):
        
        #Juntamos todos los vectores de tokens en uno solo
        tokens = []
        [tokens.extend(list(set(ngrams))) for ngrams in ngramsTokenList]
        
        fdist = Counter(tokens)
        mostCommonsTuples = fdist.most_common(20)
        
        mostCommons = dict(mostCommonsTuples)
        
        maxFreqValueNormalized = math.log(max(mostCommons.values()))
        
        result = {}
        
        if maxFreqValueNormalized > 0:
            for token in mostCommons.keys():
                freqNormalized = math.log(mostCommons[token]) / maxFreqValueNormalized
                if freqNormalized > lowerLimit:
                    result[token] = int(freqNormalized * 100)
            
        return result
    
    def getWdfIdf(self, ngrade=2, numTokens=10, display=False):
        '''
        Obtenemos los terminos mediante WdfIdf
        '''
           
        ngramsTokenList = self._getNgramTokenList(ngrade=ngrade, sortedTokens=False)   
             
        wdfIdfTokens = wdfIdf(ngramsTokenList, numTokens=numTokens)
        
        if display:
            app_logger.info(u"{space} Wdf-Idf {ngrade} {space}".format(ngrade=ngrade, space='-' * 30))
            print(u"{space} Wdf-Idf {ngrade} {space}".format(ngrade=ngrade, space='-' * 30))
            for token, wdfidf in wdfIdfTokens:
                app_logger.debug(u'%s --> %s' % (token, wdfidf))
            print('-' * 80)
            
        return wdfIdfTokens
    
    def _getPositiveQueries(self, mostCommons, ngrade=2):
        positiveQueries = mostCommons.keys()
        
        querySplit, _resultDict = wordListLemmatizer(self.seoLibrary.query.split(), self.seoLibrary.language)
        
        if ngrade == 1:
            positiveQueries.extend(querySplit)
        elif ngrade == 2:
            tuples = list(nltk_ngrams(querySplit, 2))
            positiveQueries.extend([u'%s %s' % (t[0], t[1]) for t in tuples])
        else:
            tuples = list(nltk_ngrams(querySplit, 3))
            positiveQueries.extend([u'%s %s %s' % (t[0], t[1], t[2]) for t in tuples])
    
        return positiveQueries
    
        
        


    
