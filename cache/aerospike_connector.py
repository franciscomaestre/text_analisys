#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
To clear a namespace:

    asinfo -v "set-config:context=namespace;id=seologies;set=nlp;set-delete=true;"

'''

import aerospike
import collections
from config import settings
# from config import AEROSPIKE_SERVER, AEROSPIKE_PORT, AEROSPIKE_NAMESPACE,\
#    AEROSPIKE_SPACE, AEROSPIKE_TIMEOUT
from utils.logger import LoggerFactory
    
app_logger = LoggerFactory.getInstance('app')

class AerospikeConnector(object):
    
    def __init__(self, host=settings.AEROSPIKE_SERVER, port=settings.AEROSPIKE_PORT, namespace=settings.AEROSPIKE_NAMESPACE, space=settings.AEROSPIKE_SPACE):
        self.host = host
        self.port = port
        self.namespace = namespace
        self.space = space
        self.config = {
          'hosts': [ (host, port) ],
          'policies': {
                'timeout': 2000,  # milliseconds
                'retry': 2
            }
        }
        self.client = None
        self.connect()
        print 'Estamos creando el AerospikeConnector'
        
    def connect(self):
        # Create a client and connect it to the cluster
        try:
            self.client = aerospike.client(self.config).connect()
        except Exception, e:
            print("failed to connect to the cluster with", self.config['hosts'])
            raise e
        
    def get(self, key):
        key = (self.namespace, self.space, key)
        
        try:
            (key, _metadata, record) = self.client.get(key)
            return convert(record)
        except Exception, e:
            # print e
            return {}
        
    def set(self, key, data,):
        # Records are addressable via a tuple of (namespace, set, key)
        aerospikeKey = (self.namespace, self.space, key)
        try:
            # Write a record
            self.client.put(aerospikeKey, data, meta={'ttl':settings.AEROSPIKE_TIMEOUT}, policy={'timeout': 1500})
        except Exception as e:
            app_logger.error(u"AerospikeConnector _set error: {0}".format(e))
            app_logger.error(aerospikeKey)
            '''
            try:
                if not self.client.is_connected() and retries > 0:
                    print u'Reintentamos.... %s' % (retries)
                    app_logger.error(u'Reintentamos.... %s' % (retries))
                    self.connect()
            except Exception as e:
                app_logger.error(u"AerospikeConnector _retry error: {0}".format(e))
            '''
                
        
def convert(data):
    if isinstance(data, basestring):
        try:
            return data.decode('utf8')
        except:
            return data
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
