#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import settings
from utils.logger import LoggerFactory
import operator
from nlp.classifier.classifier_factory import ClassifierFactory

app_logger = LoggerFactory.getInstance('app')          

def getSeoLibraryMainCategories(seoLibrary, documentsLimit = settings.CLASSIFIER_DOCUMENTS_LIMIT, numCategories = 5):
    mainCategories = {}
    categoriesPerSeoDocument = {}
    for clsType in ClassifierFactory.TYPES:
        mainCat, catPerSeoDocument = _getSeoLibraryMainCategories(seoLibrary, clsType, documentsLimit, numCategories)
        mainCategories[clsType] = mainCat
        categoriesPerSeoDocument[clsType] = catPerSeoDocument
    return mainCategories, categoriesPerSeoDocument

def _getSeoLibraryMainCategories(seoLibrary, classifierType, documentsLimit, numCategories):
    if settings.CLASSIFIER_ENABLED:
        app_logger.debug(u'Comienza la carga del categorizador')
        result = {}
        categoriesPerSeoDocument = {}
        classifier = ClassifierFactory.getModel(seoLibrary.language, seoLibrary.country, classifierType)
        limit = min(len(seoLibrary.seoDocuments), documentsLimit)
        
        for seoDocument in seoLibrary.seoDocuments[0:limit]:
            categories = classifier.predictDocument(seoDocument)
            categoriesPerSeoDocument[seoDocument.link] = dict(categories)
            app_logger.debug(u'%s --> %s' % (seoDocument.link, categories))
            for cat, score in categories:
                if not cat in result:
                    result[cat] = []
                result[cat].append(score)
        
        import numpy as np
        
        for cat, scores in result.items():
            scoreLimit = np.percentile(scores, 25)
            app_logger.debug(u'Original %s --> %s' % (cat, scores))
            app_logger.debug(u'Filtered %s --> %s' % (cat, [score for score in scores if score >= scoreLimit]))
            result[cat] = [score for score in scores if score >= scoreLimit]
        
        lowerLimit = []
        for cat, score in result.items():
            if len(score) > 1:
                lowerLimit.append(len(score))
        
        lowerLimit = np.median(lowerLimit)
        
        resultFiltered = {cat:np.median(scores) for cat, scores in result.items() if len(scores) >= lowerLimit}
        maxScore = max(resultFiltered.values()) 
        resultFiltered = {cat:score for cat, score in resultFiltered.items() if score*100.00/maxScore > 30}
        
        for cat, score in dict(sorted(resultFiltered.items(), key=operator.itemgetter(1),reverse=True)[0:numCategories]).items():
            app_logger.info(u'FINAL: %s --> %s' % (cat, score))
            
        mainCategories = dict(sorted(resultFiltered.items(), key=operator.itemgetter(1),reverse=True)[0:numCategories])
        
        return mainCategories, categoriesPerSeoDocument
    else:
        return {}, {}
    

def getTokensFromCategories(selectedCategories, language, country):
    from operator import itemgetter
    categoriesTokensLists = {}
    for clsType in ClassifierFactory.TYPES:
        classifier = ClassifierFactory.getModel(language, country, clsType)
        model = classifier.model.steps[1][1]
        vocabulary = classifier.model.steps[0][1].vocabulary_
        inversedVocabulary = {pos:token for token,pos in vocabulary.items()}
        for index, category in enumerate(model.classes_):
            if category in dict(selectedCategories.get(clsType, [])).keys():
                categoriesTokensLists[category] = []
                for pos, score in enumerate(model.coef_[index]):
                    if score > 0:
                        categoriesTokensLists[category].append((inversedVocabulary[pos], score))
                categoriesTokensLists[category] = sorted(categoriesTokensLists[category], key=itemgetter(1), reverse=True)[0:5]
    
    return categoriesTokensLists
