#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom import minidom
import urllib2

def getAlexaRanking(page):
    resultAlexa = {}
    urlXml = u'http://data.alexa.com/data?cli=10&dat=snbamz&url=' + page
    req = urllib2.Request(urlXml, headers={'User-Agent' : "Magic Browser"})
    fileXml = urllib2.urlopen(req)
    xmlDocument = minidom.parse(fileXml)
    itemsSD = xmlDocument.getElementsByTagName('SD')
    
    try:
        itemsPopularity = itemsSD[1].getElementsByTagName('POPULARITY')
        rankGlobalPosition = str(itemsPopularity[0].attributes['TEXT'].value)
        resultAlexa['globalPosition'] = rankGlobalPosition
    except:
        pass
    
    try:
        itemsCountry = itemsSD[1].getElementsByTagName('COUNTRY')
        nameCountry = str(itemsCountry[0].attributes['NAME'].value)
        rankNationalPosition = str(itemsCountry[0].attributes['RANK'].value)
        resultAlexa['nameCountry'] = nameCountry
        resultAlexa['nationalPosition'] = rankNationalPosition
    except:
        pass
    
    return resultAlexa
