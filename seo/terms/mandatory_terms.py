#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.probability import FreqDist
import itertools
from config import settings
import math
from utils.median_distribution import getMedianDistributionInfo

class MandatoryTerms(object):
    
    CACHE_PATH = u'/frequent'
    INTERVALS =  [5, 10, 15, 20]
    
    def __init__(self, seoLibrary, mostCommonLimit=settings.MANDATORY_MOST_COMMON_LIMIT):
        self.seoLibrary = seoLibrary
        self.mostCommonLimit = mostCommonLimit
        
    def getTokens(self):
        """
        rankedMandatory 
        {'tokens': 
            {u'bar': {'all': {'densityAverage': 0.5584,
                              'densityUpperLimit': 2.55,
                              'freqAverage': 0,
                              'freqUpperLimit': 1},
                      'h1': {'densityAverage': 0.0,
                             'densityUpperLimit': 0.0,
                             'freqAverage': 0,
                             'freqUpperLimit': 0},
                      'h2': {'densityAverage': 0.5073,
                                  ....
        """        
        
        
        
        mandatoryTokens = self._getTokens()
        
        maxValue = min(len(self.seoLibrary.seoDocuments), max(MandatoryTerms.INTERVALS))
        
        documentsFreqs = []
        
        for seoDocument in self.seoLibrary.seoDocuments[0:maxValue]:
            documentsFreqs.append(FreqDist(seoDocument.getTextTokens(lemmatize=True)))
        
        #Para cada bloque de cada documento, tenemos una lista de FreqDist's
        mandatoryFreqs = {
                      'uriTokens': self._getTokensFreqList(self.seoLibrary.getUriTokens(unique=False), maxValue),
                      'titleTokens': self._getTokensFreqList(self.seoLibrary.getTitleTokens(unique=False), maxValue),
                      'metaDescriptionTokens': self._getTokensFreqList(self.seoLibrary.getMetaDescriptionTokens(unique=False), maxValue),
                      'h1Tokens': self._getTokensFreqList(self.seoLibrary.getH1Tokens(unique=False), maxValue),
                      'h2Tokens':self._getTokensFreqList(self.seoLibrary.getH2Tokens(unique=False), maxValue),
                      'strongTokens':self._getTokensFreqList(self.seoLibrary.getStrongTokens(unique=False), maxValue),
                    }
        
        allList = []
        
        for i in range(0, maxValue):
            freqs = FreqDist()
            for blockFreqList in mandatoryFreqs.values():
                freqs += blockFreqList[i]
            allList.append(FreqDist(freqs))
            
        mandatoryFreqs['all'] = allList
        
        mandatoryTokensInfo = {}
        
        for lemma in mandatoryTokens:
            occurencesScore, seoDocumentsFreqs, seoDocumentsDensities = self._getseoDocumentsInfo(lemma, documentsFreqs)
            if occurencesScore > settings.MANDATORY_LOWER_LIMIT:
                token = self.seoLibrary.lemma2Token([(lemma, 1)])[0][0][0]
                if not token in mandatoryTokensInfo:
                    # create entry
                    mandatoryTokensInfo[token] = {}
                
                for mandatoryField, freqList in mandatoryFreqs.items():
                    freqs = []
                    densities = []
                    for freqTokens in freqList:
                        freqs.append(freqTokens.get(lemma, 0))
                        densities.append(int(freqTokens.get(lemma, 0)*10000/max(1,freqTokens.N()))/100.00)
                    mandatoryTokensInfo[token][mandatoryField] = self._getBlockInfo(freqs, densities)
                mandatoryTokensInfo[token]['text'] =self._getBlockInfo(seoDocumentsFreqs, seoDocumentsDensities)
        return mandatoryTokensInfo
    
    def _getBlockInfo(self,freqs, densities):
        result = {}
        _lowerLimit, median, upperLimit = getMedianDistributionInfo([density for density in densities if density > 0.0])
        result['densityAverage'] = median
        result['densityUpperLimit'] = int(100*upperLimit)/100.00
        _lowerLimit, median, upperLimit = getMedianDistributionInfo([freq for freq in freqs if freq > 0])
        result['freqAverage'] = median
        result['freqUpperLimit'] = max(math.ceil(upperLimit), settings.MANDATORY_TOKEN_MIN_QUANTITY)
        return result
    
    def _getseoDocumentsInfo(self, lemma,  documentsFreqs):
        score = 0
        freqs = []
        densities = []
        for dDist in documentsFreqs:
            if lemma in dDist:
                score+=1
            densities.append(int(dDist.get(lemma, 0)*10000/max(1, dDist.N()))/100.00)
            freqs.append(dDist.get(lemma, 0))
        return score*1.00/len(documentsFreqs), freqs, densities
    
    def _getTokens(self):
        mandatoryTokens = set()
        
        limits = [limit for limit in MandatoryTerms.INTERVALS if limit <= len(self.seoLibrary.seoDocuments) and limit <= settings.MANDATORY_DOCUMENTS_LIMIT]
        
        for limit in limits:
            
            mandatory = {
                      'uriTokens': self._getTokensList(self.seoLibrary.getUriTokens(unique=True), limit),
                      'titleTokens': self._getTokensList(self.seoLibrary.getTitleTokens(unique=True), limit),
                      'metaDescriptionTokens': self._getTokensList(self.seoLibrary.getMetaDescriptionTokens(unique=True), limit),
                      'h1Tokens': self._getTokensList(self.seoLibrary.getH1Tokens(unique=True), limit),
                      'h2Tokens':self._getTokensList(self.seoLibrary.getH2Tokens(unique=True), limit),
                      'strongTokens':self._getTokensList(self.seoLibrary.getStrongTokens(unique=True), limit),
                    }
    
            tokens = list(itertools.chain(*mandatory.values()))
            allFreqDist = FreqDist(tokens)
            for token, _freq in allFreqDist.most_common(self.mostCommonLimit):
                mandatoryTokens.add(token)
                
        return list(mandatoryTokens)
    
    def _getTokensList(self, listTokenList, maxDocuments): 
        return list(itertools.chain(*[tokenList for tokenList in listTokenList[0:maxDocuments]])) 
    
    def _getTokensFreqList(self, listTokenList, maxDocuments): 
        return [FreqDist(tokenList) for tokenList in listTokenList[0:maxDocuments]]
    
    
