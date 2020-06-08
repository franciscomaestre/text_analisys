#!/usr/bin/python
# -*- coding: utf-8 -*-

from data_mining.seo_document_downloader import SeoDocumentDownloader
from utils.translator import TranslatorFactory
import random
from utils.persistence.file_storage_factory import FileStorageFactory
from config import settings
from data_mining.search_engines.google import getGoogleHost
from data_mining.search_engines.google.google_scraper import GoogleScraper
from utils.remain_timer import RemainTimer
from nlp.classifier.trainer.models.trainer_data import TrainerData
from multiprocessing.pool import ThreadPool
import gc

CLASSIFIER_DATA_PATH = '/trainerData'

def getData(topics, initLevel = settings.TRAINER_INIT_LEVEL, language='es', country='ES'):
    fileStorage = FileStorageFactory.getFileStorage(CLASSIFIER_DATA_PATH)
    key = 'trainerData_%s_%s_%s_%s_%s_%s_%s' % (
                                              language, 
                                              country, 
                                              initLevel, 
                                              settings.TRAINER_DOWNLOAD_PERCENTAGE, 
                                              settings.TRAINER_DOWNLOADER_INTERVAL, 
                                              settings.TRAINER_DOWNLOADER_PARTS,
                                              settings.TRAINER_TREE_TYPE
                                              )
    result = fileStorage.get(key)
    if not result or not settings.CACHE or not settings.TRAINER_DOWNLOAD_DOCUMENTS  or settings.SCRAPER_RELOAD_CONTENT:
        print('NO CACHE --- Generando trainer data... %s' % key)
        result = _getData(topics, initLevel, language, country)
        if settings.TRAINER_DOWNLOAD_DOCUMENTS:
            fileStorage.set(key, result)
    return result

def _getData(topics, initLevel, language, country):
    
    #Vamos a guardar datos estadísticos de cada categoría
    dataInfo = {}
    
    #Trainer data parts
    targetList = []
    documentList = []
    urlList = []
    
    _topics, _totalRequests, media2Download = _getRequestsInfo(topics)
    topicTranslated, totalRequests, media2Download = _getRequestsInfo(topics, min2Download=media2Download)
    
    if settings.TRAINER_DOWNLOAD_DOCUMENTS:
        remainTimer = RemainTimer(totalRequests, 'DOCUMENTOS %s-%s' % (country, language))
    else:    
        remainTimer = RemainTimer(totalRequests, 'GOOGLE %s-%s' % (country, language))
    
    for topic, content in topicTranslated.items():

        dataInfo[topic] = []

        lenPart= int(len(content)*1.0/settings.TRAINER_DOWNLOADER_PARTS)
        startInterval = (settings.TRAINER_DOWNLOADER_INTERVAL-1)*lenPart
        if settings.TRAINER_DOWNLOADER_PARTS == settings.TRAINER_DOWNLOADER_INTERVAL:
            endInterval = len(content)
        else:
            endInterval = startInterval + lenPart
            
        print('Intervalo a Descargar %s - %s' % (startInterval, endInterval))
        
        gc.collect() 
        downloadPool = ThreadPool(processes=settings.TRAINER_NUM_PROCESSES)
        processList = []    
        
        for topicQuery in content[startInterval:endInterval]:
            
            if len(content) > media2Download:
                downloadLimit = settings.TRAINER_DOWNLOAD_LIMIT
            else:
                downloadLimit = settings.TRAINER_DOWNLOAD_LIMIT+10
                
            if settings.TRAINER_DOWNLOAD_DOCUMENTS:
                process = downloadPool.apply_async(_getSeoDocuments, args=(topicQuery, language, country, downloadLimit))
            else:
                process = downloadPool.apply_async(_getGoogleLinks, args=(topicQuery, language, country, downloadLimit))
            
            processList.append(process)
        
        results = []        
        
        for process in processList:
            try:
                remainTimer.start()
                if settings.TRAINER_DOWNLOAD_DOCUMENTS:
                    results.extend(process.get(timeout=60))
                else:
                    process.get(timeout=60)
                remainTimer.stop()
            except:
                pass
        
        if len(results) > 10:
            for seoDocument in results:
                try:
                    #Eliminamos los documentos repetidos
                    if seoDocument.link not in dataInfo[topic]:
                        documentList.append(' '.join(seoDocument.getTextTokens(lemmatize=True)))
                        targetList.append(topic)
                        urlList.append(seoDocument.link)
                    dataInfo[topic].append(seoDocument.link)
                except Exception as ex:
                    print(ex)
            
        #Lo cerramos para que el garbage colector actue
        downloadPool.close()
        downloadPool.terminate()
        
    return TrainerData(initLevel, list(set(targetList)), urlList, documentList, targetList, language, country)

