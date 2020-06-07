#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import math
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4.element import NavigableString
from utils.logger import LoggerFactory
from data_mining.web_pages import scrapping_rules as rules
from data_mining.web_pages.scrapers.base import ScraperBase

SIGMA_MULTIPLIER = 1
SEPARATOR = ' '

app_logger = LoggerFactory.getInstance('SeoAppScrapper')


def cleanHtml(rawHtml):
    ##rawHtml = re.sub(rules.REPLACE_BR_REGEX, "</p><p>", rawHtml)
    rawHtml = re.sub(rules.REPLACE_DOT_REGEX, ". ", rawHtml)
    ###rawHtml = re.sub(re.compile("<script.*>.*</script>"), "", rawHtml)
    return rawHtml

def removeEmptyTags(soup):
    empty_tags = []
    for tag in soup.find_all():
        if not tag.contents:
            empty_tags.append(tag)
    [tag.extract() for tag in empty_tags]
    

def removeTags(soup):
    
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    
    [navigable.extract() for navigable in soup.findAll(text=lambda text:(isinstance(text, NavigableString)) and len(text.string.strip()) <= rules.MIN_EMPTY)]
    
    for tag in rules.TAGS_TO_REMOVE:
        map(lambda x: x.extract(), soup.findAll(tag))
            
def replaceTags(soup):
    
    for tag in soup.find_all(rules.TAGS_TO_REPLACE.keys()):
        tag.name = rules.TAGS_TO_REPLACE[tag.name]
        
def convertToPlainParagraph(soup):
    
    for tag in soup.find_all(rules.TAGS_TO_GET_CONTENT):
        ##tag.name = 'p' if tag.name == 'span' else tag.name
        tag.name = 'p'
        tag.string = tag.get_text(separator=' ', strip=True, types=[NavigableString])


def RemoveHiddenTags(soup):
    for tag in soup.find_all([], style=rules.REMOVE_DISPLAY_NONE_REGEX):
        tag.extract()
        
def removeLinks(soup):
    
    # add num links to parent
    
    elementsToRemove = []
    
    # los links finales se ponen en el padre
    for tag in soup.find_all('a'):
        if len(list(tag.parent.children)) == 1:
            tag.parent.replaceWithChildren()
    
    for tag in soup.find_all('a'):
        try:  
            if (tag.next_sibling and tag.next_sibling.name == 'a'):
                elementsToRemove.append(tag)
        except:
            pass
        try:
            if (tag.previous_sibling and tag.previous_sibling.name == 'a'):
                elementsToRemove.append(tag)
        except:
            pass

    for tag in elementsToRemove:
        tag.extract()
    
    # second step
    if elementsToRemove:
        removeEmptyTags(soup)
        removeLinks(soup)
        
def convertToPlainParagraphSplitted(soup):
    
    for tag in soup.find_all(rules.TAGS_TO_GET_CONTENT_SPLITTED):
        tag.name = 'p'
        tag.string = tag.get_text(separator=rules.SPLITTER, strip=True, types=[NavigableString])
        
        
def removeBodyHeader(soup):
    
    body = soup.body
    
    if body:
        header = soup.body.find('header', recursive=False)
    
        if header:
            header.extract()
    
def encapsulateNavigables(soup):
    # Convert div, article, section', header ... to <p></p>
    map(lambda tag: _encapsulateTag(soup, tag, 'p'), soup.findAll(rules.TAGS_TO_ENCAPSULATE_CHILDREN))
    
def _encapsulateTag(soup, tag, tagToConvert='p'):
    for child in tag.children:
        if isinstance(child, NavigableString):
            
            newTag = soup.new_tag(tagToConvert)
            newTag.string = child.string
            child.replace_with(newTag)
            
