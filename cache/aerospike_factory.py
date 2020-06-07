#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.cache.aerospike_connector import AerospikeConnector
from config import settings
# from config import AEROSPIKE_NAMESPACE, AEROSPIKE_SPACE


class AerospikeFactory(object):
    
    instances = {}
    
    @staticmethod
    def getInstance(namespace=settings.AEROSPIKE_NAMESPACE, space=settings.AEROSPIKE_SPACE):
        key = u'%s_%s' % (namespace, space)
        if not key in AerospikeFactory.instances:
            AerospikeFactory.instances[key] = AerospikeConnector(namespace=namespace, space=space)
        return AerospikeFactory.instances[key]
