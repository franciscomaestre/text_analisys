#!/usr/bin/python
# -*- coding: utf-8 -*-


class SeoDetails(object):
    
    def __init__(self, token, forms):
        self.token = token
        self.tokenForms = forms
        self.appearances = []
        
    def addSentences(self, link, sentences):
        self.appearances.append({'link': link, 'sentences': sentences})
        
    def getInfo(self):
        return self.__dict__