def removeSmallTags(soup):
    
    for p in soup.find_all('p'):
        if len(p.get_text(separator=' ', strip=True, types=[NavigableString])) < rules.MIN_WORD_LENGTH:
            p.extract()
            continue
        childrenLen = len(list(p.parent.children))
        if childrenLen <= 2 and len([child for child in p.parent.children if child.name == 'p']) == childrenLen:
            if (len(p.parent.get_text(separator=' ', strip=True, types=[NavigableString])) < childrenLen * rules.MIN_WORDS * rules.MIN_WORD_LENGTH):
                p.extract()
                
    for tag in soup.find_all(True):
        if len(tag.get_text(separator=' ', strip=True, types=[NavigableString])) < rules.MIN_WORD_LENGTH:
            tag.extract()



# ----------------------------------------------------------------------
def getLinkDensity(tag):
    
    if tag.name == 'a':
        return 1.0
    
    link_length = len("".join([i.get_text(separator='', strip=True, types=[NavigableString]) or "" for i in tag.findAll("a")]))
    text_length = len(tag.get_text(separator='', strip=True, types=[NavigableString]))
    
    return float(link_length) / max(text_length, 1)


def checkDensisity(node):
    candidates = {}

    density = getLinkDensity(node)
    if density < 1:
                
        children = node.find_all(recursive=False)
        found_candidate = False
        for cNode in children:
            children_candidates = checkDensisity(cNode)
            if children_candidates: 
                found_candidate = True
                candidates.update(children_candidates)
        if not found_candidate:    
            candidates[node] = density
    else:
        # remove node
        node.extract()

    return candidates
# ----------------------------------------------------------------------

