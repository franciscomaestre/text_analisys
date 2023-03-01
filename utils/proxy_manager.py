#!/usr/bin/python
# -*- coding: utf-8 -*-
    
import urllib3
import random
from config import settings    
from utils.persistence.file_storage_factory import FileStorageFactory
from multiprocessing import RLock
from utils.logger import LoggerFactory

app_logger = LoggerFactory.getInstance('proxy')

class ProxyBase(object):
    '''
    Base proy. Must implement:
        getProxies()
        _saveProxies()
    '''
    
    proxy_basic_auth=None
    COUNTER = 0
    SELECTED = 0
    LOCK = RLock()    
    
    def __init__(self):
        self.proxies = self.getProxies()
        self.recoverInvalidatedProxies() 
    
    def getNextProxy(self):
        with ProxyBase.LOCK:
            ProxyBase.SELECTED = random.randint(0, len(self.proxies)-1)
            selectedProxy = self.proxies[ProxyBase.SELECTED]
            ProxyBase.COUNTER += 1
            if ProxyBase.COUNTER >= len(self.proxies):
                ProxyBase.COUNTER = 0
            self.recoverInvalidatedProxies()
                
            if selectedProxy.status:
                return selectedProxy
            else:
                for proxy in self.proxies:
                    if proxy.status:
                        return self.getNextProxy()
            print(u'Proxies are dead')
            app_logger.info(u'Proxies are dead')
            raise Exception(u'Proxies are dead')    
    
    def getProxies(self):
        raise NotImplementedError

    def invalidateProxy(self):
        with ProxyBase.LOCK:
            selectedProxy = self.proxies[ProxyBase.SELECTED]
            selectedProxy.status = False
            selectedProxy.counter = ProxyBase.COUNTER
            self._saveProxies()

    def recoverInvalidatedProxies(self):
        #Calculamos cuantos proxies siguen con vida
        alive = 0
        for proxy in self.proxies:
            if proxy.status:
                alive+=1
        
        app_logger.info(u'PROXIES STATUS ---- UP: %s DOWN: %s ' % (alive, len(self.proxies)-alive))
        print(u'PROXIES STATUS ---- UP: %s DOWN: %s ' % (alive, len(self.proxies)-alive))
        
        #Resucitamos aquellos proxies que llevan mucho tiempo KO
        for proxy in self.proxies:
            if not proxy.status and (proxy.counter+ max(20, alive*5) < ProxyBase.COUNTER or ProxyBase.COUNTER == 0):
                proxy.status = True
                proxy.counter = 0
        
        #Cada N peticiones, reordenamos el vector
        if ProxyBase.COUNTER % len(self.proxies) == 0:
            app_logger.info(u'Desordenando los proxies')
            random.shuffle(self.proxies)

        self._saveProxies()
        
    def _saveProxies(self):
        raise NotImplementedError

        
class CompositeProxyManager(ProxyBase): 
    '''
    Composite proxy
    '''
    
    COUNTER = 0
    LOCK = RLock()    
    
    def __init__(self):
        self.proxies = []
        self.componentsList = []
        
    def add(self, proxyManager):
        self.componentsList.append(proxyManager)
        self.proxies.extend(proxyManager.proxies)

    def getProxies(self):
        return self.proxies

    def _saveProxies(self):
        for component in self.componentsList:
            component._saveProxies()

class ProxyBuyProxies(ProxyBase):
    '''
    http://api.buyproxies.org
    '''
    
    proxy_basic_auth='tocomocho:XXXXXXXXX'
    COUNTER = 0
    LOCK = RLock()
    
    PROXIES_ENDPOINT_TEMPLATE = 'http://api.buyproxies.org/?a=showProxies&pid=%s&key=56ec6ff221b4242e0c4c44a2b09fb881'
    PROXIES_PID_LIST = [
                        58376  # 100 semi 2046/07/01
                        ]
    
    CACHE_PATH = u'/proxy'
    
    def __init__(self):
        self.proxies = self.getProxies()
        self.recoverInvalidatedProxies() 
    
    def getProxies(self):
        fileStorage = FileStorageFactory.getFileStorage(ProxyBuyProxies.CACHE_PATH)
        key = u'_proxy'
        self.proxies = fileStorage.get(key)
        if not self.proxies or not settings.CACHE:  
            self.proxies = self._getProxies()
            random.shuffle(self.proxies)
            self._saveProxies()
        return self.proxies
    
    def _getProxies(self):
        print(u'Cargando proxies de BuyProxy')
        content = ''
        for pid in ProxyBuyProxies.PROXIES_PID_LIST:
            http = urllib3.PoolManager()
            r = http.request('GET', ProxyBuyProxies.PROXIES_ENDPOINT_TEMPLATE % pid)
            content += r.data
        proxies = []
        for line in content.splitlines():
            proxy = ProxyInfo(line.split(':')[0], 
                              line.split(':')[1],
                              proxy_basic_auth = ProxyBuyProxies.proxy_basic_auth)
            proxies.append(proxy)
        return proxies
    
    def _saveProxies(self):
        fileStorage = FileStorageFactory.getFileStorage(ProxyBuyProxies.CACHE_PATH)
        key = u'_proxy'
        fileStorage.set(key, self.proxies, timeout=24 * 60 * 60)
    
        
class ProxyInfo(object):
    '''
    proxy host/port/status/proxy_basic_auth
    '''
    def __init__(self, host, port = 55555, status = True, counter = 0, proxy_basic_auth=None):
        self.host = host
        self.port = port
        self.proxy_basic_auth = proxy_basic_auth
        self.status = status
        self.counter = counter
        
    def __repr__(self, *args, **kwargs):
        return u"Proxy: %-15s:%-4s  %s" %(self.host, self.port, self.status)
      

# -------------------------------------------------------------------------------
# Global manager
#ProxyManager = CompositeProxyManager()
#ProxyManager.add(ProxyBuyProxies())       # buyProxies
#ProxyManager.add(ProxyManagerFineProxy())  # fineProxy. rusos --> Quemados




# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------        
def main():
    
    proxyManager = ProxyManager
    
    for _i in range(0,100):
        print(proxyManager.getNextProxy())

if __name__ == '__main__':
    import os
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", "core.conf.debug_settings")
    
    main()
