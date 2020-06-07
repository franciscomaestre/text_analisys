#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import nltk

from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class StopWords(object):
    
    instanceList = {}
    
    @staticmethod
    def getList(language):
        if not language in StopWords.instanceList:
            StopWords.instanceList[language] = StopWords.createList(language)
        return StopWords.instanceList[language]
            
    @staticmethod
    def createList(language):
        stopWords = nltk.corpus.stopwords.words(language)
        stopWords.extend(string.punctuation)
        stopWords.extend(['...', '""', "''", '!!', '??', ' :'])
        stopWords.extend(['facebook', 'twitter', 'google', 'cookies', 'pinterest', 'cookies?', 'etc'])
        stopWords.extend(['instagram', 'comentario', 'aviso', 'legal', 'contacto', 'correo', 'http', 'https', 'com', 'org'])
        stopWords.extend(['unos', 'unas'])
        #stopWords.extend([u'cómo', u'qué', u'cuándo', 'porque', u'adónde', 'como', 'que', u'quién', 'quien', u'cuántos', 'cuantos', 'donde', u'dónde', 'cuanto', 'aunque', 'ahora', u'sesión', 'unos', 'unas'])
        return stopWords

    @staticmethod
    def extraStopword(language='es'):
        if language == 'es':
            return [u'cómo', u'qué', u'cuándo', u'porque', u'adónde', u'como', u'que', u'quién', u'quien', u'cuántos', u'cuantos', u'donde', u'dónde', u'cuanto', u'aunque', u'ahora', u'sesión', u'unos', u'unas']
        else:
            return []
