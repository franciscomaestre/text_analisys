#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 de jul. de 2016

'''
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory
from core.scraping.scraper import UserAgent

from selenium import webdriver


def main():
    
    url = u'http://www.animalclan.com/es/6310-collar-scalibor-oferta.html'
    
    browser = webdriver.PhantomJS()
    try:
        browser.set_page_load_timeout(10)
        browser.get(url)
        
        jQuery = '''
        var script = document.createElement('script'); 
        script.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js';
        script.type = 'text/javascript';
        document.getElementsByTagName('head')[0].appendChild(script);
        '''
        
        browser.execute_script(jQuery)
        
        print browser.is_displayed()
        
    except Exception, ex:
        print ex
    finally:
        browser.close()

def download(url):
    pool = Urllib3PoolFactory.getSameOriginPool()
    request = pool.request('GET', url,
                           headers={"User-Agent": UserAgent.chrome , "Accept" : "text/html" })
    
    return request.data

if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')

    main()
    
    
    
    