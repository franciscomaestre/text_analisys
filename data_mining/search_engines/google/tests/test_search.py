#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from core.data_mining.search_engines.google.google_api_search import GoogleSearchEngine
from core.data_mining.search_engines.google.google_scraper import GoogleScraper
from core.data_mining.search_engines.google.google_selenium import GoogleSelenium

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(GoogleSearchTest, cls).setUpClass()
        cls.query = u'Fitness y musculacion Maquinas de pilates'
        cls.language = 'es'
        cls.country = 'ES'
        cls.googleHost = 'google.es'

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def _test_google_engine_search(self):
        googleSearch = GoogleSearchEngine(GoogleSearchTest.query, GoogleSearchTest.language, GoogleSearchTest.country, GoogleSearchTest.googleHost)
        items = googleSearch.search()
        self.assertTrue(len(items) > 10, 'GoogleSearchEngine: Problem obtaining 40 Urls')

    def test_google_scraper_search(self):
        googleScraper = GoogleScraper(query=GoogleSearchTest.query,
                                      language=GoogleSearchTest.language,
                                      country=GoogleSearchTest.country,
                                      googleHost=GoogleSearchTest.googleHost,
                                      max_results=20)
        
        items = googleScraper.search()
        self.assertTrue(len(items) > 10, 'GoogleScraper: Problem obtaining 20 Urls')
    
    def _test_google_selenium_search(self):
        googleSelenium = GoogleSelenium(query=GoogleSearchTest.query,
                                      language=GoogleSearchTest.language,
                                      country=GoogleSearchTest.country,
                                      googleHost=GoogleSearchTest.googleHost,
                                      max_results=20)
        
        items = googleSelenium.search()
        self.assertTrue(len(items) > 10, 'GoogleSelenium: Problem obtaining 20 Urls')
    

if __name__ == "__main__":
    unittest.main()
