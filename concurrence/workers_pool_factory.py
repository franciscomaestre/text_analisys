#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing.pool import Pool, ThreadPool
from multiprocessing import cpu_count
from config import settings
# from config import POOL_THREAD_MULTIPLIER, RABBIT_POOL_SIZE


class WorkersPoolFactory(object):
    
    CPU_COUNT = cpu_count()
    
    pool = None
    
    rabbit = None
    
    @staticmethod
    def getPool():
        if not WorkersPoolFactory.pool:
            WorkersPoolFactory.pool = Pool(processes=int(WorkersPoolFactory.CPU_COUNT * settings.POOL_THREAD_MULTIPLIER), 
                                           maxtasksperchild=settings.POOL_THREAD_MAX_TASK_PER_CHILD)
        return WorkersPoolFactory.pool
    
    @staticmethod
    def getThreadPool():
        if not WorkersPoolFactory.rabbit:
            WorkersPoolFactory.rabbit = ThreadPool(processes=int(settings.RABBIT_POOL_SIZE))
        return WorkersPoolFactory.rabbit
