#!/usr/bin/python
# -*- coding: utf-8 -*-
from nltk.probability import FreqDist
from core.seo.containers.seo_document import _getMandatoryBlockTokens
from config import settings

class SeoLibrary(object):
    
    CACHE_PATH = '/seoLibrary'
    
    def __init__(self, query, language, country):
        self.query = query
        self.language = language
        self.country = country
        self.seoDocuments = []
        self.lemmas = None
        
    def getTrigramsTokens(self, sortedTokens=True, lemmatize=True):
        '''
        Hemos normalizado las apariciones ya que el sistema de obtención de trigramas
        elimina las repeticiones por documento normalizándolo
        '''
        return  [ document.getTrigramsTokens(sortedTokens, lemmatize=lemmatize) for document in self.seoDocuments]
    
    def getBigramsTokens(self, sortedTokens=True, lemmatize=True):
        '''
        Hemos normalizado las apariciones ya que el sistema de obtención de bigramas
        elimina las repeticiones por documento normalizándolo
        '''
        return  [document.getBigramsTokens(sortedTokens, lemmatize=lemmatize) for document in self.seoDocuments]
    
    def getTextTokens(self, lemmatize=True):
        return [document.getTextTokens(lemmatize=lemmatize) for document in self.seoDocuments]
    
    def getUriTokens(self, unique=True):
        return [document.getUriTokens(unique=unique) for document in self.seoDocuments]
    
    def getMetaDescriptionTokens(self, unique=True):
        return [document.getMetaDescriptionTokens(unique=unique) for document in self.seoDocuments]
    
    def getMetaKeywordsTokens(self, unique=True):
        return [document.getMetaKeywordsTokens(unique=unique) for document in self.seoDocuments]
    
    def getTitleTokens(self, unique=True):
        return [document.getTitleTokens(unique=unique) for document in self.seoDocuments]
    
    def getH1Tokens(self, unique=True):
        return [document.getH1Tokens(unique=unique) for document in self.seoDocuments]
    
    def getH2Tokens(self, unique=True):
        return [document.getH2Tokens(unique=unique) for document in self.seoDocuments]
    
    def getStrongTokens(self, unique=True):
        return [document.getStrongTokens(unique=unique) for document in self.seoDocuments]
    
    def getAltTokens(self, unique=True):
        return [document.getAltTokens(unique=unique) for document in self.seoDocuments]
    
    def lemma2Token(self, lemmaTokens):
        tokenList = []
        tokenForms = {}
        if not self.lemmas:
            self.lemmas = {}
            for index in [1,2,3]:
                self.lemmas[index] = {}
                for seoDocument in self.seoDocuments:
                    if index in seoDocument.lemmas:
                        for lemma in seoDocument.lemmas[index]:
                            if lemma not in self.lemmas[index]:
                                self.lemmas[index][lemma] = []
                            self.lemmas[index][lemma].extend(seoDocument.lemmas[index][lemma])
            
        for lemma, metric in lemmaTokens:
            index = len(lemma.split())
            info = self.lemmas[index].get(lemma, [])
            if info:
                freq = FreqDist(info)
                tokenList.append((freq.max(), metric))
                tokenForms[freq.max()] = list(set(info))
            else:
                if(len(lemma.split()) > 1):
                    tokenSeparated, _tf = self.lemma2Token([(part, metric) for part in lemma.split()])
                    if tokenSeparated:
                        token = u' '.join(dict(tokenSeparated).keys())
                        tokenList.append((token, metric))
                        tokenForms[token] = [token]
                
        
        return tokenList, tokenForms   


def getMandatoryBlockTokenList(seoLibrary, mandatoryField, unique=True):
    return [ _getMandatoryBlockTokens(seoDocument, mandatoryField, unique=unique) for seoDocument in seoLibrary.seoDocuments[0:settings.MANDATORY_DOCUMENTS_LIMIT] ]
