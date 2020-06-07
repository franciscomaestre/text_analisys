#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


class RemainTimer(object):
    
    def __init__(self, totalRequests, requestType = u'REQUEST'):
        self.totalRequests = totalRequests
        self.totalTime = 0
        self.counter = 0
        self.startTime = 0
        self.requestType = requestType
    
    def start(self):
        self.startTime = time.time()
        
    def stop(self):
        elapsed = time.time() - self.startTime
        self.totalTime += elapsed
        self.counter += 1
        meanTime = self.totalTime * 1.0 / self.counter
        remainTime = int((self.totalRequests - self.counter) * meanTime)
        print u'%s de %s . %s -- Tiempo restante .... %s segundos' % (self.counter, self.totalRequests, self.requestType, remainTime)
    
    def reset(self):
        self.totalTime = 0
        self.counter = 0