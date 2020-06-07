#!/usr/bin/python
# -*- coding: utf-8 -*-

def getGoogleHost(country):
    if country == u'ES':
        googleHost = u'www.google.es'
    elif country == u'GB':
        googleHost = u'www.google.co.uk'
    elif country == u'EN':
        googleHost = u'www.google.com'
    elif country == u'US':
        googleHost = u'www.google.com'
    elif country == u'FR':
        googleHost = u'www.google.fr'
    elif country == u'IT':
        googleHost = u'www.google.it'
    elif country == u'DE':
        googleHost = u'www.google.de'
    elif country == u'PT':
        googleHost = u'www.google.pt'
    else:
        print (u'We are not prepared yet for this country %s. Setting DEFAULT ' % country)
        googleHost = u'google.com'
    
    return googleHost
