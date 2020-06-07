#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.seo.containers.seo_document import SeoDocument
from core.data_mining.web_pages.scraper import Scraper

class Classifier(object):
    
    def __init__(self, model, language, country):
        self.model = model
        self.language = language
        self.country = country
        
    def predictLink(self, link, ):
        googleScraper = Scraper(link, sameOrigin=True)
        dataDocument = googleScraper.getDataDocument()
        seoDocument = SeoDocument(link, dataDocument, 1, self.language, self.country)
        return self.predictDocument(seoDocument)
        
    def predictDocument(self, seoDocument):
        text = u' '.join(seoDocument.getTextTokens(lemmatize=True))
        return self.predictText(text)
        
    def predictText(self, text):
        try:
            probability = self.model.predict_proba([text])[0]
            results = []
            for i in range(0, len(probability)):
                results.append((self.model.steps[-1][-1].classes_[i], int(probability[i] * 100)))
            return [(u'%s' % topic, prob) for topic, prob in sorted(results, key=lambda tup: tup[1], reverse=True)[0:3]]
        except Exception as ex:
            raise ex
        
        