#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, ssl
from urlparse import urlparse
from urllib2 import URLError

class HttpsProtocolResponses(object):
    
    AVAILABLE = u'AVAILABLE'
    
    NOT_AVAILABLE = u'NOT AVAILABLE'
    
    ERROR = u'SSL VERIFICATION FAILED'

class HttpsProtocolChecker():
    def __init__(self, url):
        self.url = url
        self.httpUrl = self._transformToHttpUrl(url)
        try:
            self.response = requests.get(self.httpUrl, timeout=3)
        except (URLError, ssl.CertificateError, ssl.SSLError, IOError) as ex:
            self.error = HttpsProtocolResponses.ERROR
        
    def isHttpsActive(self):
        if hasattr(self, 'error'):
            return self.error
        if hasattr(self, 'response'):
            responseUrl = self.response.url
            parsedUrl = urlparse(responseUrl)
            if not (parsedUrl.scheme == 'https'):
                return HttpsProtocolResponses.NOT_AVAILABLE
            return HttpsProtocolResponses.AVAILABLE
        
        return HttpsProtocolResponses.NOT_AVAILABLE
    
    def _transformToHttpUrl(self, url):
        parsedUrl = urlparse(url)
        
        if (parsedUrl.scheme == ''):
            return 'http://' + url
        elif (parsedUrl.scheme == 'https'):
            return url.replace('https://', 'http://', 1);
        else:
            return url

if __name__ == '__main__':
    
    urls = ['https://www.luciasecasa.com']                 #Is not Https                     | Result: Not Https
    urls.append('https://www.seologies.com/')              #Correct Https                    | Result: Https
    urls.append('https://revoked.grc.com/')                #Revoked certificate              | Result: Https
    urls.append('https://tv.eurosport.com/')               #The domain name does not match   | Result: Not Https
    urls.append('https://self-signed.badssl.com')          #Self-signed certificate          | Result: certificate verify failed
    urls.append('https://rc4.badssl.com/')                 #Outdated RC4 cipher              | Result: sslv3 alert handshake failure
    urls.append('https://dh480.badssl.com/')               #A weak Diffie-Hellman key        | Result: dh key too small
    urls.append('https://qvica1g3-e.quovadisglobal.com/')  #Expired certificate              | Result: Connection Timeout
    
    for url in urls:
        httpCheck = HttpsProtocolChecker(url)
        print u'%s --> %s' % (url, httpCheck.isHttpsActive())
