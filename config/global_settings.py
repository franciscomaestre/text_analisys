#!/usr/bin/python
# -*- coding: utf-8 -*-

DEBUG = False
CACHE = True

SCRAPER_RELOAD_CONTENT = False

LOCAL_CPUS = []

#------------  Scrapper Options

DOWNLOADER_SEARCH_ENGINE = 'google'
DOCUMENT_MIN_CHARACTERS = 250
DOCUMENT_WORD_MIN_LEN = 3
FORBIDDEN_URLS = '\.pdf$|\.txt$|\.xml|\.youtube\.|\.youtu\.be'


GOOGLE_SCRAPER_PROBABILITY = 100  # Percent probability [0-100]
GOOGLE_SCRAPER_RETRIES = 10

#------------ Term Discovery

SEO_TERMS_DOWNLOADER_TIMEOUT = 4
SEO_TERMS_DOWNLOAD_LIMIT = 30
SEO_TERMS_DOWNLOAD_LIMIT_LESS_PRECISION = 20
SEO_TERMS_LOWER_LIMIT = 0.40

#------------ Text Audit

TEXT_AUDIT_DOWNLOAD_LIMIT = 20

#------------ Web Audit

WEB_AUDIT_DOWNLOAD_LIMIT = 10
WEB_AUDIT_MAX_DOMAINS = 5

#------------ Site Audit

SITE_AUDIT_DOWNLOAD_LIMIT = 400
SITE_AUDIT_LDA_DOCUMENT_LIMIT = 200
SITE_AUDIT_MIN_DOCUMENT_LENGTH = 40
SITE_AUDIT_NUM_TOPICS = 4  # 8
SITE_AUDIT_NUM_WORDS_PER_TOPIC = 20
SITE_AUDIT_MIN_TOPIC_SIZE = 2
SITE_AUDIT_LAMBDA = 0.7
SITE_AUDIT_DISPLAY = True


BETTER_HEADLINES_LIMIT = 100

#------------ Relevants

RELEVANTS_DOWNLOAD_LIMITS = 25
RELEVANTS_DOWNLOAD_LIMITS_LESS_PRECISION = 20
RELEVANTS_NUM_QUERIES = 6

#------------  SEM CPC

CPC_MAX_SEARCH = 2
CPC_REQUEST_LIMIT = 2
CPC_MAX_SIGMA = 3
CPC_MIN_RESULTS = 5

#------------Detailed (Información de cada Proof Term)

DETAILED_LIMIT = 5
DETAILED_WORD_LENGTH = 20
DETAILED_WORD_LIMIT = 3
CONTEXT_LIMIT = 5
CONTEXT_LIMIT_MIN = 3

#------------Mandatory (Magnets and Mandatory)

MANDATORY_LOWER_LIMIT = .20
MANDATORY_DOCUMENTS_LIMIT = 20
MANDATORY_MOST_COMMON_LIMIT = 15
MANDATORY_TOKEN_QUANTITY_LOWER_LIMIT = 2
MANDATORY_TOKEN_MIN_QUANTITY = 3

#------------ Classifier

CLASSIFIER_MODELS_PATH = u'/var/seologies/models'
CLASSIFIER_ENABLED = True
CLASSIFIER_DOCUMENTS_LIMIT = 20

TRAINER_DOWNLOADER_INTERVAL = 1
TRAINER_DOWNLOADER_PARTS = 1
TRAINER_DOWNLOAD_DOCUMENTS = True
TRAINER_NUM_PROCESSES = 1
TRAINER_DOWNLOAD_PERCENTAGE = 0.45
TRAINER_INIT_LEVEL = 1
TRAINER_DOWNLOAD_LIMIT = 20
TRAINER_MIN_QUERIES_PER_TOPIC = 30
TRAINER_TRAIN_MODEL = True
TRAINER_TREE_TYPE = 'products'

#------------ScreenCapture

SCREENCAPTURE_TEXTAUDIT_WIDTH = 305
SCREENCAPTURE_TEXTAUDIT_HEIGHT = 165
SCREENCAPTURE_PATH = u'/var/seologies/snapshot'
SCREENCAPTURE_DOMAIN = u'http://backend-api.seologies.com/snapshot'

#------------Logger

LOG_BASE_PATH = u'/var/log/seologies'

#------------API's

SEMRUSH_KEY = '953b6de2a5049e4b6b9b4835e87db81f'
SEMRUSH_CPC_LOWER_LIMIT = 0.05
SEMRUSH_CO_LOWER_LIMIT = 0.8
SEMRUSH_REAL_IP = '2.137.231.57'
SEMRUSH_TIMEOUT = 3.5
SEMRUSH_DISPLAY_LIMIT = 15

GREPWORD_API_KEY = '97eabb51032ee99'
GREPWORD_CMP_LOWER_LIMIT = 0.75
GREPWORD_MAX_STEPS = 10

GOOGLE_SEARCH_ENGINE_ID = '017084139525212023454:nw96h6_bekw'
GOOGLE_SEOLOGIES_API_KEY = 'AIzaSyDSkuYnwEXExo66jz1mvccbcV5ppF7OVb4'

BING_API_KEY = 'RP8APwlYcRwq9vgqE/Sq5sQ4YOIQx2UoNcdG5df95GM'
BING_AUTOSUGGEST_KEY = 'a8708ba62c45409c9a835a16942baf04'
BING_SPELLCHECKER_KEY = '3b30164c8bc141db94c686c1528cfc1c'

# https://datamarket.azure.com/dataset/explore/8818f55e-2fe5-4ce3-a617-0b8ba8419f65
BING_SEARCH_KEY = 'RP8APwlYcRwq9vgqE/Sq5sQ4YOIQx2UoNcdG5df95GM'
# https://datamarket.azure.com/dataset/amla/text-analytics#terms

# GOOGLE_SEOLOGIES_API_KEY = 'AIzaSyA6heELIVh6A_ioVwiinD8azA7P7b4023E'
# GOOGLE_SEARCH_ENGINE_ID = '011936815388225308440:ciabnvwdmsk'

PLAGTRACKER_USER = 'francisco.maestre.movil@gmail.com'
PLAGTRACKER_KEY = 'Eiveik8Oopjoosie1aeTh'

COPYSCAPE_USER = 'bibado'
COPYSCAPE_KEY = 'j5sjlrdryj4dttp6'
COPYSCAPE_USER = 'whaka'
COPYSCAPE_KEY = 'j7wlkmmyqko5n4rg'
COPYSCAPE_CACHE_TIMEOUT = 10*60

#------------System

POOL_THREAD_MULTIPLIER = 0.6  # cpu_cores * POOL_THREAD_MULTIPLIER will be the size of the pool
POOL_THREAD_MAX_TASK_PER_CHILD = 200  # maxtasksperchild is the number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process
URL_POOL_SIZE = SEO_TERMS_DOWNLOAD_LIMIT
POOL_THREAD_SCRAPER_TIMEOUT = 20

STORAGE_CACHE_PATH = '/var/cache/seologies'
STORAGE_CACHE_TIMEOUT = 90 * 24 * 60 * 60
STORAGE_CACHE_COMPRESS = True

MEMCACHED_SERVER = '127.0.0.1:11211'
MEMCACHED_TIMEOUT = 6 * 60 * 60
MEMCACHED_SPACE = 'python'

RABBIT_POOL_SIZE = 2
RABBIT_HOST = 'localhost'
RABBIT_USER = 'seologiesBackend'
RABBIT_PASSWORD = 'th245yura'
