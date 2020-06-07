#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 26 de jul. de 2016

'''

import re,base64,mimetypes,urlparse
from bs4 import BeautifulSoup
from core.data_mining.web_pages.scraper import Scraper


#feedparse has a _kick ass_ charset detection function!
#import feedparser

def is_remote(address):
    return urlparse.urlparse(address)[0] in ('http','https')

def data_encode_image(name,content):
    print("%s %s" %(name, mimetypes.guess_type(name)[0]))
    return u'data:%s;base64,%s' % (mimetypes.guess_type(name)[0],base64.standard_b64encode(content))

def ignore_url(address):
    url_blacklist = ('getsatisfaction.com',
                     'google-analytics.com',)

    for bli in url_blacklist:
        if address.find(bli) != -1:
            return True

    return False

def get_content(from_,expect_binary=False):
    try:
        googleScraper = Scraper(from_, sameOrigin=True)
        dataDocument = googleScraper.getDataDocument()
        return dataDocument.rawHtml
    except Exception, ex:
        print u'%s  %s' % (from_, ex)
        return u''

def resolve_path(base,target):

    if True:
        return urlparse.urljoin(base,target)

    if is_remote(target):
        return target

    if target.startswith('/'):
        if is_remote(base):
            protocol,rest = base.split('://')
            return '%s://%s%s' % (protocol,rest.split('/')[0],target)
        else:
            return target
    else:
        try:
            base,rest = base.rsplit('/',1)
            return '%s/%s' % (base, target)
        except ValueError:
            return target


def replaceJavascript(base_url,soup):

    for js in soup.findAll('script',{'src':re.compile('.+')}):
        try:
            real_js = get_content(resolve_path(base_url,js['src']))
            
            script = soup.new_tag('script', type="text/javascript")
            script.string = real_js if real_js else ''
            js.replaceWith(script)
            
            #js.replaceWith(u'<script>%s</script>' % real_js)
        except Exception,e:
            print 'failed to load javascript from %s' % js['src']
            print e
            #js.replaceWith('<!-- failed to load javascript from %s -->' % js['src'])


css_url = re.compile(ur'url\((.+?\))')
def replaceCss(base_url,soup):

    for css in soup.findAll('link',{'rel':'stylesheet','href':re.compile('.+')}):
        try:
            real_css = get_content(resolve_path(base_url,css['href']))

            def replacer(result):
                try:
                    found_img_path = result.groups()[0][:-1].strip("';")
                    if u'data:image' in found_img_path:
                        return found_img_path
                    
                    path = resolve_path(resolve_path(base_url,css['href']),found_img_path)
                    return u'url(%s)' % data_encode_image(path,get_content(path,True))
                except Exception,e:
                    print e
                    return u''

            style = soup.new_tag('style', type='text/css')
            new_style_string = re.sub(css_url,replacer,real_css)
            style.string = new_style_string 
            css.replaceWith(style)
            #css.replaceWith(u'<style>%s</style>' % re.sub(css_url,replacer,real_css))

        except Exception,e:
            print 'failed to load css from %s' % css['href']
            print e
            #css.replaceWith('<!-- failed to load css from %s -->' % css['href'])


def replaceImages(base_url,soup):

    from itertools import chain

    for img in chain(soup.findAll('img',{'src':re.compile('.+')}),
                     soup.findAll('input',{'type':'image','src':re.compile('.+')})):
        try:
            path = resolve_path(base_url,img['src'])
            real_img = get_content(path,True)
            img['src'] = data_encode_image(path,real_img)
        except Exception,e:
            print 'failed to load image from %s' % img['src']
            print e
            #img.replaceWith('<!-- failed to load image from %s -->' % img['src'])



def get_local_web(url, bs):
    replaceJavascript(url,bs)
    replaceCss(url,bs)
    replaceImages(url,bs)

    return bs

def main(url):
    bs = BeautifulSoup(get_content(url), "lxml")

    replaceJavascript(url,bs)
    replaceCss(url,bs)
    replaceImages(url,bs)


    # --------------------------------------------------------------------------------------------
    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'
    htmlText = unicode(bs)


    f=open(path, 'w')
    f.write(htmlText.encode('utf8'))
    f.close()
    webbrowser.open('file://' + path)


if __name__ == '__main__':
    url = u'https://es.wikipedia.org/wiki/Adolf_Hitler'    
    
    main(url)
    
    