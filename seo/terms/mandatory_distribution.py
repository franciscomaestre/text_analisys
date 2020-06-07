#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.probability import FreqDist

def mandatoryCommonDistribution(seoLibrary, mandatoryTokens, limit):
    blocks = ['uriTokens', 'titleTokens', 'metaDescriptionTokens', 'h1Tokens', 'h2Tokens','strongTokens']
    
    #Numpy 
    vocab = mandatoryTokens
    documentsLen = min(limit, len(seoLibrary.seoDocuments))
    vocabLen = len(vocab)
    mandatoryBlocksLen = len(blocks)
    
    import numpy as np
    """
    Doc x Word X Mandatory
    """
    matrixInfo = np.zeros((documentsLen, mandatoryBlocksLen, vocabLen), np.int16)
    
    # ------
    
    limit = min(limit, len(seoLibrary.seoDocuments))

    for seoDocumentIndex, seoDocument in enumerate(seoLibrary.seoDocuments[0:limit]):
        
        mandatoryList = {}
        
        mandatoryList['uriTokens'] = FreqDist(seoDocument.getUriTokens(unique=False))
        mandatoryList['titleTokens'] = FreqDist(seoDocument.getTitleTokens(unique=False))
        mandatoryList['h1Tokens'] = FreqDist(seoDocument.getH1Tokens(unique=False))
        mandatoryList['metaDescriptionTokens'] = FreqDist(seoDocument.getMetaDescriptionTokens(unique=False))
        mandatoryList['h2Tokens'] = FreqDist(seoDocument.getH2Tokens(unique=False))
        mandatoryList['strongTokens'] = FreqDist(seoDocument.getStrongTokens(unique=False))
        
        
        for blockIndex, block in enumerate(blocks):
            intersection = list(set(mandatoryTokens) & set(mandatoryList[block].keys()))
            for token in intersection:
                tokenIndex = mandatoryTokens.index(token)
                matrixInfo[seoDocumentIndex, blockIndex, tokenIndex] = mandatoryList[block][token]
    
        
    blocksView = np.sum(matrixInfo, axis = 2) > 0 
    
    uniquesDistributions = np.array([np.array(tx) for tx in set(tuple(x) for x in blocksView)])
    
    distributions = [(x, len(blocksView[np.all(blocksView==x, axis=1)])) for x in uniquesDistributions]
    distributions = sorted([(x, freq) for x, freq in distributions if freq > 1], key=lambda x: x[1], reverse=True)
    
    results = []
    
    for dist, freq in distributions[0:3]:
        
        results.append(
                       {
                        'freq': int(freq*100.00/documentsLen),
                        'distribution': [blocks[index] for index, block in enumerate(dist) if block == True]
                        }
                       )
    return results