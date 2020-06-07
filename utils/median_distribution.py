#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def getMedianDistributionInfo(dataList):
    if not dataList:
        return 0, 0, 0
    median = np.median(dataList)
    lowerLimit = np.percentile(dataList, 12.5)
    upperLimit = np.percentile(dataList, 100)
    return lowerLimit, median, upperLimit