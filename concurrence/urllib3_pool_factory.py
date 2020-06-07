#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from config import settings
import urllib3
from urllib3.util.retry import Retry
from utils.proxy_manager import ProxyManager

class Urllib3PoolFactory(object):
    '''
    Es un pool de conexiones, no de procesos ni threads
    '''
    
    pool = {}
    sameDomainPool = {}
    
    @staticmethod
    def getPool():
        pid = os.getpid()
        if not pid in Urllib3PoolFactory.pool:
            urllib3.disable_warnings() #@UndefinedVariable
            Urllib3PoolFactory.pool[pid] = urllib3.PoolManager(num_pools=settings.URL_POOL_SIZE,
                                                               timeout=urllib3.Timeout(connect=1.5, read=3.5),
                                                               retries=Retry(total=None, connect=1, read=1, redirect=2))
        return Urllib3PoolFactory.pool[pid]
    
    @staticmethod
    def getSameOriginPool():
        pid = os.getpid()
        if not pid in Urllib3PoolFactory.sameDomainPool:
            urllib3.disable_warnings() #@UndefinedVariable
            import requests
            session = requests.Session()
            session.max_redirects = 2
            Urllib3PoolFactory.pool[pid] = session
            Urllib3PoolFactory.sameDomainPool[pid] = urllib3.PoolManager(num_pools=settings.URL_POOL_SIZE,
                                                                         timeout=urllib3.Timeout(connect=1.0, read=4.5),
                                                                         retries=Retry(total=None, connect=2, read=2, redirect=2, backoff_factor=0.1))
        return Urllib3PoolFactory.sameDomainPool[pid]
    
    
    @staticmethod
    def getProxyPool():
        urllib3.disable_warnings() #@UndefinedVariable

        nextProxy = ProxyManager.getNextProxy()
        if nextProxy.proxy_basic_auth:
            headers = urllib3.make_headers(proxy_basic_auth=nextProxy.proxy_basic_auth)
        else:
            headers = None
        proxy_url = u'http://%s:%s' % (nextProxy.host, nextProxy.port)
        proxy = urllib3.ProxyManager(proxy_url, 
                                     proxy_headers=headers,
                                     retries=Retry(total=None, connect=2, read=2, redirect=2, backoff_factor=0.1))
        return proxy
    

