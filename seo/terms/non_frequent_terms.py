#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk import FreqDist
from utils.concurrence.callback_wait import CallbackWait
from config import settings
# from config import SEO_TERMS_DOWNLOAD_LIMIT
import numpy

from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class NonFrequentTerms(object):
    
    CACHE_PATH = '/lessFrequent'
    
    def __init__(self, seoLibrary):
        ##self.condition = CallbackWait()
        self.seoLibrary = seoLibrary
    
    def getLongTermsRanked(self, minLen=7.0, numberMostCommons=30, display=False):
        result = []
        resultDocuments = {}
        for seoDocument in self.seoLibrary.seoDocuments:
            tokenList = list(set(seoDocument.getTextTokens(removeSplitter=True, lemmatize=True)))
            for token in tokenList:
                if len(token) > minLen:   
                    result.append(token)
                    if token not in resultDocuments:
                        resultDocuments[token] = [seoDocument.order]
                    else:
                        resultDocuments[token].append(seoDocument.order)
        
        fdist = FreqDist(result)
        
        for token in fdist.keys():
            fdist[token] = fdist[token] * self.getRankingModifier(numpy.mean(resultDocuments[token])) * self.getLengthModifier(len(token), minLen)
        
        maxValue = max(fdist.values())
                
        return [(word, int(metric * 100.00 / maxValue)) for word, metric in fdist.most_common(numberMostCommons)]
        
    def getRankingModifier(self, media):
        return 0.5 + (settings.SEO_TERMS_DOWNLOAD_LIMIT - media) / settings.SEO_TERMS_DOWNLOAD_LIMIT
    
    def getLengthModifier(self, length, minLen=7.0):
        return min(2, length / minLen)

    
