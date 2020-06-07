#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import numpy as np
from config import settings

def getLdaTopics(seoDocumentTokens):
    import gensim

    dictionaryTokens = []
    for tokenList in seoDocumentTokens: 
        dictionaryTokens.append(tokenList)
    dictionary = gensim.corpora.Dictionary(dictionaryTokens)
    corpus = [dictionary.doc2bow(tokenList) for tokenList in dictionaryTokens]
    
    np.random.seed(83)#Lo ponemos para evitar que nos cambie en cada iteración ya que los resultados no convergen del todo en muchos casos
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=settings.SITE_AUDIT_NUM_TOPICS, iterations=10000, passes=15)
    ldaTopics = lda.show_topics(num_topics=settings.SITE_AUDIT_NUM_TOPICS, num_words=settings.SITE_AUDIT_NUM_WORDS_PER_TOPIC, formatted=False)
    
    import pyLDAvis.gensim
    ldaTopicsTable = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    
    return ldaTopics, ldaTopicsTable

def getLdaTokens(seoLibrary, ldaTopics, ldaTopicsTable):
    import math
    import operator
    from api.seo_terms_discovery import _lemma2Token
    
    topicsFreq = ldaTopicsTable[0]['Freq'].to_dict()
    topicsID = ldaTopicsTable[0]['topics'].to_dict()
    
    data = ldaTopicsTable[1]
    lbda = settings.SITE_AUDIT_LAMBDA
    data['relevance'] = lbda * data['logprob'] + (1 - lbda) * data['loglift']
    data['relevance'] += abs(data['relevance'].min(axis=0))
        
    logTopicFreq = [math.log(f+1) for f in topicsFreq.values()]
    minFreq = np.mean(logTopicFreq)
    
    results = {}
        
    for index, _topic in enumerate(ldaTopics):
        if math.log(topicsFreq[index]+1) < minFreq:
            continue
        topic = u'Topic%s' % (topicsID[index])
        topicTokens = []
        
        for t in ldaTopics[index][1]:
            try:
                relevance =  data[(data['Category'] == topic) & (data['Term'] == t[0])].relevance
                relevance = float(relevance)
                topicTokens.append((t[0], relevance))
            except Exception as ex:
                continue
        
        lowerLimit = np.percentile(dict(topicTokens).values(), 25)
        lsaTokens, _tokenForms  = _lemma2Token(topicTokens, seoLibrary)
        for token, relevance in lsaTokens:
            if relevance > lowerLimit:
                if token not in results:
                    results[token] = float('-inf')
                results[token] = max(results[token], int(relevance * topicsFreq[index]))
        
    return sorted(results.items(), key=operator.itemgetter(1), reverse=True)


