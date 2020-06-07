#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
from config import settings
from core.nlp.classifier.classifier import Classifier
import time

class ClassifierFactory(object):

    MODELS = {}
    TYPES = [u'verticals', u'products']
    
    @staticmethod
    def getModel(language, country, classifierType):
        key = u'%s-%s' % (language, country)
        if not key in ClassifierFactory.MODELS:
            ClassifierFactory.MODELS[key] = {}
            for clsType in ClassifierFactory.TYPES:
                ClassifierFactory.MODELS[key][clsType] = Classifier(ClassifierFactory.getModelTrained(language, country, clsType), language, country)
        return ClassifierFactory.MODELS[key][classifierType]

    @staticmethod
    def getModelTrained(language, country, classifierType):
        filename = settings.CLASSIFIER_MODELS_PATH+u'/model_%s_%s_%s.pkl' % (language, country, classifierType)
        model = None
        try:
            model = cPickle.load(open(filename, 'rb'))
            '''
            with open(filename, 'wb') as fout:
                cPickle.dump(model, fout, protocol=cPickle.HIGHEST_PROTOCOL)
                print u'Lo escribimos'
            '''
        except Exception as ex:
            print(ex)
            pass
        if not model:
            raise Exception(u'Modelo no encontrado %s' % filename)
        return model

    @staticmethod
    def warmUp():
        trainedModels = [(u'es',u'ES'), (u'en',u'US'), (u'en',u'GB'), (u'fr',u'FR'), (u'it',u'IT'), (u'pt',u'PT')]
        for language, country in trainedModels:
            for classifierType in ClassifierFactory.TYPES:
                try:
                    init = time.time()
                    ClassifierFactory.getModel(language, country, classifierType)
                    print u'Classifier_%s_%s_%s ---> %s segundos' % (language, country, classifierType, time.time()-init)
                except Exception as ex:
                    print(ex)
    