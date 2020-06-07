#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep


queryCounter = 0
totalQueries = 0
proxyErrors = []

def qetQueryData(query, language, country, googleHost=u'google.es'):
    from utils.proxy_manager import ProxyManager, ProxyBase
    from core.data_mining.search_engines.google.google_selenium_plus import GoogleSeleniumPlus
    
    global queryCounter, proxyErrors
    queryCounter+=1
    
    googleSeleniumPlus = GoogleSeleniumPlus(query, language, country, googleHost=googleHost)
    
    try:
        googleSeleniumPlus._search(0, visible=1)
    except Exception, ex:
        print u'%s  -- %s '%(query, ex)
        proxyErrors.append(ProxyManager.proxies[ProxyBase.COUNTER-1])
        return
    print u'%s de %s  ---  Last used %s' % (queryCounter, totalQueries, ProxyManager.proxies[ProxyBase.COUNTER-1])
    sleep(0.5)

if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')
    
    from utils.proxy_manager import ProxyManager
    
   
    queries_ES = [u'comprar cristales gafas', 
               u'alquilar piso', 
               u'vender casa', 
               u'comprar coche', 
               u'restaurantes en madrid', 
               u'visitar roma', 
               u'comprar camisetas', 
               u'juegos de rol', 
               u'liberar memoria', 
               u'comprar movil', 
               u'vender zapatillas', 
               u'comprar colchón', 
               u'estudiar a distancia',
               u'copiar en clase', 
               u'gobierno de españa', 
               u'rasberrypi 3', 
               u'actualizar windows', 
               u'alquiler casas rurales', 
               u'viajes de verano', 
               u'cita a ciegas', 
               u'escribir poesia'
               u'Cómo evitar los gases',
               u'Cómo evitar los gases',
                u'Cómo evitar la ansiedad',
                u'Cómo evitar la caida del cabello',
                u'Cómo evitar la eyaculación precoz',
                u'Cómo evitar roncar',
                u'Cómo evitar las agujetas',
                u'Cómo evitar la retencion de liquidos',
                u'Cómo evitar los celos',
                u'Cómo evitar ponerse rojo',
                u'Cómo evitar el mal aliento',
                u'Cómo ser feliz',
                u'Cómo ser modelo',
                u'Cómo ser guapa',
                u'Cómo ser popular',
                u'Cómo ser hacker',
                u'Cómo ser millonario',
                u'Cómo ser youtuber',
                u'Cómo ser mejor persona',
                u'Cómo ser buen comercial',
                u'Cómo ser más inteligente']
    
   

    queries_EN = [
               u'Harry Potter and the Cursed Child',
               u'buy a car',
               u'buy second hand smartphone',
               u'buy new tv',
               u'win lottery',
               u'how to make cookies',
               u'how to gain more money',
               u'Golden State warriors',
              u'Memorial Day',
              u'Doc Savage',
              u'restaurant in ny',
              u'restaurant in dallas',
              u'nascar',
              u'Chicken as food',
              u'Kobe Bryant',
              u'Stephen Curry',
              u'LeBron James',
              u'Madrid',
              u'New York City',
              u'Happy Birthday to You',
              u'Purple Rain',
              u'Let It Go',
              u'spanish translation google',
    ]
    


    multiplier = 4
    totalQueries = (len(queries_ES) + len(queries_EN)) * multiplier

    print 80*'-'
    print(u'TOTAL PROXIES: %s   TOTAL QUERIES: %s' % (len(ProxyManager.proxies), totalQueries))
    print 80*'-'

    for i in range(multiplier):
        for query in queries_ES:
            qetQueryData(query, 'es', 'ES', googleHost=u'google.es')
            
        for query in queries_EN:
            qetQueryData(query, 'en', 'EN', googleHost=u'google.com')


    print(80*'-')
    print(u'Proxies con ERROR')
    print(80*'-')
    for proxy in proxyErrors:
        print(u'%s' % proxy)    
    print(80*'-')
    print(80*'-')
        