#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
from config import settings
from nlp.classifier.classifier import Classifier
import time

class ClassifierFactory(object):

    MODELS = {}
    TYPES = ['verticals', 'products']
    
    @staticmethod
    def getModel(language, country, classifierType):
        key = '%s-%s' % (language, country)
        if not key in ClassifierFactory.MODELS:
            ClassifierFactory.MODELS[key] = {}
            for clsType in ClassifierFactory.TYPES:
                ClassifierFactory.MODELS[key][clsType] = Classifier(ClassifierFactory.getModelTrained(language, country, clsType), language, country)
        return ClassifierFactory.MODELS[key][classifierType]

    @staticmethod
    def getModelTrained(language, country, classifierType):
        filename = settings.CLASSIFIER_MODELS_PATH+'/model_%s_%s_%s.pkl' % (language, country, classifierType)
        model = None
        try:
            model = cPickle.load(open(filename, 'rb'))
            '''
            with open(filename, 'wb') as fout:
                cPickle.dump(model, fout, protocol=cPickle.HIGHEST_PROTOCOL)
                print 'Lo escribimos'
            '''
        except Exception as ex:
            print(ex)
            pass
        if not model:
            raise Exception('Modelo no encontrado %s' % filename)
        return model

    @staticmethod
    def warmUp():
        trainedModels = [('es','ES'), ('en','US'), ('en','GB'), ('fr','FR'), ('it','IT'), ('pt','PT')]
        for language, country in trainedModels:
            for classifierType in ClassifierFactory.TYPES:
                try:
                    init = time.time()
                    ClassifierFactory.getModel(language, country, classifierType)
                    print 'Classifier_%s_%s_%s ---> %s segundos' % (language, country, classifierType, time.time()-init)
                except Exception as ex:
                    print(ex)
    