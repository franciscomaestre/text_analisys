#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join, isdir
import os

paths = [
         '/var/cache/seologies/semCPC',
        '/var/cache/seologies/seoTerms',
        '/var/cache/seologies/dataDocument',
        '/var/cache/seologies/readabilityText',
        '/var/cache/seologies/scoredTerms',
        '/var/cache/seologies/classifierData',
        '/var/cache/seologies/detailedTerms',
        '/var/cache/seologies/bingRelated',
        '/var/cache/seologies/semRush',
        '/var/cache/seologies/proxy',
        '/var/cache/seologies/bingSuggestion',
        '/var/cache/seologies/bingSearch ',
        '/var/cache/seologies/spellChecker ',
        '/var/cache/seologies/relatedTerms',
        '/var/cache/seologies/queryDocumentsDownloaded',
        '/var/cache/seologies/seoDocument',
        '/var/cache/seologies/googleSearchEngine',
         ]

def ensureDir(dirPath):
    if not os.path.exists(dirPath):
        try:
            os.makedirs(dirPath, 0o700)
        except OSError as e:
            raise e
'''
for path in paths[0:4]:
    onlyDir = [f for f in listdir(path) if isdir(join(path, f))]
    totalFolders = len(onlyDir)
    for pathDir in onlyDir:
        print u'Carpetas restantes ... %s' % totalFolders
        totalFolders -= 1
        onlyfiles = [f for f in listdir(join(path, pathDir)) if isfile(join(path, pathDir, f))]
        total = len(onlyfiles)
        counter = 0
        for fileName in onlyfiles:
            os.rename(join(path, pathDir, fileName), join(path, fileName))
            if counter % 500 == 0:
                print u'Fichero %s de %s' % (counter, total)
            counter +=1
        os.rmdir(join(path, pathDir)) 

'''        
for path in paths:
    try:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        total = len(onlyfiles)
        counter = 0
        print u'Ficheros iniciales en %s --> %s ' % (path, total)
        results = {}
        for fileName in onlyfiles:
            dirPath = join(path, fileName[0:2], fileName[2:4])
            oldPath = join(path, fileName)
            newPath = join(dirPath, fileName)
            #print u'%s --> %s' % (oldPath, newPath)
            ensureDir(dirPath)
            os.rename(oldPath, newPath)
            results[dirPath] = fileName
            if counter % max(1,int(total*0.01)) == 0:
                print u'Porcentaje procesado... %s %%  (%s de %s)' % (int(counter*100.0/total), counter, total)
            counter +=1
        if results:
            print u'Cantidad de Paths %s ' % len(results)
            print u'Media Ficheros/Path %s ' % (total*1.0/len(results),)
    except Exception, ex:
        print ex
