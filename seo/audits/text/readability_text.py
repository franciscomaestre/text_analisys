#!/usr/bin/python
# -*- coding: utf-8 -*-

from textstat.textstat import textstat
import hashlib

from utils.logger import LoggerFactory
from config import settings
from utils.persistence.file_storage_factory import FileStorageFactory
from utils.persistence.django.encoding import force_bytes
app_download_logger = LoggerFactory.getInstance('downloader')
app_logger = LoggerFactory.getInstance('app')

class ReadabilityText(object):
    
    CACHE_PATH = u'/readabilityText'
    
    def __init__(self, language='es'):
        self.language = language


    def textReadabilityScore(self, text):
        md5Text = hashlib.md5(force_bytes(text)).hexdigest()
        fileStorage = FileStorageFactory.getFileStorage(ReadabilityText.CACHE_PATH)
        key = u'textReadabilityScore_%s_%s' % (self.language, md5Text)
        result = fileStorage.get(key)
        if not result or not settings.CACHE:
            result = self._textReadabilityScore(text)
        return result
    
    def _textReadabilityScore(self, text):
        if self.language == 'es':
            return self.spanish_flesch_reading_ease(text)
        elif self.language == 'pt':
            return self.portuguese_flesch_reading_ease(text)
        elif self.language == 'it':
            return self.italian_flesch_reading_ease(text)
        elif self.language == 'fr':
            return self.french_flesch_reading_ease(text)
        elif self.language == 'nl':
            return self.dutch_flesch_reading_ease(text)
        elif self.language == 'en':
            return self.english_flesch_reading_ease(text)
        else:
            return 0
    
    # flesch formula
    def english_flesch_reading_ease(self, text):
        return textstat.flesch_reading_ease(text)
    
    # fernandez huerta formula
    def spanish_flesch_reading_ease(self, text):
        ASL = textstat.avg_sentence_length(text)
        ASW = textstat.avg_syllables_per_word(text)
        FRE = 206.84 - float(1.02 * ASL) - float(60 * ASW)
        return int(FRE)
    
    # fernandez huerta formula
    def portuguese_flesch_reading_ease(self, text):
        ASL = textstat.avg_sentence_length(text)
        ASW = textstat.avg_syllables_per_word(text)
        FRE = 206.84 - float(1.02 * ASL) - float(60 * ASW)
        return int(FRE)
    
    # Roberto Vacca & Valerio Franchina formula
    def italian_flesch_reading_ease(self, text):
        ASL = textstat.avg_sentence_length(text)
        ASW = textstat.avg_syllables_per_word(text)
        FRE = 217 - float(1.3 * ASL) - float(60 * ASW)
        return int(FRE)
    
    # Kandel & Moles formula
    def french_flesch_reading_ease(self, text):
        ASL = textstat.avg_sentence_length(text)
        ASW = textstat.avg_syllables_per_word(text)
        FRE = 209 - float(1.15 * ASL) - float(68 * ASW)
        return int(FRE)
    
    # Douma formula
    def dutch_flesch_reading_ease(self, text):
        ASL = textstat.avg_sentence_length(text)
        ASW = textstat.avg_syllables_per_word(text)
        FRE = 206.84 - float(0.33 * ASL) - float(77 * ASW)
        return int(FRE)
