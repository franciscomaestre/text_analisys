#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from config import settings

import  urllib3, hashlib
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.cache.file_storage_factory import FileStorageFactory
from urllib3.util.retry import Retry
from core.cache.django.encoding import force_bytes
from utils.translator import TranslatorFactory
urllib3.disable_warnings() #@UndefinedVariable

from utils.logger import LoggerFactory
app_download_logger = LoggerFactory.getInstance('downloader')
app_logger = LoggerFactory.getInstance('app')


def checkGrammar(textSeoDocument, language=None, country=None):
    try:
        bingSpellChecker = BingSpellChecker()
        sentences = textSeoDocument.getSentences()
        completeText = ' '.join(sentences)
        badWordsList = bingSpellChecker.getBadWords(completeText)
        for badWord in badWordsList:
            badWord['sentence'], badWord['offset'] = _getBadWordSentences(badWord, sentences)
        return badWordsList
    except Exception as ex:
        app_logger.error(u"_bingSpellChecker %s" % ex)
        return []

        
def _getBadWordSentences(badWord, sentences):
    
    term = badWord['badWord']
    offset = badWord['offset']
    
    origin = u''
    termParts = term.split()
    index = 0
    
    '''
    Buscamos la sentencia que contiene el offset 
    '''
    for sentence in sentences:
        try:
            index += (len(sentence) + 1)
            if index < offset: # find sentence
                continue
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
                offset = pos - startPosition
                origin = partialSentence
                break
        except:
            continue

    return origin, offset

class BingException(Exception):
    pass

class BingSpellChecker(object):

    SPELLCHECKER_CACHE_PATH = u'/spellChecker'
    #QUERY_URL = 'https://bingapis.azure-api.net/api/v5/spellcheck?mode=%s&Market=en-US'
    QUERY_URL = 'https://api.cognitive.microsoft.com/bing/v5.0/spellcheck?mode=%s&Market=en-US'

    def __init__(self, api_key=settings.BING_SPELLCHECKER_KEY):
        self.api_key = api_key
        self.pool = Urllib3PoolFactory.getSameOriginPool()

    def getBadWords(self, text):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        md5Text = hashlib.md5(force_bytes(text)).hexdigest()
        fileStorage = FileStorageFactory.getFileStorage(BingSpellChecker.SPELLCHECKER_CACHE_PATH)
        key = 'spellChecker__%s' % (md5Text)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._getBadWords(text)
            fileStorage.set(key, result)
        return result

    def _getBadWords(self, text):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        if(text.count(' ') <= 9):
            mode = 'spell'
        else:
            mode = 'proof'
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key
        }
        fields = {
            'Text':text
        }
        request = self.pool.request('POST', BingSpellChecker.QUERY_URL % mode, fields=fields, headers=headers, retries=Retry(connect=2, read=2, redirect=2))
        response = request.data
        responseDict = json.loads(response)
        badWords = []
        translator = TranslatorFactory.getTranslator()
        try:
            flaggedTokensList = responseDict['flaggedTokens']
            for flaggedToken in flaggedTokensList:
                suggestions = flaggedToken['suggestions'][0]['suggestion']
                if translator.trans(flaggedToken['token']) != translator.trans(suggestions):
                    
                    # Don't add if there are "only spaces" differences
                    if u"".join(suggestions.lower().split()) == u"".join(flaggedToken['token'].lower().split()):
                        continue
                    
                    badWords.append({'badWord' : flaggedToken['token'], 'suggestion' : suggestions, 'offset' : flaggedToken['offset']})
            return badWords
        except Exception, e:
            return badWords
        
