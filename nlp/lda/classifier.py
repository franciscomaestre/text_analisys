#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import math
import operator

from core.nlp.classifier.classifier_factory import ClassifierFactory

#
# gensim. Phrase collocation detection: 
# https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf
#

def classifyLdaTopics(topTopics, topicsFreq, language, country):                
    '''
    Categorizamos los topics resultantes
    '''

    logTopicFreq = [math.log(f+1) for f in topicsFreq.values()]
    minFreq = np.mean(logTopicFreq)
    
    results = {}
    for index, _topic in enumerate(topTopics):
        if math.log(topicsFreq[index]+1) < minFreq:
            continue
        topic_words = [t[0] for t in topTopics[index][1]]
        topic_words = u' '.join(topic_words)
        #print("(%2s) -- FREQ %s --  %s" % (index, topicsFreq[index], topic_words))
        categoriesDetected = {}
        try:
            for clsType in ClassifierFactory.TYPES:
                classifier = ClassifierFactory.getModel(language, country, clsType)
                categoriesDetected[clsType] = dict(classifier.predictText(topic_words))
        except Exception as ex:
            continue
        for categoriesType, categories in categoriesDetected.items():
            if categoriesType not in results:
                results[categoriesType] = {}
            for category, score in categories.items():
                if category not in results[categoriesType]:
                    results[categoriesType][category] = []
                results[categoriesType][category].append(score)
    
    for categoriesType, categories in results.items():
        for category, scores in categories.items():
            scoreLimit = np.percentile(scores, 25)
            results[categoriesType][category] = np.median([score for score in scores if score >= scoreLimit])
        results[categoriesType] = sorted(results[categoriesType].items(), key=operator.itemgetter(1),reverse=True)

    return results

def findLdaTopicNames(topTopics, topicsFreq, language, country):                
    '''
    Categorizamos los topics resultantes
    '''
    
    results = []
    for index, _topic in enumerate(topTopics):
        topic_words = [t[0] for t in topTopics[index][1]]
        topic_words = u' '.join(topic_words)
        
        categoriesDetected = {}
        try:
            for clsType in ClassifierFactory.TYPES:
                classifier = ClassifierFactory.getModel(language, country, clsType)
                categoriesDetected[clsType] = classifier.predictText(topic_words)
        except Exception as ex:
            continue
        
        results.append(categoriesDetected)
        
    return results
    
    
    