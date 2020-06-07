#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 de jul. de 2016
'''
import re

from bs4 import Comment
from bs4.element import NavigableString
from core.data_mining.web_pages import scrapping_rules


class NotEnougthTextException(Exception):
    pass

class ScraperBase(object):
    def getFilteredText(self, rawHtml, returnText=True):
        """
        returnText=True:
            rules.SPLITTER.join(resultText), soup
        returnText=False:
            return bestNodes, soup
        """
        raise NotImplementedError

    def cleanHtml(self, rawHtml):
        ##rawHtml = re.sub(rules.REPLACE_BR_REGEX, "</p><p>", rawHtml)
        rawHtml = re.sub(scrapping_rules.REPLACE_BR_REGEX, ".", rawHtml)
        rawHtml = re.sub(scrapping_rules.REPLACE_DOT_REGEX, ". ", rawHtml)
        ###rawHtml = re.sub(re.compile("<script.*>.*</script>"), "", rawHtml)
        return rawHtml
    
    MAX_EMPTY_STEPS = 2
    def removeEmptyTags(self, soup):
        empty_tags = []
        parent_tags = []
        for tag in soup.find_all():
            if not tag.contents:
                if tag != soup.body:
                    empty_tags.append(tag)
                    parent_tags.append(tag.parent)
        [tag.extract() for tag in empty_tags]
        
        # second step
        self._removeEmptyTags(parent_tags, soup, step=0)

    def _removeEmptyTags(self, parent_tags, soup, step):
        
        step += 1
        if step > ScraperBase.MAX_EMPTY_STEPS:
            return
        
        empty_tags = []
        inner_parent_tags = []
        for tag in parent_tags:
            if not tag.contents:
                if tag != soup.body:
                    empty_tags.append(tag)
                    inner_parent_tags.append(tag.parent)
        [tag.extract() for tag in empty_tags]
        
        self._removeEmptyTags(inner_parent_tags, soup, step)
        
        

    def removeTags(self, soup):
        """
        Remove comments, small strings and TAGS_TO_REMOVE(scripts, styles ...)
        """
        
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]
        
        # los parrafos con link en medio puedne tener palabras o parentesis ... Solo quitamos retornos.
        [navigable.extract() for navigable in soup.findAll(text=lambda text:(isinstance(text, NavigableString)) and len(text.string.strip('\n\r')) <= 0)] # rules.MIN_EMPTY
        
        for tag in scrapping_rules.TAGS_TO_REMOVE:
            map(lambda x: x.extract(), soup.findAll(tag))
    
