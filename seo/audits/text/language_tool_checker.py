#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import settings

import  urllib3, hashlib
from utils.persistence.file_storage_factory import FileStorageFactory
from utils.persistence.django.encoding import force_bytes
from nlp.stop_words import StopWords
import language_check #@UnresolvedImport
from nlp.hunspell import hunSpellcheck
urllib3.disable_warnings() #@UndefinedVariable

from utils.logger import LoggerFactory
app_download_logger = LoggerFactory.getInstance('downloader')
app_logger = LoggerFactory.getInstance('app')

laguageToolChecker_factory = {}

def checkGrammar(textSeoDocument, language, country):
    checkList = []
    try:
        language_country = language+'-'+country
        
        if not language_country in laguageToolChecker_factory:
            laguageToolChecker = LaguageToolChecker(language_country)
            laguageToolChecker_factory[language_country] = laguageToolChecker
        else:
            laguageToolChecker = laguageToolChecker_factory[language_country] 
            
            
        sentences = textSeoDocument.getSentences()
        
        language_country = u"%s_%s"%(language, country)
        for sentence in sentences:
            badWordsList = laguageToolChecker.getBadWords(sentence)
            serializedBadWords = []
            for serializedWord in badWordsList:
                # si esta bien según hunspell, lo damos por bueno
                #if language != "en" and hunSpellcheck(language_country, serializedWord['badWord']): ## check language_country
                #    continue
                if language == "en": ## english
                    serializedBadWords.append(serializedWord)
                elif not hunSpellcheck('en_US', serializedWord['badWord']): ## check english
                    serializedBadWords.append(serializedWord)
            checkList.extend(serializedBadWords)
        return checkList
    except Exception as ex:
        app_logger.error(u"laguageToolChecker %s" % ex)
        return checkList

class BadWord(object):
    def __init__(self, badWord, suggestions, offset, sentence):
        self.badWord = badWord
        self.suggestions = suggestions # list
        self.offset = offset           # content offset
        self.sentence = sentence       # context
            
    def serialize(self):
        return {
                'badWord':self.badWord,
                'offset':self.offset,
                'sentence':self.sentence,
                'suggestion':self.suggestions,
                }


class LaguageToolChecker(object):

    LANGUAGETOOLCHECKER_CACHE_PATH = u'/languageToolChecker'
    ENGLISH_STOP_WORDS = StopWords.getList('english')
    
    def __init__(self, language_country='es-ES'):
        self.language_country = language_country
        self.language = language_country.split("-")[0]
        self.language_tool = language_check.LanguageTool(language_country)

    def getBadWords(self, text):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        md5Text = hashlib.md5(force_bytes(text)).hexdigest()
        fileStorage = FileStorageFactory.getFileStorage(LaguageToolChecker.LANGUAGETOOLCHECKER_CACHE_PATH)
        key = u'languageToolChecker__%s_%s' % (md5Text, self.language_country)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._getBadWords(text)
            fileStorage.set(key, result)
        return result

    def _getBadWords(self, text):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        badWords = []
        
        matches = self.language_tool.check(text)
        for match in matches:
            if match.ruleId in [u'WHITESPACE_RULE', 
                                u'UPPERCASE_SENTENCE_START', 
                                #u'MORFOLOGIK_RULE_ES', 
                                u'COMMA_PARENTHESIS_WHITESPACE']:
                continue
            ## print u'%s' % match
            errorWord = match.context[match.contextoffset:match.contextoffset+match.errorlength]
            
            # siempre quitamos los stopWord en ingles menos en inglés
            if self.language!= 'en' and errorWord in LaguageToolChecker.ENGLISH_STOP_WORDS:
                continue
            
            suggestions = match.replacements
            offset = match.contextoffset
            sentence = match.context
            
            # Don't add if there are "only spaces" differences
            if suggestions:
                if u"".join(suggestions[0].lower().split()) == u"".join(errorWord.lower().split()):
                    continue
            
            badWord = BadWord(errorWord, suggestions, offset, sentence)
            
            badWords.append(badWord.serialize())

        return badWords


if __name__ == "__main__":
    language_country = "es-ES"
    laguageToolChecker = LaguageToolChecker(language_country)
    sentences = [u'El español del camión supervisava la supervisión de la representación',
                 u'La obeja salta esta vaya',
                 u'Esta   es la primra setencia mal escibida',
                 u'La obeja bala y no lo piyas',
                 u'Storage of cookies is voluntary; a client does not have to accept or store cookies.']
    for sentence in sentences:
        badWordsList = laguageToolChecker.getBadWords(sentence)
        print(badWordsList)
    
    tool = language_check.LanguageTool('en-US')
    print(laguageToolChecker.getBadWords(u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy.') )
    
    tool = language_check.LanguageTool('pt-PT')
    print(laguageToolChecker.getBadWords(u'Cola o teu próprio texto aqui... ou berifica este texto, afim de ver alguns dos dos problemas que o LanguageTool consegue detectar. Isto tal vez permita corigir os teus erros à última da hora.') )

    tool = language_check.LanguageTool('fr-FR')
    print(laguageToolChecker.getBadWords(u'Copiez votre texte ici ou vérifiez cet exemple contenant plusieurs erreur que LanguageTool doit doit pouvoir detecter.') )

    tool = language_check.LanguageTool('it-IT')
    print(laguageToolChecker.getBadWords(u'Inserite qui lo vostro testo... oppure controlate direttamente questo ed avrete un assaggio di quali errori possono essere identificati con LanguageTool.') )
    
        
