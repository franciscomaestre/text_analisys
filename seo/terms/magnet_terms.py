#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.probability import FreqDist
from config import settings
from seo.containers.seo_document import _getMandatoryBlockTokens
from urllib.parse import urlparse
import numpy as np

class MagnetTerms(object):
    
    CACHE_PATH = u'/magnetFrequent'
    
    def __init__(self, seoLibrary, seoDocumentLimit=settings.MANDATORY_DOCUMENTS_LIMIT, scoreLowerLimit=None, uniqueDomains=True):
        self.seoLibrary = seoLibrary
        self.seoDocumentLimit = seoDocumentLimit
        self.scoreLowerLimit = scoreLowerLimit
        self.uniqueDomains = uniqueDomains
        
    def getTokens(self):    

        if self.scoreLowerLimit:
            limits = [self.seoDocumentLimit]
        else:
            limits = np.arange(5,self.seoDocumentLimit+1,5)
        blocks = ['title', 'uri']
        
        resultBigrams = {}
        resultTrigrams = {}
        
        for block in blocks:
            
            bestMandatoryTrigrams = {}
            bestMandatoryBigrams = {}
            
            for limit in limits:
                
                lowerLimit = self.scoreLowerLimit if self.scoreLowerLimit else max(settings.MANDATORY_TOKEN_QUANTITY_LOWER_LIMIT, int(limit*settings.MANDATORY_LOWER_LIMIT))
                
                if limit <= self.seoDocumentLimit:
                    trigrams = []
                    bigrams =[]
                    
                    for seoDocument in self.seoLibrary.seoDocuments[0:limit]:
                        try:
                            parsed_uri = urlparse(seoDocument.link)
                            domain = u'{uri.netloc}'.format(uri=parsed_uri)
                            tokenList = _getMandatoryBlockTokens(seoDocument, u'%sTokens' % block, unique=False)
                            trigrams.extend(self._getTrigrams(domain, tokenList))
                            bigrams.extend(self._getBigrams(domain, tokenList))
                        except Exception as ex:
                            print(u'ERROR - %s - %s' % (seoDocument.link, ex))
                    
                    if self.uniqueDomains:
                        trigrams = self._filterByDomain(trigrams)
                        bigrams = self._filterByDomain(bigrams)
                    else:
                        trigrams = [token for token, _domain in trigrams]
                        bigrams = [token for token, _domain in bigrams]
                    
                    fdist = FreqDist(trigrams)
                    for token, score in fdist.most_common(settings.MANDATORY_MOST_COMMON_LIMIT):
                        if score >= lowerLimit:
                            scoreNormalized = int(score*100.00/limit)
                            if token not in bestMandatoryTrigrams:
                                bestMandatoryTrigrams[token] = scoreNormalized
                            else:
                                if scoreNormalized > bestMandatoryTrigrams[token]:
                                    bestMandatoryTrigrams[token] = scoreNormalized
                            
                    fdist = FreqDist(bigrams)
                    for token, score in fdist.most_common(settings.MANDATORY_MOST_COMMON_LIMIT):
                        if score >= lowerLimit:
                            scoreNormalized = int(score*100.00/limit)
                            if token not in bestMandatoryBigrams:
                                bestMandatoryBigrams[token] = scoreNormalized
                                #bestMandatoryTrigrams[token] = (scoreNormalized, mostCommonLimit)
                            else:
                                if scoreNormalized > bestMandatoryBigrams[token]:
                                    bestMandatoryBigrams[token] = scoreNormalized
                                    #bestMandatoryTrigrams[token] = (scoreNormalized, mostCommonLimit)
            
            resultBigrams.update(bestMandatoryBigrams)
            resultTrigrams.update(bestMandatoryTrigrams)
        
        result = {}
        for token, score in resultBigrams.items():
            found = False
            for trigramToken in resultTrigrams.keys():
                if token in trigramToken:
                    found = True
                    break
            if not found:
                result[token] = score
                
        result.update(resultTrigrams)
                                
        return result
                    
    def _getTrigrams(self, domain, tokenList):
        trigrams = []
        trigram_measures = nltk.collocations.TrigramAssocMeasures()
        finder = nltk.collocations.TrigramCollocationFinder.from_words(tokenList)
        trigramList = sorted(finder.score_ngrams(trigram_measures.raw_freq))
        for trigram, _score in trigramList:
            try:
                trigramToken = u'%s %s %s' % (trigram[0], trigram[1], trigram[2])
                trigramToken = self.seoLibrary.lemma2Token([(trigramToken , 1)])[0][0][0]
                if len(trigramToken.split()) == 3:
                    trigrams.append((trigramToken, domain))
            except:
                pass
        return trigrams
    
    def _getBigrams(self, domain, tokenList):
        bigrams = []
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        finder = nltk.collocations.BigramCollocationFinder.from_words(tokenList)
        bigramList = sorted(finder.score_ngrams(bigram_measures.raw_freq))
        for bigram, _score in bigramList:
            try:
                bigramToken = u'%s %s' % (bigram[0], bigram[1])
                bigramToken = self.seoLibrary.lemma2Token([(bigramToken , 1)])[0][0][0]
                if len(bigramToken.split()) == 2:
                    bigrams.append((bigramToken, domain))   
            except:
                pass
        return bigrams
    
    def _filterByDomain(self, ngramList):
        ngramsFiltered = []
        originMatrix = {}
        
        for token, domain in ngramList:
            if domain not in originMatrix:
                originMatrix[domain] = []
            if token not in originMatrix[domain]:
                originMatrix[domain].append(token)
                ngramsFiltered.append(token)
        return ngramsFiltered
    

    

    
