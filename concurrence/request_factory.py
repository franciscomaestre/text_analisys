#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from config import settings
import urllib3
from urllib3.util.retry import Retry
from utils.proxy_manager import ProxyManager

class RequestFactory(object):
    '''
    Es un pool de conexiones, no de procesos ni threads
    '''
    
    pool = {}
    sameDomainPool = {}
    
    @staticmethod
    def getPool():
        pid = os.getpid()
        if not pid in RequestFactory.pool:
            urllib3.disable_warnings() #@UndefinedVariable
            import requests
            session = requests.Session()
            session.max_redirects = 2
            RequestFactory.pool[pid] = session
        return RequestFactory.pool[pid]
    
    @staticmethod
    def getSameOriginPool():
        pid = os.getpid()
        if not pid in RequestFactory.sameDomainPool:
            urllib3.disable_warnings() #@UndefinedVariable
            import requests
            session = requests.Session()
            session.max_redirects = 2
            RequestFactory.sameDomainPool[pid] = session
        return RequestFactory.sameDomainPool[pid]
    
    @staticmethod
    def getProxyPool():
        urllib3.disable_warnings() #@UndefinedVariable

        nextProxy = ProxyManager.getNextProxy()
        
        if nextProxy.proxy_basic_auth:
            proxy_url = u'http://%s@%s:%s' % (nextProxy.proxy_basic_auth, nextProxy.host, nextProxy.port)
        else:
            proxy_url = u'http://%s:%s' % (nextProxy.host, nextProxy.port)
            
        proxies = {
          'http': proxy_url,
          'https': proxy_url,
        }
        
        import requests
        
        session = requests.Session()
        session.proxies = proxies
        session.max_redirects = 2
        
        return session
    

