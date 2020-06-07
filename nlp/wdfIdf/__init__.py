#!/usr/bin/python
# -*- coding: utf-8 -*-

import gensim
import nltk
import operator
import math

def _wdf(p):
    return p

def _idf(docfreq, totaldocs, log_base=10.0, add=0.0):
    """
    Compute default inverse-document-frequency for a term with document frequency `doc_freq`::

      idf = add + log(totaldocs / doc_freq)
    """
    return add + math.log(1.0 + (1.0 * totaldocs / docfreq), log_base)
           
def wdfIdf(tokensLists, numTokens=10):
    
    dictionary = gensim.corpora.Dictionary(tokensLists)
    
    # dictionary.save('/tmp/prueba.dict') # store the dictionary, for future reference
    # id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
    
    corpus = []
    
    for tokenList in tokensLists:
        corpusPart = dictionary.doc2bow(tokenList)
        lenTokenList = len(tokenList)
        corpusModified = [(token, math.log(freq * 1.0 + 1.0, 2) / math.log(lenTokenList + 1, 2)) for token, freq in corpusPart]
        corpus.append(corpusModified)
            
    # corpus = [dictionary.doc2bow(tokenList) for tokenList in tokensLists]
    
    # gensim.corpora.MmCorpus.serialize('/tmp/prueba.mm', corpus)
    # mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')
    
    tfidf = gensim.models.TfidfModel(corpus, wlocal=_wdf, wglobal=_idf, normalize=True)
    
    result = {}
    
    for document in corpus:
        for tokenId, wdfidf in tfidf[document]:
            if dictionary[tokenId] not in result:
                result[dictionary[tokenId]] = wdfidf
            else:
                result[dictionary[tokenId]] += wdfidf
    
    
    for token in result.keys():
        result[token] /= len(corpus)
        result[token] = int(100 * result[token])
            
    return sorted(result.items(), key=operator.itemgetter(1), reverse=True)[0:numTokens]
