#!/usr/bin/python
# -*- coding: utf-8 -*-

class DomainGoogleRankingInfo(object):
    
    def __init__(self, domain, appearIn, notAppearIn):
        self.domain = domain
        self.appearIn = appearIn
        self.notAppearIn = notAppearIn
        import numpy as np
        if self.appearIn:
            rankings = [rankedUrl.rank for _query, rankedUrl in self.appearIn.items()]
            self.avgPos = int(np.mean(rankings))
            self.bestPos = min(rankings)
            self.worstPos = max(rankings)
        else:
            self.avgPos = None
            self.bestPos = None
            self.worstPos = None
        
    def getStats(self):
        return self.bestPos, self.avgPos, self.worstPos
    
    def getInfo(self):
        info = self.__dict__.copy()
        info['appearIn'] = {query:rankedUrl.getInfo() for query, rankedUrl in self.appearIn.items()}
        return info
    
    def __str__(self, *args, **kwargs):
        return u'Domain: %s Avg: %s Best: %s Worst: %s AppearIn: %s NotAppearIn: %s' % (self.domain, self.avgPos, self.bestPos, self.worstPos, len(self.appearIn), len(self.notAppearIn))


class GoogleRankedUrl(object):
    
    def __init__(self, url, rank):
        self.url = url
        self.rank = rank
        
    def getInfo(self):
        return self.__dict__