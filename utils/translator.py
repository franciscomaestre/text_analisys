#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.logger import LoggerFactory

app_logger = LoggerFactory.getInstance('app')

class Translator(object):
    
    def __init__(self, tabin, tabout):
        self.tabin = [ord(char) for char in tabin]
        self.tabout = tabout
        self.translateTable = dict(zip(self.tabin, self.tabout))
        
    def trans(self, toTranslate):
        try:
            return toTranslate.translate(self.translateTable).strip()
        except Exception as ex:
            app_logger.error(u"Translator First Try: %s %s" % (ex, toTranslate))
            try:
                toTranslate = u'%s' % toTranslate
                return toTranslate.translate(self.translateTable).strip()
            except Exception as ex:
                app_logger.error(u"Translator Second Try: %s %s" % (ex, toTranslate))
    
class TranslatorFactory(object):
    
    instance = {}  
    
    @staticmethod
    def getTranslator(removeAccents=False):
        version = 'accents' if not removeAccents else 'noAccents'
        if not version in TranslatorFactory.instance:
            if not removeAccents:
                TranslatorFactory.instance[version] = Translator(u"¿?¡!()\".", u"        ")
            else:
                TranslatorFactory.instance[version] = Translator(u"áéíóúàèìòùâêîôûäëïöüç¿?¡!()\".", u"aeiouaeiouaeiouaeiouc      ")  # signos alrededor de las palabras
        return TranslatorFactory.instance[version]
    
