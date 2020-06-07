#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from core.data_mining.search_engines.bing.bing_related_search import BingRelatedSearch
from core.data_mining.search_engines.bing.bing_suggestion_search import BingSuggestionSearch
from core.data_mining.search_engines.bing.bing_search import BingSearch
from core.data_mining.search_engines.bing.bing_spellchecker import BingSpellChecker

class BingTest(unittest.TestCase):

    def _test_01_searchbing_nocache(self):
        language = 'es'
        country = 'ES'
        bingCountry = language + '-' + country
        bing = BingRelatedSearch()
        result_list = bing._search_all(u"invertir en bolsa", limit=10, market=bingCountry)
        
        self.assertGreater(len(result_list), 5 , "BingRelatedSearch: pocos resultados %d de 10" % len(result_list))

    def _test_02_searchbing_cache(self):
        language = 'es'
        country = 'ES'
        bingCountry = language + '-' + country
        bing = BingRelatedSearch()
        result_list = bing.search_all(u"invertir en bolsa", limit=10, market=bingCountry)
        
        self.assertGreater(len(result_list), 5 , "BingRelatedSearch: pocos resultados %d de 10" % len(result_list))
            
    def _test_03_suggestions_nocache(self):
        bingSuggestions = BingSuggestionSearch()
        result_list = bingSuggestions._search(u"carlos blanco vazquez", market='es-ES')
        
        self.assertGreater(len(result_list), 1, "BingRelatedSearch: pocos resultados %d de 10" % len(result_list))

    def test_04_suggestions_cache(self):
        bingSuggestions = BingSuggestionSearch()
        result_list = bingSuggestions.search(u"carlos blanco vazquez", market='es-ES')
        
        self.assertGreater(len(result_list), 1, "BingRelatedSearch: pocos resultados %d de 10" % len(result_list))
        
    def test_05_search_cache(self):
        bing = BingSearch()
        result_list = bing.search_all(u"carlos blanco vazquez", downloadLimit=10, market='es-ES')
        
        self.assertGreater(len(result_list), 1, "BingSearch: pocos resultados %d de 10" % len(result_list))
        
    def _test_06_search_nocache(self):
        bing = BingSearch()
        result_list = bing._search_all(u"carlos blanco vazquez", downloadLimit=10, market='es-ES')
        
        self.assertGreater(len(result_list), 1, "BingSearch: pocos resultados %d de 10" % len(result_list))

    def test_07_spellchecker_nocache(self):
        bing = BingSpellChecker()
        result_list = bing._getBadWords('De tanto ojear en las revajas se me a puesto dolor de ojos y eso que dí un vistazo rapido a aquéllos deshechos de la temporada, todo estaba echo un reboltijo y no podía si no echar una mirada desbaída sobre abrigos, vestidos entayados o amplios, abrigos sin, o con ombreras, el gran almacén, era un vatiburrillo sobre el que havía caido una orda de compradores. Era algo expecial y inedito para mí. prefiero la compra tranquila, la charla con el vendedor y la eleción sin hapresuramientos.')
        self.assertGreater(len(result_list), 3, "BingSpellChecker: pocos resultados %d de 10" % len(result_list))
        
    def _test_08_spellchecker_cache(self):
        bing = BingSpellChecker()
        result_list = bing.getBadWords('De tanto ojear en las revajas se me a puesto dolor de ojos y eso que dí un vistazo rapido a aquéllos deshechos de la temporada, todo estaba echo un reboltijo y no podía si no echar una mirada desbaída sobre abrigos, vestidos entayados o amplios, abrigos sin, o con ombreras, el gran almacén, era un vatiburrillo sobre el que havía caido una orda de compradores. Era algo expecial y inedito para mí. prefiero la compra tranquila, la charla con el vendedor y la eleción sin hapresuramientos.')
        
        self.assertGreater(len(result_list), 3, "BingSpellChecker: pocos resultados %d de 10" % len(result_list))
        
        
if __name__ == "__main__":
    unittest.main()
