#!/usr/bin/python
# -*- coding: utf-8 -*-
import gensim
import operator

def word2vec(tokensLists, size=12, resultNumber=10, positiveQueries=[]):
    '''
    Le pasamos una lista de listas.
    Cada sub-lista son los tokens(raw,stemmer,seo_web_audit....) de un documento
    
    Dentro de word2vec podemos usar 3 funciones para obtener palabras o datos sobre las mismas
    
        - similarity(w1,w2)
        - n_similarity(word_list_1,word_list_2)
        - most_similar(positive_word_list)
    '''
    
    result = {}
    
    # tokensLists = [tokensList for tokensList in tokensLists if tokensList]
    try:
        model = gensim.models.Word2Vec(tokensLists, size=size, window=3, min_count=5, workers=4)
    except:
        try:
            model = gensim.models.Word2Vec(tokensLists, size=size, window=3, min_count=2, workers=4)
        except:
            return result
    
    for positiveQuery in positiveQueries:
        try:
            similars = dict(model.most_similar(positive=positiveQuery, topn=resultNumber))
            for token, value in similars.items():
                if token in result.keys():
                    result[token] = max(result[token], value)
                else:
                    result[token] = value
        except Exception as ex:
            # print(ex)
            pass
            
    result_sorted = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    '''
    for token,freq in result_sorted:
        print(u"{token} --> {freq}".format(token=token,freq=freq))
    '''
    
    return [result[0] for result in result_sorted]
    

def word2vecScored(tokensLists, size=12, resultNumber=10, positiveQueries=[]):
    '''
    Le pasamos una lista de listas.
    Cada sub-lista son los tokens(raw,stemmer,seo_web_audit....) de un documento
    
    Dentro de word2vec podemos usar 3 funciones para obtener palabras o datos sobre las mismas
    
        - similarity(w1,w2)
        - n_similarity(word_list_1,word_list_2)
        - most_similar(positive_word_list)
    '''
    
    result = {}
    resultDict = {}
    
    # tokensLists = [tokensList for tokensList in tokensLists if tokensList]
    try:
        model = gensim.models.Word2Vec(tokensLists, size=size, window=3, min_count=5, workers=4)
    except:
        try:
            model = gensim.models.Word2Vec(tokensLists, size=size, window=3, min_count=2, workers=4)
        except:
            return result
    
    for positiveQuery in positiveQueries:
        try:
            similars = dict(model.most_similar(positive=positiveQuery, topn=resultNumber))
            for token, value in similars.items():
                if token in result.keys():
                    result[token] += value
                else:
                    result[token] = value
                    resultDict[token] = positiveQuery
        except Exception as ex:
            # print(ex)
            pass
            
    '''
    for token,freq in result_sorted:
        print(u"{token} --> {freq}".format(token=token,freq=freq))
    '''
    return result, resultDict
