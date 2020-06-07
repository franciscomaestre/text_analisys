#!/usr/bin/python
# -*- coding: utf-8 -*-

def getGoogleHost(country):
    if country == 'ES':
        googleHost = 'www.google.es'
    elif country == 'GB':
        googleHost = 'www.google.co.uk'
    elif country == 'EN':
        googleHost = 'www.google.com'
    elif country == 'US':
        googleHost = 'www.google.com'
    elif country == 'FR':
        googleHost = 'www.google.fr'
    elif country == 'IT':
        googleHost = 'www.google.it'
    elif country == 'DE':
        googleHost = 'www.google.de'
    elif country == 'PT':
        googleHost = 'www.google.pt'
    else:
        print ('We are not prepared yet for this country %s. Setting DEFAULT ' % country)
        googleHost = 'google.com'
    
    return googleHost
