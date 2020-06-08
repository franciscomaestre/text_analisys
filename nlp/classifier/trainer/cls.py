#!/usr/bin/python
# -*- coding: utf-8 -*-

from nlp.classifier.trainer.topics.extractor import getTopicList, getData
from nlp.classifier.trainer.models.trainer import getModelTrained,\
    testTrainModel
from sklearn.linear_model import SGDClassifier
from data_mining.web_pages.scraper import Scraper
from seo.containers.seo_document import SeoDocument
from config import settings
import platform
import gc

'''
Google Adwords Taxonomies: Product & Services
https://www.google.com/basepages/producttype/taxonomy.en-US.txt
'''

def downloadContent(language, country):
    
    #taxonomyFiles = [('es','ES'), ('en','US'), ('en','GB'), ('fr','FR'), ('it','IT'), ('pt','BR')]

    levels = [1]
    if settings.DEBUG and platform.node() in settings.LOCAL_CPUS:
        print('Local settings --- %s' % platform.node())
        levels = [1]
            
    for level in levels:
        print('Comenzamos el nivel %s' % level)
        testModels(level, language, country)

def testModels(initLevel= 1, language='es', country='ES'):
    
    topicList = getTopicList('data/%s/taxonomy.%s-%s.txt' % (settings.TRAINER_TREE_TYPE, language, country), initLevel=initLevel, minTopicSize=4)
    
    trainerData = getData(topicList, initLevel, language, country)
    
    topicList = None
    
    if settings.TRAINER_TRAIN_MODEL:
        
        clsList = [
                   SGDClassifier(n_jobs=1, loss='modified_huber', penalty='l2', n_iter=10, learning_rate='optimal', alpha=0.0001, fit_intercept=True),
                   ]
        
        for cls in clsList:
            try:
                print('INICIAMOS PRUEBAS MANUALES NIVEL %s para %s' % (initLevel, str(cls).split('(')[0]))
                model = getModelTrained(cls, trainerData, reloadModel=True)
                testTrainModel(model, trainerData)
                manualTest(model, trainerData.language, trainerData.country)
            except Exception as ex:
                print(ex)  
    else:
        trainerData = None
        print('No Trainer Data to Train')
        
    gc.collect()

def manualTest(model, language, country):

    links = [
             'http://www.dinersclub.com.ec/',
             ]
    
    
    for link in links:
        predictLink(model, link, language, country)
    
def predictLink(model, link, language, country):
    googleScraper = Scraper(link, sameOrigin=True)
    dataDocument = googleScraper.getDataDocument()
    seoDocument = SeoDocument(link, dataDocument, 1, language, country)
    document = ' '.join(seoDocument.getTextTokens(lemmatize=True))
    print('%s --> %s' % (model.predict([document])[0], link))
    try:
        probability = model.predict_proba([document])[0]
        results = []
        for i in range(0, len(probability)):
            results.append((model.steps[-1][-1].classes_[i], int(probability[i] * 100)))
        print(link)
        for topic, prob in sorted(results, key=lambda tup: tup[1], reverse=True)[0:2]:
            print('-------    %s -->\t%s' % (topic, prob))
    except Exception as ex:
        print(ex)
    