def getSoupSimplified(rawHtml, DEBUG=False):
    
    try:
        cleanedHtml = cleanHtml(rawHtml)
    except Exception as e:
        cleanedHtml = rawHtml
        app_logger.error(e)
        app_logger.error('_error CleanHtml')
    
    soup = BeautifulSoup(cleanedHtml, 'lxml')
    
    # remove empty tags
    try:
        removeEmptyTags(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error RemoveEmptyTags')
    
    """
    """
    try:
        RemoveHiddenTags(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error RemoveHiddenTags')
    
    
    try:
        removeTags(soup) 
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error RemoveTags')
        
        
    
    # ---------------------------------------------------    
    checkDensisity(soup.body)        
    
    # ---------------------------------------------------    
        
    try:
        replaceTags(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error replaceTags')
        
    try:
        convertToPlainParagraph(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error convertToPLain')
    
    try:
        removeLinks(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error removeLinks')
    
    try:
        convertToPlainParagraphSplitted(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error convertToPLain')
        
    try:
        removeBodyHeader(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error removeBody')
    
    try:
        encapsulateNavigables(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error encapsulateNavigables')
        
    try:
        removeSmallTags(soup)
    except Exception as e:
        app_logger.error(e)
        app_logger.error('_error removeSmallTags')
    
    return soup


import numpy as np
def sigmoid(x):
    "Numerically-stable sigmoid function."
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    else:
        # if x is less than zero then z will be small, denom can't be
        # zero because it's 1+z.
        z = math.exp(x)
        return z / (1 + z)
    



class Naive(ScraperBase):
    
    def getFilteredText(self, rawHtml, returnText=True):
        
        soup = getSoupSimplified(rawHtml, True)
        soup = soup.body
        
        parents = []
        media = 0.0
        numElements = 0
        positiveRegex = re.compile('h[1-3]')
        
        for tag in soup.findAll(re.compile('(p|h[0-9])')):
            
            pLen = len(tag.get_text(separator='', strip=True, types=[NavigableString]))
            
            parent = tag.parent
            
            if (parent not in parents):
                parents.append(parent)
                parent.score = 0.0
                parent.childrenLen = []
                parent['marked'] = 1
                '''
                Si dos elementos son exactamente iguales falla ya que el segundo
                no tiene creado el childrenLen. Por ello, le añadimos el attr marked
                para que no sean idénticos
                '''
                
            if(positiveRegex.match(tag.name)):
                parent.score += 30.0
                
            if (parent.has_attr("class")):
                if (rules.NEGATIVE_REGEX.match(str(parent["class"]))):
                    parent.score -= 10.0
    
            if (parent.has_attr("id")):
                if (rules.NEGATIVE_REGEX.match(str(parent["id"]))):
                    parent.score -= 10.0
    
            parent.childrenLen.append(pLen)
                
            media += pLen
            numElements += 1
    
        # ----------------------------
        
        max_length = max([sum(parent.childrenLen) for parent in parents])    
        try:
            media /= numElements
        except:
            # print 'There are no parents selected. Not really good text!!'
            return ''
            
        mediaScore = 0.0
        
        if len(parents) == 0:
            # print 'No valid text inside Url'
            return ''
        
        for parent in parents:
            #parent.score += sum(parent.childrenLen) / media
            
            ## damos mas importancia a los pesos negativos/positivos que a la longitud 
            parent.score = sigmoid(parent.score)
            parent.score += sum(parent.childrenLen)*0.10 / max_length
            
            mediaScore += parent.score
        
        mediaScore /= len(parents)
        
        # median
        scores = [p.score for p in parents]
        #print u"median : %s" % np.median(scores)
        percentil = np.percentile(scores, 40)
        #print u"percentile 30 : %s" % percentil
        filteredBestBlocks = [p for p in parents if p.score > percentil]
        
        if returnText:
            resultText = [block.get_text(separator=rules.SPLITTER, strip=True, types=[NavigableString]) for block in filteredBestBlocks]
            return rules.SPLITTER.join(resultText)
        else:
            return filteredBestBlocks
        
        # ---------------------------------------------------------------------------
        # --- ORIGINAL
               
        sigma = 0.0
        
        for parent in parents:
            sigma += (parent.score - mediaScore) * (parent.score - mediaScore)
        
        sigma /= len(parents)
            
        sigma = math.sqrt(sigma)
        
        threshold = max(1.0, mediaScore - SIGMA_MULTIPLIER * sigma)
        
        bestBlocks = [block for block in parents if block.score >= threshold]
        
        filteredBestBlocks = [block for block in bestBlocks if not (set(block.parents) & set(bestBlocks))]
        
        '''
        for block in filteredBestBlocks:
            print(block.score)
            print(block.get_text(separator = SEPARATOR, strip = True, types=[NavigableString]))
            print('-'*40)
        '''
        
        if returnText:
            resultText = [block.get_text(separator=rules.SPLITTER, strip=True, types=[NavigableString]) for block in filteredBestBlocks]
            return rules.SPLITTER.join(resultText), soup
        else:
            return filteredBestBlocks, soup
    

if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')

    urls = ['http://www.zooplus.es/shop/tienda_perros/pienso_perros/royal_canin_club_selection/royal_canin_special_club/56533',
            'http://www.elmundo.es',          
            ]
    
    def download(url):
        from concurrence.urllib3_pool_factory import Urllib3PoolFactory    
        pool = Urllib3PoolFactory.getSameOriginPool()
        from data_mining.web_pages.scraper import UserAgent
        request = pool.request('GET', url,
                               headers={"User-Agent": UserAgent.chrome , "Accept" : "text/html" })
        return request.data    
    
    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'

    scrapingFilter = Naive()

    for url in urls[-1:]:
        print(80*'-')
        print(url)
        rawHtml = download(url)
        try:
            bestNodes = scrapingFilter.getFilteredText(rawHtml, returnText=False)
        except Exception as ex:
            print(ex)
        
        htmlText = u"<html><head><meta charset='UTF-8' /></head><body>"
        htmlText += '<div><strong><a href="%s">%s' % (url, url) + '</a></strong></div><hr><br/><br/>'
        for node in bestNodes:
            #print node.contentScore
            text = node.get_text(separator=' ', strip=True, types=[NavigableString])
            htmlText += '<div style="color:blue; font-weight:bold; background-color:#ddd; text-align:center; padding: 10px 0px;"> Score: ' + u"%s  (%s)" % (node.contentScore,len(text)) + '</div>'
            htmlText += '<div>' + u"%s"%node + '</div><hr>'
            #print len(text)
            #print text        
        htmlText += '</body></html>'
        
        f=open(path, 'w')
        f.write(htmlText.encode('utf8'))
        f.close()
        webbrowser.open('file://' + path)
        


