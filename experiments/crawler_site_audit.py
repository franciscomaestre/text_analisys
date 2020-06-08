'''
import os
import sys
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')
'''

from scrapy.crawler import CrawlerProcess
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from utils.concurrence.urllib3_pool_factory import Urllib3PoolFactory

class ScrapyCrawler(CrawlSpider):
    name = 'Seologies Crawler'
    start_urls = None
    allowed_domains = None
    invalid_strings = ['javascript']
    custom_settings = {
        'DEPTH_LIMIT': 5,
    }
    
    domainUrls = []
    disallowUris = []
    
    rules = (
        Rule(LinkExtractor(allow=('.*', )), callback="parseDocument", follow= True, process_links='linksFilter'),
    )
    
    @staticmethod
    def configure(start_urls, allowed_domains, invalid_strings, disallowUris):
        ScrapyCrawler.start_urls = start_urls
        ScrapyCrawler.allowed_domains = allowed_domains
        ScrapyCrawler.invalid_strings.extend(invalid_strings)
        ScrapyCrawler.disallowUris = disallowUris
        
    def linksFilter(self,links): 
        # A hook into the links processing from an existing page, done in order to not follow "nofollow" links 
        ret_links = list()
        if links:
            for link in links:
                if not link.nofollow: 
                    ret_links.append(link)
        return ret_links

    def parseDocument(self, response):
        #print u'%s:  Depth: %s\tUrl: %s' % (counter, response.meta['depth'], response.url)
        isFollowDocument = self.isFollowDocument(response)

        for url in response.css('a').css(':not([rel="nofollow"])').css('::attr(href)').extract():
            url = response.urljoin(url).lower()
            isFollowUrl = isFollowDocument and self.isDisallowUri(url)
            urlFollow = 'follow' if isFollowUrl else 'noFollow'
            if not self.isValidUrl(url):
                continue
            ScrapyCrawler.domainUrls.append(CrawlerData(url, response.url, urlFollow))
            
        for url in response.css('a[rel="nofollow"]').css('::attr(href)').extract():
            url = response.urljoin(url).lower()
            if not self.isValidUrl(url):
                continue
            ScrapyCrawler.domainUrls.append(CrawlerData(url, response.url, 'noFollow')) 
    
    def isFollowDocument(self, response):
        try:
            robots = response.css('meta[name="robots"]').css('::attr(content)').extract()
            robots = u' '.join(robots)
        except:
            robots = ''
        if 'nofollow' in robots:
            return False
        return True
    
    def isDisallowUri(self, url):
        for uri in ScrapyCrawler.disallowUris:
            if uri in url:
                return True
        return False
    
    def isValidUrl(self, url):
        for invalidString in ScrapyCrawler.invalid_strings:
            if invalidString in url:
                return False
        return True

class CrawlerData(object):
    
    def __init__(self, url, origin, linkType):
        self.url = url
        self.origin = origin
        self.linkType = linkType

def getDomainUrls(startUrl, allowedDomains, invalidStrings):
    pool = Urllib3PoolFactory.getPool()
    request = pool.request('GET', startUrl+'/robots.txt')
    
    disallowUris = []
    try:
        for line in request.data.split('\n'):
            if 'disallow' in line.lower():
                disallowUris.append(line.lower().split(':')[1].strip())
    except:
        pass

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_ENABLED' : True,
    })
    
    ScrapyCrawler.configure([startUrl], allowedDomains, invalidStrings, disallowUris)
    process.crawl(ScrapyCrawler)
    process.start()
    process.join()
    return ScrapyCrawler.domainUrls

if __name__ == '__main__':
    
    response = getDomainUrls('http://www.dinersclub.com.ec', ['dinersclub.com.ec'], ['discover', 'titanium', 'pichincha'])
    print(u'-'*50)
    print(u'-'*50)
    print(u'url,origen,tipo')
    for crawLerData in response:
        print (u'%s,%s,%s' % (crawLerData.url, crawLerData.origin, crawLerData.linkType))
    
