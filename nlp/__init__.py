#!/usr/bin/python
# -*- coding: utf-8 -*-
import unicodedata
import string
import nltk
import re
from nltk.stem.snowball import SnowballStemmer

from nlp.stop_words import StopWords

from utils.logger import LoggerFactory
from cache.memcached_factory import MemcachedFactory
from utils.translator import TranslatorFactory
app_logger = LoggerFactory.getInstance('app')

def getNltkLanguage(language):
    if language == "es":
        return 'spanish'
    elif language == "it":
        return 'italian'
    elif language == "fr":
        return 'french'
    elif language == "de":
        return 'german'
    else: 
        return 'english'

def _getSingularize(word, language):
    import pattern.en as pattern_en  # @UnresolvedImport
    import pattern.es as pattern_es  # @UnresolvedImport
    import pattern.fr as pattern_fr  # @UnresolvedImport
    import pattern.de as pattern_de  # @UnresolvedImport
    import pattern.it as pattern_it  # @UnresolvedImport

    if language == "es":
        return pattern_es.singularize(word)
    elif language == "en":
        return pattern_en.singularize(word)
    elif language == "it":
        return pattern_it.singularize(word)
    elif language == "fr":
        return pattern_fr.singularize(word)
    elif language == "de":
        return pattern_de.singularize(word)
    else: 
        return pattern_en.singularize(word)

def _getLemma(word, language):
    import pattern.en as pattern_en  # @UnresolvedImport
    import pattern.es as pattern_es  # @UnresolvedImport
    import pattern.fr as pattern_fr  # @UnresolvedImport
    import pattern.de as pattern_de  # @UnresolvedImport
    import pattern.it as pattern_it  # @UnresolvedImport

    if language == "es":
        return pattern_es.lemma(word)
    elif language == "en":
        return pattern_en.lemma(word)
    elif language == "it":
        return pattern_it.lemma(word)
    elif language == "fr":
        return pattern_fr.lemma(word)
    elif language == "de":
        return pattern_de.lemma(word)
    else: 
        return pattern_en.lemma(word)
    

def _getParse(word, language):
    import pattern.en as pattern_en  # @UnresolvedImport
    import pattern.es as pattern_es  # @UnresolvedImport
    import pattern.fr as pattern_fr  # @UnresolvedImport
    import pattern.de as pattern_de  # @UnresolvedImport
    import pattern.it as pattern_it  # @UnresolvedImport

    if language == "es":
        return pattern_es.parse(word)
    elif language == "en":
        return pattern_en.parse(word)
    elif language == "it":
        return pattern_it.parse(word)
    elif language == "fr":
        return pattern_fr.parse(word)
    elif language == "de":
        return pattern_de.parse(word)
    else: 
        return pattern_en.parse(word)

def wordTokenizer(text, language):
    return nltk.word_tokenize(text, getNltkLanguage(language))

def removeStopWords(tokens, language, nonStopWords=[]):
    
    language = getNltkLanguage(language)
    stopWords = StopWords.getList(language)
    
    ## Siempre quitamos los stop words en ingles
    if language != 'english':
        stopWords.extend(StopWords.getList('english'))
    
    translator = TranslatorFactory.getTranslator(removeAccents=False)         # Mantenemos los acentos
    pattern = re.compile(u"^[a-z0-9áéíóúàèìòùñ-ûîïü._/-]{3,24}$", re.IGNORECASE)  # Mantenemos las mayusculas
    tokens = [translator.trans(t.strip(u'()[]".,;:')) for t in tokens]
    tokens = [t for t in tokens if t in nonStopWords or (pattern.match(t) and t.lower() not in stopWords) ]
    return tokens

def wordListSingularize(wordList, language="es"):
    resultDict = {}
    for word in wordList:
        root = getSingular(word, language)
        resultDict[root] = word
    return resultDict

def getSingular(word, language):
    key = u'singularize:%s:%s' % (word, language)
    singularCached = MemcachedFactory.getInstance(space='nlp').get(key)
    if not singularCached:
        singularCached = _getSingular(word, language)
        MemcachedFactory.getInstance(space='nlp').set(key, {'word':singularCached})
    return u'%s' % singularCached['word']

def _getSingular(word, language):
    result = _getParse(word, language)
    if '/VB' in result:
        return _getLemma(word, language)
    else:
        return _getSingularize(word, language)

def wordListLemmatizer(wordList, language="es"):
    translator = TranslatorFactory.getTranslator(removeAccents=True)
    resultDict = {}
    resultList = []
    for word in wordList:
        cleanWord = translator.trans(word)  # quitamos acentos para lematizar en el mismo lema palabras con/sin acento
        try:
            if len(cleanWord.split()) == 1:
                root = getRoot(cleanWord, language)
            else:
                rootParts = []
                for part in cleanWord.split():
                    rootParts.append(getRoot(part, language))
                root = u' '.join(rootParts)
            if not root in resultDict:
                resultDict[root] = []
            resultDict[root].append(word)
            resultList.append(root)
        except Exception as ex:
            app_logger.error(word)
            app_logger.error(root)
            app_logger.error(u'wordListLemmatizer')
            app_logger.error(wordList)
            app_logger.error(u"wordListLemmatizer: %s" % ex)
    return resultList, resultDict

def getRoot(word, language):
    try:
        key = u'nlp:root:%s:%s' % (u'_'.join(word.split()), language)
        lemmaCached = MemcachedFactory.getInstance(space=u'nlp').get(key, rawKey=True)
        _id = u'word'
        if not lemmaCached:
            lemmaCached = {_id: _getRoot(word, language)}
            MemcachedFactory.getInstance(space=u'nlp').set(key, lemmaCached, rawKey=True)
        return lemmaCached[_id]
    except Exception as ex:
        print(ex)
        return word

def _getRoot(word, language):
    try:
        snowballStemmer = SnowballStemmer(getNltkLanguage(language))
        root = snowballStemmer.stem(u'%s' % word)
        return root
    except Exception as ex:
        print(ex)
        return word

def wordListStemmer(wordList, language="es"):
    # Devuelve un array de tuplas (stem,key)
    snowballStemmer = SnowballStemmer(getNltkLanguage(language))
    stemmerData = [(snowballStemmer.stem(u'%s' % w), u'%s' % w) for w in wordList]
    return stemmerData

def sentenceTokenizer(text, language):
    translator = TranslatorFactory.getTranslator()
    return [translator.trans(sentence).strip(" .,:") for sentence in nltk.sent_tokenize(text, getNltkLanguage(language)) if len(sentence.split()) > 2]


def intersection(iterableA, iterableB, key="", negate=False):
    """Return the intersection of two iterables with respect to `key` function.
        print intersection('Today I am fine'.split(),
                           'Hello How a re you TODAY'.split(),
                           key=unicode.lower)
    """
    def unify(iterable):
        d = {}
        for item in iterable:
            d.setdefault(key(item), []).append(item)
        return d

    A, B = unify(iterableA), unify(iterableB)

    if not negate:
        return [A[k][0] for k in A if k in B]
    else:
        return [A[k][0] for k in A if not k in B]
