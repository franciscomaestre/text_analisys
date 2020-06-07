#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.cache.file_storage_factory import FileStorageFactory
from config import settings

from utils.logger import LoggerFactory
from core.seo.containers.seo_details import SeoDetails
app_logger = LoggerFactory.getInstance('app')

DISPLAY = True

class DetailedTerms(object):
    
    CACHE_PATH = u'/detailedTerms'
    
    def __init__(self, terms, termsForms, seoLibrary):
        self.query = seoLibrary.query
        self.language = seoLibrary.language
        self.country = seoLibrary.country
        self.seoLibrary = seoLibrary
        self.terms = terms
        self.termsForms = termsForms
        self.details = None
        
    def getTokens(self, contexLimit=5, display=DISPLAY):
        if not self.details:
            fileStorage = FileStorageFactory.getFileStorage(DetailedTerms.CACHE_PATH)
            key = u'detailedTerms_%s_%s_%s' % (self.query, self.language, self.country)
            self.details = fileStorage.get(key)
            if not self.details or not settings.CACHE:
                self.details = self._getTerms(contexLimit)
                fileStorage.set(key, self.details)
        return self.details
        
    def _getTerms(self, contexLimit=settings.CONTEXT_LIMIT):
        terms = dict(self.terms).keys()
        seoDetailsList = []
        for term in terms:
            seoDetailsList.append(self._getTermDetails(term, contexLimit))
        response = {}
        for seoDetails in seoDetailsList:
            response[seoDetails.token] = seoDetails.getInfo()
        return response
    
    def _getTermDetails(self, term, contexLimit):
        seoDetails = SeoDetails(term, self.termsForms.get(term,[]))
        for seoDocument in self.seoLibrary.seoDocuments:
            # Recorremos los documentos buscando aquellos que contienen el Token
            # dividimos el token en partes
            termParts = term.split()
            if termParts[0] in seoDocument.getTextTokens(removeSplitter=False, lemmatize=False):
            # Comprobamos si la primera parte del token está en el documento
                sentences = []
                for sentence in seoDocument.getSentences():
                    try:
                        pos = sentence.index(termParts[0])
                        startPosition = max(0, pos - settings.DETAILED_WORD_LENGTH * settings.DETAILED_WORD_LIMIT)
                        endPosition = pos + settings.DETAILED_WORD_LENGTH * (settings.DETAILED_WORD_LIMIT + len(termParts))
                        partialSentence = sentence[startPosition:endPosition]
                        
                        startIndex = 0
                        if startPosition > 0:
                            startIndex = 1
                        
                        endIndex = -1 
                        if endPosition > len(sentence):
                            endIndex = len(partialSentence.split())
                        
                        partialSentence = u' '.join(partialSentence.split()[startIndex:endIndex])
                                
                        contains = True
                        for termPart in termParts:
                            if termPart not in partialSentence:
                                contains = False
                                break
                        if contains:
                            sentences.append(partialSentence)
                    except:
                        continue
                    if len(sentences) > settings.DETAILED_LIMIT:
                        break
                if sentences:
                    seoDetails.addSentences(seoDocument.link, sentences)
        return seoDetails

