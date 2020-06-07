#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.translation import ugettext as _

from utils.level import Level
from utils.code import Code
from seo.containers.ratings import TextAuditRating

DISPLAY = False
from utils.logger import LoggerFactory
app_logger = LoggerFactory.getInstance('app')


class CategoriesRating(object):
    RATING_NAME = u'CATEGORIES-SCORE-%s'
    
    def __init__(self, categoriesType, mainCategories, textCategories):
        self.mainCategories = mainCategories
        self.textCategories = textCategories
        self.name = CategoriesRating.RATING_NAME % categoriesType.upper()
        
    def getRating(self):
        scoreCategories = self._getScore()
        
        message = None
        level = Level.DANGER
        code = Code.UNDEFINED
        
        # message
        if scoreCategories < 50:
            message = _(u'Tu texto tiene poco contenido en común con los resultados arrojados por google')
            level = Level.DANGER
            code = Code.IMPROVE
        else:
            message = _(u'Tu texto habla sobre la materia')
            level = Level.SUCCESS
            code = Code.OK
                
        
        return TextAuditRating(
                      self.name, 
                      scoreCategories,
                      code,
                      level,
                      scoreCategories,
                      lowerLimit=0,
                      upperLimit=100,
                      message=message
                      )        
    
    def _getScore(self):
        commonCategories = (set(self.mainCategories.keys()) & set(self.textCategories.keys()))
        return int(len(commonCategories) * 100.00 /len(self.mainCategories))
        