'''
Si el topic no contiene al menos minTopicSize palabras, entonces no lo usamos como query en solitario
para así evitar su dispersión
Alimentación, bebida y tabaco > Alimentos > Carne, marisco y huevos > Carne
   root = Alimentación, bebida y tabaco
     + parts[-1] = Carne  --> query= Carne Alimentación, bebida y tabaco
     + parts[-1] = Carne  --> query= Carne Carne, marisco y huevos
'''
def getTopicList(filename, initLevel=1, minTopicSize=4):
    topicList = {}
    with open(filename, 'r') as topicsFile:
        next(topicsFile, None)  # skip the headers 
        for row in topicsFile:
            try:
                row = row.encode('utf8')
                row = row.replace('\n', '')
                parts = row.split(' > ')
                if len(parts) > initLevel:
                    parts = parts[initLevel:]
                    root = parts[0].strip()
                    if root not in topicList:
                        topicList[root] = set()
                        topicList[root].add(root)
                    #Arte y ocio > Fiestas y celebraciones > Productos para fiestas > Sombreros para fiestas
                    # Root: Fiestas y celebraciones -- Nivel 1
                    index = 1
                    for part in parts[1:]:
                        part = part.strip()
                        topicList[root].add(part)
                        topicList[root].add(part)
                        for sIndex in range(max(0, index-2),index):
                            counter = 0
                            for p in parts[sIndex].split():
                                if p in part:
                                    counter +=1
                            if counter == 0:
                                topicList[root].add(parts[sIndex] + ' ' + part)
                        index += 1    
            except Exception as ex:
                print(ex)
                print('Error en %s' % row)
                continue
    return {topic:list(content) for topic, content in topicList.items() if len(content) > 3}


def getTopicHierarchy(topic, filename):
    parent = None
    children = []
    
    rootFound = False
    levelRoot = 0
    with open(filename, 'r') as topicsFile:
        # search root
        next(topicsFile, None)  # skip the headers 
        for row in topicsFile:
            row = row.encode('utf8')
            row = row.replace('\n', '')
            parts = row.split(' > ')
            finish = False
            for counter, part in enumerate(parts):
                if rootFound:
                    # find root
                    if len(parts) > levelRoot and parts[levelRoot].lower() == topic.lower():
                        # get children
                        children.append([parts[i] for i in range(levelRoot+1, len(parts)) ])
                    else:
                        finish = True
                    break    
                else:
                    # try find topic
                    root = part.strip()
                    if root.lower() == topic.lower():
                        rootFound = True
                        levelRoot = counter
                        parent = parts[counter-1] if counter-1 >= 0 else None
                        break
            
            if finish:
                break 
    
    return parent, topic, children


def _getRequestsInfo(topics, min2Download = 0):
    
    translator = TranslatorFactory.getTranslator()
    
    topics2Download = {}
    totalRequests = 0
    
    for topic, content in topics.items():
        random.seed(33)
        size = len(content)
        if size > settings.TRAINER_MIN_QUERIES_PER_TOPIC/settings.TRAINER_DOWNLOAD_PERCENTAGE:
            size = max(min2Download, int(len(content) * settings.TRAINER_DOWNLOAD_PERCENTAGE))
        size = min(len(content), size)
        
        randomList = random.sample(content, size)
        topics2Download[topic] = [translator.trans(query) for query in randomList]
        
        totalRequests += size
    
    media2Download = totalRequests/len(topics)
        
    return topics2Download, totalRequests, media2Download




def _getGoogleLinks(query, language, country, downloadLimit):
    try:
        print('Language: %s Country: %s Query: %s ' % (language, country, query))
        googleSearch = GoogleScraper(query,
                               language=language,
                               country=country,
                               googleHost=getGoogleHost(country),
                               max_results=downloadLimit)
        return googleSearch.search(True)
    except Exception as ex:
        print(ex)
        return []
    
def _getSeoDocuments(query, language, country, downloadLimit):
    try:
        return  SeoDocumentDownloader(query=query,
                                       language=language,
                                       country=country,
                                       downloadLimit=downloadLimit,
                                       sameOrigin=False
                                       ).getSeoDocuments() 
    except Exception as ex:
        print(ex)
        return []
                                   
if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    
    print(os.getcwd())
    sys.path.insert(0, os.path.join(PROJECT_ROOT, os.getcwd()+ "./../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')    
    
    filename = os.getcwd() + './../' + 'data/products/taxonomy.es-ES.txt'
    print(getTopicHierarchy('Transporte de bebés', filename))
