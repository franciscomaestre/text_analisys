#!/usr/bin/python
# -*- coding: utf-8 -*-

"File-based cache backend"

from utils.persistence.utils.memcached import MemcachedCache

from config import settings
import sys
# from config import MEMCACHED_SERVER,MEMCACHED_TIMEOUT, MEMCACHED_SPACE

class MemcachedFactory(object):
    
    instances = {}
          
    @staticmethod
    def getInstance(space=settings.MEMCACHED_SPACE):
        if not space in MemcachedFactory.instances:
            MemcachedFactory.instances[space] = MemcachedCache(settings.MEMCACHED_SERVER, params={
                                                                                                  'timeout':settings.MEMCACHED_TIMEOUT,
                                                                                                  'max_entries': sys.maxint,
                                                                                                  'cull_frequency': 10
                                                                                                  }, space=space)
        return MemcachedFactory.instances[space]
    
