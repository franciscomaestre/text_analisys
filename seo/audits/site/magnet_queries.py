#!/usr/bin/python
# -*- coding: utf-8 -*-

def getMagnetQueries(seoLibrary, includedTokens):
    from seo.terms.magnet_terms import MagnetTerms
    freqTerms = MagnetTerms(seoLibrary, seoDocumentLimit=len(seoLibrary.seoDocuments), scoreLowerLimit=3, uniqueDomains = False)
    magnetTerms = freqTerms.getTokens()
    
    magnetFiltered = {}
    
    for magnet, score in magnetTerms.items():
        found = False
        for token, _score in includedTokens:
            if token in magnet:
                found = True
                break
        if found:
            magnetFiltered[magnet] = score

    return magnetFiltered.items()