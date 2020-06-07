#!/usr/bin/python
# -*- coding: utf-8 -*-

from experiments.trainer.topics.extractor import getTopicList, getData
from experiments.trainer.models.trainer import getModelTrained,\
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
        print 'Local settings --- %s' % platform.node()
        levels = [1]
            
    for level in levels:
        print 'Comenzamos el nivel %s' % level
        testModels(level, language, country)

def testModels(initLevel= 1, language='es', country='ES'):
    
    topicList = getTopicList('data/%s/taxonomy.%s-%s.txt' % (settings.TRAINER_TREE_TYPE, language, country), initLevel=initLevel, minTopicSize=4)
    
    trainerData = getData(topicList, initLevel, language, country)
    
    topicList = None
    
    if settings.TRAINER_TRAIN_MODEL:
        
        clsList = [
                   #LinearSVC(tol=0.1, penalty='l2'),
                   #PassiveAggressiveClassifier(n_iter=10),
                   SGDClassifier(n_jobs=1, loss='modified_huber', penalty='l2', n_iter=10, learning_rate='optimal', alpha=0.0001, fit_intercept=True),
                   #SVC(random_state=0, kernel='linear', probability=True) Mas lento que el caballo del malo
                   ]
        
        for cls in clsList:
            try:
                print 'INICIAMOS PRUEBAS MANUALES NIVEL %s para %s' % (initLevel, str(cls).split('(')[0])
                model = getModelTrained(cls, trainerData, reloadModel=True)
                testTrainModel(model, trainerData)
                manualTest(model, trainerData.language, trainerData.country)
            except Exception as ex:
                print(ex)  
    else:
        trainerData = None
        print 'No Trainer Data to Train'
        
    gc.collect()

def manualTest(model, language, country):

    links = [
             'http://www.luciasecasa.com/',
             'https://es.wikipedia.org/wiki/Metralleta',
             'http://www.zooplus.es/shop/tienda_perros/correas_collares_perros',
             'https://cookpad.com/es/buscar/hummus',
             'http://www.imaginarium.es/juguetes-estimulacion-temprana-para-bebes-339.htm',
             'http://www.enfemenino.com/sexualidad/juegos-eroticos-s483241.html',
             'http://elpais.com',
             'http://www.timeout.es/madrid/es/locales-de-noche/los-mejores-clubes-de-madrid',
             'http://www.elconfidencial.com/alma-corazon-vida/2016-05-10/los-seis-trucos-para-acelerar-tu-metabolismo-y-conseguir-adelgazar-mas-efectivos_1196946/',
             'http://www.automovilesalhambra.es/coches-segunda-mano/?gclid=Cj0KEQjw09C5BRDy972s6q2y4egBEiQA5_guvz95XTjeHMB7PaXZbaMEmaQTiVwYMMs9wFP6sBMaThAaAm7d8P8HAQ',
             'http://www.coches.com/coches-segunda-mano/',
             'http://www.infonieve.es/',
             'http://www.kitesurfmadrid.com/',
             'http://www.zooplus.es/shop/tienda_gatos',
             'http://www.desenfunda.com/articulos-para-la-caza/accesorios-de-caza/fundas-de-armas-de-caza.html',
             'http://www.ikea.com/es/es/catalog/categories/departments/living_room/10398/'
             ]
    
    
    for link in links:
        predictLink(model, link, language, country)
    
def predictLink(model, link, language, country):
    googleScraper = Scraper(link, sameOrigin=True)
    dataDocument = googleScraper.getDataDocument()
    seoDocument = SeoDocument(link, dataDocument, 1, language, country)
    document = ' '.join(seoDocument.getTextTokens(lemmatize=True))
    print '%s --> %s' % (model.predict([document])[0], link)
    try:
        probability = model.predict_proba([document])[0]
        results = []
        for i in range(0, len(probability)):
            results.append((model.steps[-1][-1].classes_[i], int(probability[i] * 100)))
        print link
        for topic, prob in sorted(results, key=lambda tup: tup[1], reverse=True)[0:2]:
            print '-------    %s -->\t%s' % (topic, prob)
    except Exception as ex:
        print(ex)
    
