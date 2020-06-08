#!/usr/bin/python
# -*- coding: utf-8 -*-
import nlp as nltk_utils
from utils.persistence.file_storage_factory import FileStorageFactory
import nltk.collocations
from config import settings
from data_mining.web_pages.scrapping_rules import SPLITTER_TAG, SPLITTER



class SeoDocument(object):
    '''
    Clase SeoDocument: El objetivo de esta clase es modelar un documento del que podemos extraer sus
    tokens,stemmerDict,lemmas y sentences
    '''
    
    CACHE_PATH = u'/seoDocument'
    
    def __init__(self, link, dataDocument, order, language, country, cache=settings.CACHE, initialize=True):
        self.link = link
        self.order = order
        self.language = language
        self.country = country
        self.dataDocument = dataDocument
        self.bigramRawTokens = []
        self.trigramRawTokens = []
        self.lenRawTokens = None
        self.cache = cache  # La utilizamos para no cachear el text audit
        self.tokens = []
        self.lemmas = {}
        self.lemmasList = {}
        self.sentences = []
        self.stemmerDict = []
        self.nonStopWords = []
        
        if initialize:
            self.initialize()
        self.blocks = {}  # uri/title/h1/...
        
    def initialize(self):
        if not self.tokens:
            self.getTextTokens(removeSplitter=False)
        if not self.sentences:
            self.getSentences()
        if not self.bigramRawTokens:
            self.getBigramsTokens()
        if not self.trigramRawTokens:
            self.getTrigramsTokens()
            
    def resetPreloads(self):
        self.bigramRawTokens = []
        self.trigramRawTokens = []
        self.lenRawTokens = None
        self.tokens = []
        self.sentences = []
        self.initialize()
    
    def getTrigramsTokens(self, sortedTokens=True, lemmatize=True):
        if not self.trigramRawTokens:
            if sortedTokens:
                trigram_measures = nltk.collocations.TrigramAssocMeasures()
                finder = nltk.collocations.TrigramCollocationFinder.from_words(self.getTextTokens(removeSplitter=False, lemmatize=False))
                trigramList = sorted(finder.score_ngrams(trigram_measures.raw_freq))
                self.trigramRawTokens = [u'%s %s %s' % (trigram[0], trigram[1], trigram[2]) for trigram, _metric in trigramList if not SPLITTER_TAG in trigram]
            else:
                trigramList = list(nltk.ngrams(self.getTextTokens(removeSplitter=False, lemmatize=False), 3))
                self.trigramRawTokens = [u'%s %s %s' % (trigram[0], trigram[1], trigram[2]) for trigram in trigramList if not SPLITTER_TAG in trigram]
        if lemmatize:
            return self._getTextLemmaTokens(self.trigramRawTokens, ngrade=3)
        else:
            return self.trigramRawTokens
    
    def getBigramsTokens(self, sortedTokens=True, lemmatize=True):
        if not self.bigramRawTokens:
            if sortedTokens:
                bigram_measures = nltk.collocations.BigramAssocMeasures()
                finder = nltk.collocations.BigramCollocationFinder.from_words(self.getTextTokens(removeSplitter=False, lemmatize=False))
                bigramList = sorted(finder.score_ngrams(bigram_measures.raw_freq))
                self.bigramRawTokens = [u'%s %s' % (bigram[0], bigram[1]) for bigram, _metric in bigramList if not SPLITTER_TAG in bigram]
            else:
                bigramList = list(nltk.ngrams(self.getTextTokens(removeSplitter=False, lemmatize=False), 2))
                self.bigramRawTokens = [u'%s %s' % (bigram[0], bigram[1]) for bigram in bigramList if not SPLITTER_TAG in bigram]
        if lemmatize:
            return self._getTextLemmaTokens(self.bigramRawTokens, ngrade=2)
        else:
            return self.bigramRawTokens
    
    def getLenRawTokens(self):
        if not self.lenRawTokens:
            self.lenRawTokens = len(self.getTextTokens(lemmatize=False))
        return self.lenRawTokens
    
    def getTextTokens(self, removeSplitter=True, lemmatize=True):
        '''
        Obtenemos las palabras a partir del texto
        '''
        if not self.tokens:
            fileStorage = FileStorageFactory.getFileStorage(SeoDocument.CACHE_PATH)
            key = u'tokens_%s_%s_%s' % (self.link, self.language, self.country)
            self.tokens = fileStorage.get(key)
            if not self.tokens or not self.cache or settings.SCRAPER_RELOAD_CONTENT:
                self.tokens = self._getTextRawTokens()
                if self.cache:
                    fileStorage.set(key, self.tokens)
        
        if lemmatize:
            tokens = self._getTextLemmaTokens(self.tokens, ngrade=1)
        else:
            tokens = self.tokens
        
        if removeSplitter:
            try:
                return [token for token in tokens if token not in SPLITTER]
            except Exception as ex:
                print(tokens)
        else:
            return tokens
        
    def _getTextLemmaTokens(self, tokens, ngrade=1):
        resultList = []
        resultDict = {}
        if not ngrade in self.lemmasList:
            resultList, resultDict = nltk_utils.wordListLemmatizer(tokens, self.language)
            self.lemmas[ngrade] = resultDict
            self.lemmasList[ngrade] = resultList
        return self.lemmasList[ngrade]
    
    def _getTextRawTokens(self):
        tokens = nltk_utils.wordTokenizer(self.dataDocument.text, self.language)
        tokens = nltk_utils.removeStopWords(tokens, self.language, self.nonStopWords)
        return tokens
        
    def getSentences(self):
        if not self.sentences:
            fileStorage = FileStorageFactory.getFileStorage(SeoDocument.CACHE_PATH)
            key = u'sentences_%s_%s_%s' % (self.link, self.language, self.country)
            self.sentences = fileStorage.get(key)
            if not self.sentences or not self.cache:
                self.sentences = nltk_utils.sentenceTokenizer(self.dataDocument.text.replace(SPLITTER_TAG, '.'), self.language)
                if self.cache:
                    fileStorage.set(key, self.sentences)
        return self.sentences
    
    def getUriTokens(self, unique=True):
        if not unique:
            return self._processTokens(self.dataDocument.uri, unique)
        if not 'uriTokens' in self.blocks:
            self.blocks['uriTokens'] = self._processTokens(self.dataDocument.uri, unique)
        return self.blocks['uriTokens']
    
    def getMetaDescriptionTokens(self, unique=True):
        if not unique:
            return self._processTokens(self.dataDocument.meta, unique)
        if not 'metaDescriptionTokens' in self.blocks:
            self.blocks['metaDescriptionTokens'] = self._processTokens(self.dataDocument.meta, unique)
        return self.blocks['metaDescriptionTokens']
    
    def getMetaKeywordsTokens(self, unique=True):
        if not unique:
            return self._processTokens(self.dataDocument.keywords, unique)
        if not 'metaKeywords' in self.blocks:
            self.blocks['metaKeywords'] = self._processTokens(self.dataDocument.keywords, unique)
        return self.blocks['metaKeywords']
    
    def getTitleTokens(self, unique=True):
        if not unique:
            return self._processTokens(self.dataDocument.title, unique)
        if not 'titleTokens' in self.blocks:
            self.blocks['titleTokens'] = self._processTokens(self.dataDocument.title, unique)   
        return self.blocks['titleTokens']
    
    def getH1Tokens(self, unique=True):
        if not unique:
            return self._processTokens(' '.join(self.dataDocument.h1), unique)
        if not 'h1Tokens' in self.blocks:
            self.blocks['h1Tokens'] = self._processTokens(' '.join(self.dataDocument.h1), unique)
        return self.blocks['h1Tokens']
        
    def getH2Tokens(self, unique=True):
        if not unique:
            return self._processTokens(' '.join(self.dataDocument.h2), unique)
        if not 'h2Tokens' in self.blocks:
            self.blocks['h2Tokens'] = self._processTokens(' '.join(self.dataDocument.h2), unique)
        return self.blocks['h2Tokens']
        
    def getStrongTokens(self, unique=True):
        if not unique:
            return self._processTokens(' '.join(self.dataDocument.strong), unique)
        if not 'strongTokens' in self.blocks:
            self.blocks['strongTokens'] = self._processTokens(' '.join(self.dataDocument.strong), unique)
        return self.blocks['strongTokens']
    
    def getAltTokens(self, unique=True):
        if not unique:
            return self._processTokens(' '.join(self.dataDocument.alt), unique)
        if not 'altTokens' in self.blocks:
            self.blocks['altTokens'] = self._processTokens(' '.join(self.dataDocument.alt), unique)
        return self.blocks['altTokens']
    
    def _processTokens(self, tokens, unique=True):
        tokens = nltk_utils.wordTokenizer(tokens, self.language)
        tokens = nltk_utils.removeStopWords(tokens, self.language, self.nonStopWords)
        resultList, resultDict = nltk_utils.wordListLemmatizer(tokens, self.language)
        if unique:
            #Si es Unique, wordListlemmatizer te devuelve un diccionario con lemma --> tokenForms
            #Dado que solo nos interesa el lemma único, sacamos sus keys
            return resultDict.keys()
        else:
            return resultList
    
    def getLanguage(self):
        return self.language
    
    def __str__(self, *args, **kwargs):
        return u'%s || %s...' % (self.link, self.dataDocument.text[:10])

