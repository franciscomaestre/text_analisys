#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep
import argparse


if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "./../../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')
    from config.request_settings_manager import RequestSettings, RequestSettingsManager
    
    extraSettings = {}
    
    parser = argparse.ArgumentParser(description='Seologies parameters.')
    parser.add_argument('--market', help='language-Country -- es-ES')
    parser.add_argument('--type', help='facebook/products/verticals')
    parser.add_argument('--interval', help='1-3')
    parser.add_argument('--processes', help='Num parallel process')
    parser.add_argument('--percentage', help='%% percentage [1-100]')
    parser.add_argument('--documents', help='Donwload documents (True/False)')
    parser.add_argument('--train', help='Train Model? (True/False)')
    args = parser.parse_args()
    
    language = 'es'
    country = 'ES'
    
    if args.market:
        parts = args.market.split('-')
        language = parts[0]
        country = parts[1]
    
    if args.type:
        extraSettings.update({'TRAINER_TREE_TYPE': args.type})
        
    if args.interval:
        parts = args.interval.split('-')
        extraSettings.update({'TRAINER_DOWNLOADER_INTERVAL': int(parts[0]), 'TRAINER_DOWNLOADER_PARTS': int(parts[1])})   
        
    if args.processes:
        extraSettings.update({'TRAINER_NUM_PROCESSES': int(args.processes)})   
        
    if args.documents:
        donwloadDocuments = True if args.documents.lower() == 'true' else False
        extraSettings.update({'TRAINER_DOWNLOAD_DOCUMENTS': donwloadDocuments})
        
    if args.percentage:
        percentage = int(args.percentage)/100.00
        extraSettings.update({'TRAINER_DOWNLOAD_PERCENTAGE': percentage})
        
    if args.train:
        trainModels = True if args.train.lower() == 'true' else False
        extraSettings.update({'TRAINER_TRAIN_MODEL': trainModels})
    
    extraSettings = RequestSettings(extraSettings)   
    RequestSettingsManager.setSettings(extraSettings)

    from core.nlp.classifier.trainer import cls
    cls.downloadContent(language, country)
