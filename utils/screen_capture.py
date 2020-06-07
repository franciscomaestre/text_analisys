#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Requeriments: 
 - selenium
 - Pillow:  (PIL port)  --> pip install Pillow
                            sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev tcl8.5-dev tk8.5-dev
                        test: from PIL import Image
                        
    
    Selenium es un servidor al que se le hacen peticiones. Hacer una busqueda entre sus elementos es muuuuy lento.
    SEO y hidden elements: http://www.freshegg.co.uk/blog/technical-seo/google/how-does-google-treat-hidden-content                    
                         
"""

import base64
from PIL import Image
from selenium import webdriver
import cStringIO
from config import settings
import sys
from cache.file_storage import FileStorage
from cache.file_storage_factory import FileStorageFactory
import time

class ScreenCapture(object):
    
    CROP_WIDTH = 800
    CROP_HEIGHT = 600
    
    MIN_HIDDEN_LENGTH = 100
    SELENIUM_CACHE = u'/seleniumCache'
        
    def __init__(self, url, width=64, height=64, processSelenium=False):
        
        self.url = url
        self.width = width
        self.height = height
        self.processSelenium = processSelenium
        self.imageFileStorage = FileStorage(
                                              settings.SCREENCAPTURE_PATH,
                                              {
                                               'timeout':settings.STORAGE_CACHE_TIMEOUT,
                                               'compress':settings.STORAGE_CACHE_COMPRESS,
                                               'max_entries': sys.maxint,
                                               'cull_frequency': 10
                                               }
                                            )
    
    def snapshot(self):
        
        browser = None
        result = {}
        
        initTime = time.time()
        
        try:
            # ------------------------------------------------------
            key = u'%s.%s.%s' % (self.url,self.width,self.height)
            imageUrl = self.imageFileStorage.get(key)
            if not imageUrl:
                screen_path = self.imageFileStorage._key_to_file(key)
                screen_path = screen_path.replace('djcache', 'jpg')
                self.imageFileStorage._createSubFolder() # create cache subfolder
                
                ret, browser = self._snapshot(screen_path)
                if ret:
                    imageUrl = screen_path.replace(settings.SCREENCAPTURE_PATH, settings.SCREENCAPTURE_DOMAIN)
                    # store in cache
                    self.imageFileStorage.set(key, imageUrl)
                    
            # ------------------------------------------------------
            if self.processSelenium:
                fileStorage = FileStorageFactory.getFileStorage(ScreenCapture.SELENIUM_CACHE)
                key = u'seleniumCache_%s' % (self.url, )
                result = fileStorage.get(key)
                if not result or not settings.CACHE:
                    result, browser = self._processSelenium(browser)
                    fileStorage.set(key, result)
            
            elapsedTime = time.time() - initTime
            result.update({'imageUrl':imageUrl,
                           'elapsedTime':elapsedTime,})
            
        
            return result
        
        finally:
            if browser:
                browser.close()
    
             
    def _snapshot(self, screen_path):
        
        browser = webdriver.PhantomJS()
        try:
            browser.set_page_load_timeout(10)
            
            browser.set_window_size(ScreenCapture.CROP_WIDTH, ScreenCapture.CROP_HEIGHT)
            browser.get(self.url)
            
            img_base64 = browser.get_screenshot_as_base64()
            img = Image.open(cStringIO.StringIO(base64.decodestring(img_base64)))
            img = img.crop((0, 0, ScreenCapture.CROP_WIDTH, ScreenCapture.CROP_HEIGHT)) # defines crop points
            
            # resize
            size = self.width, self.height
            img.thumbnail(size, Image.ANTIALIAS)
            img.convert('RGB').save(screen_path, 'JPEG')
            
            '''
            # covert to base64
            _buffer = cStringIO.StringIO()
            img.save(_buffer, format="JPEG")
            img_str = base64.b64encode(_buffer.getvalue())
            
            return 'data:image/jpeg;base64,'+img_str
            '''
           
            return True, browser
        except:
            return False, browser
        #finally:
        #    browser.close()


        
    
    def _processSelenium(self, driver):
        """
        Muy lento. Cada llamada a is_displayed(), get_attribute() ... es una llamada al servidor web interno del driver.
        Para acelerarlo habría que integrar Chromium: https://github.com/cztomczak/cefpython.
        
        SEO y hidden elements: http://www.freshegg.co.uk/blog/technical-seo/google/how-does-google-treat-hidden-content
        """
        
        if not driver:
            driver = webdriver.PhantomJS()
            driver.set_page_load_timeout(10)
            driver.get(self.url)
            
        
        # Find hidden elements
        hidden_length = 0
        try:
            body = driver.find_element_by_tag_name("body")
            children = body.find_elements_by_xpath(".//*")
            #children_length =  len(children)
            hidden_elements = {}
            for index, child in enumerate(children):
                try:
                    #if child.tag_name == u'h1':
                    #print u'%s / %s' % (index, children_length)
                    if child.tag_name not in [u'br', u'script', u'noscript', u'style', u'iframe'] and not child.is_displayed(): # and len(child.text) > 5:
    
                        parent = child.find_element_by_xpath("..")                    
                        if not parent in hidden_elements:
                            text_element = child.get_attribute('textContent').strip() #textContent / innerHTML
                            text_element = u" ".join(text_element.split())
                            length = len(text_element)
                            if length > ScreenCapture.MIN_HIDDEN_LENGTH:
                                hidden_length += length
                                #print u'%10s %8s %s' %(child.tag_name, child.is_displayed(), text_element)  #textContent / innerHTML
                        hidden_elements[child] = child
                except:
                    pass

            """    
            print(80*'-')
            print u'hidden_length: %s' % hidden_length
            print(80*'-')
            """
        except:
            pass
        
        return {'hidden_length':hidden_length}, driver 

        

if __name__ == '__main__':
    screenCapture = ScreenCapture(u'http://www.animalclan.com/es/6310-collar-scalibor-oferta.html', width=305, height=165)
    result = screenCapture.snapshot()
    print(result)
    
    
    
    