def _getMandatoryBlockTokens(seoDocument, mandatoryField, unique=True):
    if mandatoryField == 'uriTokens':
        return seoDocument.getUriTokens(unique)
    elif mandatoryField == 'titleTokens':
        return seoDocument.getTitleTokens(unique)
    elif mandatoryField == 'metaDescriptionTokens':
        return seoDocument.getMetaDescriptionTokens(unique)
    elif mandatoryField == 'h1Tokens':
        return seoDocument.getH1Tokens(unique)
    elif mandatoryField == 'h2Tokens':
        return seoDocument.getH2Tokens(unique)
    elif mandatoryField == 'strongTokens':
        return seoDocument.getStrongTokens(unique)
    elif mandatoryField == 'altTokens':
        return seoDocument.getAltTokens(unique)    
    
class DataDocument(object):
    
    def __init__(self):
        self.uri = ''
        self.title = ''
        self.meta = ''
        self.keywords = ''
        self.h1 = []
        self.h2 = []
        self.strong = []
        self.alt = []
        self.text = ''
        self.rawHtml = ''
        
        # ------------
        self.bodyWords = 0
        
if __name__ == '__main__':
    from data_mining.web_pages.scraper import Scraper
    from data_mining.web_pages.scrapers.readability import Readability
    url = u'http://www.animalclan.com/es/16739-scalibor-65cm-royal-canin-club-adult-special-performance.html'
    url = u'http://www.publico.es'
    url = u'http://www.animalclan.com/es/15295-royal-canin-gatos-norweian-forest.html?%20search_query=norw&results=1'
    language = u'es'
    country = u'ES'
    
    scraper = Scraper(url, scrapingFilterClass=Readability)
    dataDocument = scraper._getDataDocument()
    seoDocument = SeoDocument(url, order=1, language=language, country=country, dataDocument=dataDocument, cache=False)
    
    print(seoDocument.getTitleTokens(unique=False))
    print(80*'-')
    print(seoDocument._getTextRawTokens())
    print(80*'-')
    for sentence in seoDocument.getSentences():
        print(sentence)
    print(80*'-')
    