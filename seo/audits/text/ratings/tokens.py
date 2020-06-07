#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils.translation import ugettext as _

from nltk.probability import FreqDist
import math
from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating
from config import settings
from utils.median_distribution import getMedianDistributionInfo

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')

class TokenScoreRating(object):
    RATING_NAME = u'TERMS-SCORE'
    
    def __init__(self, lemma, textLemmas, referencedLemmas, fdistLemmas, useWdfIdf=True):
        self.lemma = lemma
        self.textLemmas = textLemmas
        self.referencedLemmas = referencedLemmas
        self.fdistLemmas = fdistLemmas
        self.useWdfIdf = useWdfIdf
        
        self.rawScore = 0
        self.lowerLimit = 1
        self.upperLimit = 0
        
    def getRating(self):
        termScore, lowerLimitScore = self._getScore()

        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        interval = 100.00 - lowerLimitScore
        
        if termScore < lowerLimitScore:
            message = _(u'Frecuencia muy baja')
            level = Level.DANGER
            code = Code.INCREASE
        elif termScore < lowerLimitScore + interval * 0.25:
            message = _(u'Frecuencia Aceptable')
            level = Level.ACCEPTABLE
            code = Code.OK
        elif termScore < lowerLimitScore + interval * 1.01:
            message = _(u'Frecuencia óptima')
            level = Level.SUCCESS
            code = Code.OK
        else:
            message = _(u'Frecuencia excesiva')
            level = Level.DANGER
            code = Code.OVERUSED        

    
        return TextAuditRating(
                      TokenScoreRating.RATING_NAME, 
                      termScore,
                      code,
                      level,
                      self.rawScore,
                      self.lowerLimit,
                      self.upperLimit,
                      message
                      )        
                            
        
        
    def _getScore(self):
        termFreq, lowerLimit, upperLimit = self._termInfo()
        termScore = termFreq * 100.00 / max(settings.MANDATORY_TOKEN_MIN_QUANTITY,(upperLimit))
        termScore = min(105, int(termScore * 100) / 100.0)
        if self.useWdfIdf:
            lowerLimitScore = max(1, lowerLimit)
        else:
            lowerLimitScore = 1

        return termScore, lowerLimitScore  

    
    def _termInfo(self):
        info = []
        rawInfo = []
        # lemma frec in referencedLemmas
        try:
            for bData in self.referencedLemmas:
                if self.lemma in bData:
                    fdist = FreqDist(bData)
                    freq = fdist[self.lemma]
                    rawInfo.append(freq)
                    lenTokenList = len(bData)
                    if self.useWdfIdf:
                        metric = math.log(freq * 1.0 + 1.0, 2) / math.log(lenTokenList + 1, 2)
                    else:
                        metric = freq
                    if DISPLAY:
                        app_logger.info(u'[%s] Apariciones: %s Len: %s Max: %s Metric: %s' % (self.lemma, fdist[self.lemma], len(bData), max(fdist.values()), metric))
                    info.append(metric)
        
            # lemma frec in textLemmas
            freq = self.fdistLemmas[self.lemma]
            
            _lowerLimit, _median, upperLimit = getMedianDistributionInfo(rawInfo)
            
            self.rawScore = int(freq)
            self.upperLimit = max(settings.MANDATORY_TOKEN_MIN_QUANTITY, int(upperLimit))
            
            lenTokenList = len(self.textLemmas)
            if self.useWdfIdf:
                termFreq = math.log(freq * 1.0 + 1.0, 2) / math.log(lenTokenList + 1, 2)
            else:
                termFreq = freq
            # referencedLemmas mean/sigma of lemma
            lowerLimit, _median, upperLimit = getMedianDistributionInfo(info)
            
            if not self.useWdfIdf:
                lowerLimit = math.ceil(lowerLimit)
                upperLimit = math.ceil(upperLimit)
                
            return termFreq, lowerLimit, upperLimit
        except Exception as ex:
            raise ex