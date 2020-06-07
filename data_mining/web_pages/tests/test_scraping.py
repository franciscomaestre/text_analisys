import unittest
from core.data_mining.web_pages.scraper import Scraper

class ScrappingTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(ScrappingTestCase, cls).setUpClass()
        cls.googleScraper = Scraper('https://docs.python.org/2/library/urlparse.html');

    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_01_extract_no_cache(self):
        self.data = ScrappingTestCase.googleScraper._getDataDocument()
        self.assertIsNotNone(self.data, u'no data downloaded')

    def test_02_extract_cache(self):
        self.data = ScrappingTestCase.googleScraper.getDataDocument()
        self.assertIsNotNone(self.data, u'no data downloaded')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ScrappingTestCase('test_scraper_getDataDocument'))
    return suite


if __name__ == "__main__":
    unittest.main()
