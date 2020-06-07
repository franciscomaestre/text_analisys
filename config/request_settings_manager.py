#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


class RequestSettingsManager(object):
    
    instances = {}
    
    @staticmethod
    def getSettings():
        pid = os.getpid()
        return RequestSettingsManager.instances.get(pid, RequestSettings())

    @staticmethod
    def setSettings(requestSettings):
        pid = os.getpid()
        if not pid in RequestSettingsManager.instances:
            RequestSettingsManager.instances[pid] = requestSettings

class RequestSettings(object):
    
    def __init__(self, rawRequest={}):
        for key, value in rawRequest.items():
            setattr(self, key, value)
            
