#!/usr/bin/python
# -- coding: utf-8 -*-

import re
#import math

from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory

from bs4 import BeautifulSoup
from bs4.element import NavigableString
from core.data_mining.web_pages.scraper import UserAgent
from core.data_mining.web_pages.scrapers.naive import cleanHtml, removeEmptyTags,\
    removeTags

# Si la clase del elemento o el id contiene algo parecido, no los procesamos
#UNLIKELY_CANDIDATES = re.compile(u".*combx.*|.*comment.*|.*community.*|.*disqus.*|.*extra.*|.*foot.*|.*header.*|.*menu.*|.*remark.*|.*rss.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*ad-break.*|.*agegate.*|.*pagination.*|.*pager.*|.*popup.*|.*tweet.*|.*twitter.*")
UNLIKELY_CANDIDATES = re.compile(u".*combx.*|.*comment.*|.*community.*|.*disqus.*|.*extra.*|.*foot.*|.*header.*|.*menu.*|.*remark.*|.*rss.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*ad-break.*|.*agegate.*|.*pagination.*|.*pager.*|.*popup.*|.*tweet.*|.*twitter.*")
##okMaybeItsACandidate = re.compile(u".*article.*|.* body.*|.* column.*|.* main.*|.* shadow.*")

# Solo partimos de este tipo de nodos para sacar el texto
NODES_TO_EXTRACT = ['p', 'td', 'pre' ]

TAGS_TO_P = [] #'h1','h2','h3','h4','h5','h6']

# Si un <div> no contiene estos elementos, lo juntamos todo en un <p>
DIV_TO_P_ELEMENTS = ['a', 'blockquote', 'dl', 'div', 'img', 'ol', 'p', 'pre', 'table', 'ul']  
DIV_TO_P_ELEMENTS.extend(TAGS_TO_P)

# Expresiones para calcular el peso de cada elemento
#NEGATIVE_REGEX = re.compile(u".*combx.*|.*comment.*|.*com-.*|.*contact.*|.*foot.*|.*footer.*|.*footnote.*|.*masthead.*|.*media.*|.*meta.*|.*outbrain.*|.*promo.*|.*related.*|.*scroll.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*shopping.*|.*tags.*|.*tool.*|.*widget.*")
NEGATIVE_REGEX = re.compile(u".*combx.*|.*comment.*|.*com-.*|.*contact.*|.*foot.*|.*footer.*|.*footnote.*|.*masthead.*|.*outbrain.*|.*promo.*|.*related.*|.*scroll.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*shopping.*|.*tags.*|.*tool.*|.*widget.*")
POSITIVE_REGEX = re.compile(u".*article.*|.*body.*|.*content.*|.*entry.*|.*hentry.*|.*main.*|.*page.*|.*pagination.*|.*post.*|.*text.*|.*blog.*|.*story.*")
HIDDEN_REGEX = re.compile(u".*display: *none.*|.*visibility: *none.*|.*visibility: *hidden.*|.*opacity: *0.*")
"""
style="display: none;"
visibility: hidden;
opacity: 0;
width: 0; height: 0;
"""

ENDPOINT_REGEX = re.compile("\.( |$)") 

MIN_NODE_CHARACTERS_LENGTH = 150  # characters
FIND_ONLY_MAIN_ARTICLE = False    # True --> extract main text and siblings
CHILDREN_FACTOR = 1.0             # peso que dan los hijos a los padres

def download(url):
    
    pool = Urllib3PoolFactory.getSameOriginPool()
    
    request = pool.request('GET', url,
                           headers={"User-Agent": UserAgent.chrome , "Accept" : "text/html" })
    
    return request.data

def processHtml(rawHtml):
    
    # Clean TEXT
    cleanedHtml = cleanHtml(rawHtml)  # remove br, dots
    
    soup = BeautifulSoup(cleanedHtml, 'lxml')
    
    removeEmptyTags(soup)
    removeTags(soup)  # comments, TAGS_TO_REMOVE (scrips, style ...)
    
    # ----------------------------------------
    #findHidden(soup)
    # ----------------------------------------
    
    ## convertNavigableToParagraph(soup)
    convertToParagraph(soup)
        
    # 1. ----------------------------------------  find candidates
    #   buscamos los nodos iniciales para obtener bloques NODES_TO_EXTRACT [p, td, pre]
    nodesToScore = []
    
    # borramos nodos con clases e ids en UNLIKELY_CANDIDATES
    for node in soup.body.find_all():
        
        tag_to_search = u' '.join(node.get('class', []))  + node.get('id', '')
        if UNLIKELY_CANDIDATES.match(tag_to_search):
            node.extract()

    # buscamos los nodos hijos de los que partimos
    div_to_p = []
    for node in soup.body.find_all():
        
        if node.name.lower() in NODES_TO_EXTRACT: 
            innerText = node.get_text(separator='', strip=True, types=[NavigableString])
            if len(innerText) < 25:
                continue
            nodesToScore.append(node)
    
        ## Turn all divs that don't have children block level elements into p's 
        if node.name.lower() == "div":
            if not node.find_all(DIV_TO_P_ELEMENTS):
                div_to_p.append(node)
                
    # convert div to p. Maintain attributes                
    for node in div_to_p:            
        innerText = node.get_text(separator='', strip=True, types=[NavigableString])
        if len(innerText) < 25:
            continue
        node.clear()  # remove children
        node.name = 'p'
        node.string = innerText
        """
        new_node = soup.new_tag('p')
        new_node.string = node.get_text(separator='', strip=True, types=[NavigableString])
        node.replace_with(new_node)
        """
        nodesToScore.append(node)
        
    # 2. ----------------------------------------  
    #   buscamos los padres y abuelos y les damos un peso inicial segun su longitud y las caracteristicas suyas y de sus hijos
    candidates = {}
    for node in nodesToScore:
        parentNode = node.parent
        grandParentNode = parentNode.parent if parentNode else None
        parent_key = HashableElement(parentNode)
        grand_parent_key = HashableElement(grandParentNode)
        
        if not parentNode:
            continue
        
        # Limite mínimo de caracteres del nodo
        innerText = node.get_text(separator='', strip=True, types=[NavigableString])
        if len(innerText) < 25:
            continue   
        
        # init parent node weigths
        if parent_key not in candidates:
            initializeNode(parentNode)
            candidates[parent_key] = parentNode

        # init grandParent node weigths
        if grandParentNode and grand_parent_key not in candidates:
            initializeNode(grandParentNode)
            candidates[grand_parent_key] = grandParentNode

        contentScore = 0
        # Add a point for the paragraph itself as a base. 
        contentScore += 1
        
        # Add points for any commas within this paragraph 
        contentScore += innerText.count(',') + innerText.count('.')
        
        # For every 100 characters in this paragraph, add another point. Up to 3 points. 
        contentScore += min(int(len(innerText) / 100), 3)
        
        # Add the score to the parent. The grandparent gets half. 
        candidates[parent_key].contentScore += contentScore;

        if grandParentNode:
            candidates[grand_parent_key].contentScore += contentScore/2             

    
    # 3. ----------------------------------------
    #    Modificamos los pesos con la densidad de links    
    for candidate in candidates.values():
        ##
        # Scale the final candidates score based on link density. Good content should have a
        # relatively small link density (5% or less) and be mostly unaffected by this operation.
        ##
        candidate.contentScore = candidate.contentScore * (1-getLinkDensity(candidate))
        
    # sort
    topCandidates = sorted(candidates.values(), key=lambda x: x.contentScore, reverse=True)
    
    if not topCandidates:
        raise Exception(u"No hay suficiente texto para procesar la página")
    
    # Quitamos dela lista ordenada de candidatos los que tienen un hijo o padres con mas puntos 
    # get top parents. dont add parents/children
    finalCandidates = []
    for topCandidate in topCandidates:
        add = True
        if topCandidate.contentScore < 10.0:
            add = False
        else:
            for candidate in finalCandidates:
                if topCandidate in candidate.findChildren():
                    add = False  # algun padre tiene mas puntos
                    break
                if candidate in topCandidate.findChildren():
                    add = False # algun hijo tiene mas puntos
                    break
            
        if add:
            finalCandidates.append(topCandidate)
    
    # 4. ----------------------------------------
    # Buscamos los hermanos de cada bloque.
    # Nos quedamos con el primer bloque y los demas si tienen un mínimo de datos(nodes_length/3) y puntos(contentScore/4)
    bestNodes = []
    min_length = MIN_NODE_CHARACTERS_LENGTH
    min_score = 0
    for index, topCandidate in enumerate(finalCandidates):
        foundNodes, nodes_length = getSiblings(topCandidate)
        
        # límites para añadir otros nodos 
        if index == 0:
            min_length = max(MIN_NODE_CHARACTERS_LENGTH, nodes_length/3)
            min_score = topCandidate.contentScore/4
        
        if index == 0 or nodes_length > min_length:
            if topCandidate.contentScore > min_score:
                bestNodes.extend(foundNodes)
            if FIND_ONLY_MAIN_ARTICLE:
                break

    for node in bestNodes:
        print node.contentScore
        text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
        print len(text)
        print text
   
    return bestNodes

def getSiblings(node):
    bestNodes = []
    nodes_length = 0
    
    siblingScoreThreshold = max(10, node.contentScore * 0.2)
    siblingNodes          = node.parent.find_all(recursive=False)    

    topCandidate_classNames = set(node.get('class', []))
    for sibling in siblingNodes:
        append = False
        
        if sibling == node:
            append = True
        else:
            contentBonus = 0
            # Give a bonus if sibling nodes and top candidates have the same classname 
            class_names = set(sibling.get('class', []))
            if class_names & topCandidate_classNames and topCandidate_classNames:
                contentBonus += node.contentScore * 0.2            
            
            if getattr(sibling, 'contentScore', None) and (sibling.contentScore+contentBonus >= siblingScoreThreshold):
                append = True
            
            if not append:
                if sibling.name.lower() == 'p':
                    linkDensity = getLinkDensity(sibling);
                    nodeContent = sibling.get_text(separator='', strip=True, types=[NavigableString])
                    nodeLength  = len(nodeContent)
                    
                    if nodeLength > 80 and linkDensity < 0.25:  # pocos links y test largo
                        append = True
                    elif nodeLength < 80 and linkDensity == 0 and ENDPOINT_REGEX.match(nodeContent):  # no hay links y hay puntos
                        append = True
        
        if append:
            bestNodes.append(sibling)
            text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
            nodes_length += len(text)

    return bestNodes, nodes_length

def initializeNode(node):
    node.contentScore = 0
    
    node_name = node.name.lower()
    if node_name == 'div':
        node.contentScore += 5
    elif node_name in ['pre', 'td', 'blockquote']:
        node.contentScore += 3    
    elif node_name in ['address', 'ol', 'ul', 'dl', 'dd', 'dt', 'li', 'form']:
        node.contentScore -= 3    
    #elif node_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'th']:
    elif node_name in ['th']:
        node.contentScore -= 5    

    node.contentScore += getClassWeight(node)
    
def getLinkDensity(node):
    if node.name == u'a':
        return 1.0
    
    link_length = len("".join([i.get_text(separator='', strip=True, types=[NavigableString]) or "" for i in node.findAll("a")]))
    text_length = len(node.get_text(separator='', strip=True, types=[NavigableString]))
    
    return float(link_length) / max(text_length, 1)   


def getClassWeight(node, recursive=True):
    weight = 0
    
    # Look for a special classname 
    node_class = unicode(node.get("class", u''))
    # Look for a special ID 
    node_id = unicode(node.get("id", u''))
    tag_to_search = u' '.join(node_class)  + node_id

    if tag_to_search.strip():
        if NEGATIVE_REGEX.match(tag_to_search):
            weight -= 25.0
        elif POSITIVE_REGEX.match(tag_to_search):
            weight += 25.0    
    
    # Look for hidden elements
    node_style = unicode(node.get('style', u''))
    if node_style:
        if HIDDEN_REGEX.match(node_style):
            weight -= 25.0
            
    # weight children
    if recursive:
        for child in node.find_all(recursive=False):
            children_weight = getClassWeight(child, recursive=True)
            weight += CHILDREN_FACTOR * children_weight
     
    return weight


class HashableElement():
    def __init__(self, node):
        self.node = node
        self._path = None

    def _get_path(self):
        if self._path is None:
            reverse_path = []
            node = self.node
            while node:
                node_id = (node.name, tuple(node.attrs), node.string)
                reverse_path.append(node_id)
                node = node.parent
            self._path = tuple(reverse_path)
        return self._path
    path = property(_get_path)

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, other):
        return self.path == other.path

    def __getattr__(self, name):
        return getattr(self.node, name)


def convertNavigableToParagraph(soup):
    for navigable in soup.findAll(text=lambda text:(isinstance(text, NavigableString)) and len(text.string.strip()) > 25):
        newTag = soup.new_tag('p')
        newTag.string = navigable.string
        navigable.replace_with(newTag)
            
        
def convertToParagraph(soup):
    if TAGS_TO_P:
        for tag in soup.find_all(TAGS_TO_P):
            tag.name = 'p'



# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
import itertools

def xpath_soup(element):
    """
    Generate xpath of soup element
    :param element: bs4 text or node
    :return: xpath as string
    """
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        """
        @type parent: bs4.element.Tag
        """
        previous = itertools.islice(parent.children, 0, parent.contents.index(child))
        xpath_tag = child.name
        xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
        components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


def findHidden(soup):

    hidden_length = 0
    hidden_elements = {}
    for tag in soup.find_all(HIDDEN_REGEX):

        if not tag.parent in hidden_elements:
            hidden_text = tag.get_text(separator='', strip=True, types=[NavigableString])
            hidden_text = u" ".join(hidden_text.strip())
            hidden_length += len(hidden_text)
            print u'%s %s' % (tag.name, tag.get_text(separator='', strip=True, types=[NavigableString])[:10])   

        hidden_elements[tag] = tag 

    return hidden_length
    

def _findHidden(url, nodes):
    from selenium import webdriver
    
    driver = webdriver.PhantomJS()
    try:
        driver.set_page_load_timeout(5)
        driver.get(url)
        
        body = driver.find_element_by_tag_name("body")
        children = body.find_elements_by_xpath(".//*")
        children_length =  len(children)
        hidden_elements = {}
        hidden_length = 0
        for index, child in enumerate(children):
            try:
                #if child.tag_name == u'h1':
                #print u'%s / %s' % (index, children_length)
                if child.tag_name not in [u'br', u'script', u'noscript', u'style', u'iframe'] and not child.is_displayed(): # and len(child.text) > 5:

                    parent = child.find_element_by_xpath("..")                    
                    if not parent in hidden_elements:
                        text_element = child.get_attribute('textContent').strip() #textContent / innerHTML
                        text_element = u" ".join(text_element.split())
                        length = len(text_element)
                        if length > 25:
                            hidden_length += length
                            print u'%10s %8s %s' %(child.tag_name, child.is_displayed(), text_element)  #textContent / innerHTML
                    hidden_elements[child] = child
            except:
                pass
            
        print 80*'-'
        print u'hidden_length: %s' % hidden_length
        print 80*'-'
            
        '''        
        for tag in nodes:
            xpath = xpath_soup(tag)
            try:
                element = driver.find_element_by_xpath(xpath)
                print u'%10s %s %s' %(element.is_displayed(), xpath, len(tag.get_text(separator='', strip=True, types=[NavigableString])))
                
                parent = tag.parent
                xpath = xpath_soup(parent)
                element = driver.find_element_by_xpath(xpath)
                print u'%10s %s %s ' %(element.is_displayed(), xpath, len(parent.get_text(separator='', strip=True, types=[NavigableString])))
                
                # chidren
                for child in tag.find_all():
                    xpath = xpath_soup(child)
                    element = driver.find_element_by_xpath(xpath)
                    is_displayed = element.is_displayed()
                    if not is_displayed:
                        print u'%10s %s %s %s' %(is_displayed, xpath, child, len(child.get_text(separator='', strip=True, types=[NavigableString])))
                
            except Exception, ex:
                print ex
        '''   
        
    except Exception, ex:
        print ex
    finally:
        driver.close()


findHiddenElementsJD = '''
function removeHiddenNodes(root) {
    var nodeIterator, node,
        hiddenNodes = [],
        i = 0;
    nodeIterator = document.createNodeIterator(root, NodeFilter.SHOW_ELEMENT, function(node) {
        var nodeName = node.nodeName.toLowerCase();
        if (nodeName === "script" || nodeName === "style" || nodeName === "noscript") {
            return NodeFilter.FILTER_REJECT;
        }
        if (node.offsetParent === void 0) {
            return NodeFilter.FILTER_ACCEPT;
        }
        var computedStyle = window.getComputedStyle(node, null);
        if (computedStyle.getPropertyValue("visibility") === "hidden" || computedStyle.getPropertyValue("display") === "none") {
            return NodeFilter.FILTER_ACCEPT;
        }
    });
    while ((node = nodeIterator.nextNode()) && ++i) {
        if (node.parentNode instanceof HTMLElement) {
            //node.parentNode.removeChild(node);
            hiddenNodes.push(node);
        }
    }
    console.log("%s nodes removed", i);
    return hiddenNodes
}

return removeHiddenNodes(document.body);

'''



# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    import os
    import sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "../"))
    os.environ.setdefault("SEOLOGIES_SETTINGS_MODULE", 'config.debug_settings')

    urls = [u'http://www.zooplus.es/shop/tienda_perros/pienso_perros/royal_canin_club_selection/royal_canin_special_club/56533',
            u'http://www.animalclan.com/es/16739-scalibor-65cm-royal-canin-club-adult-special-performance.html',
            
            u'http://www.elmundo.es',
            
            u'http://www.animalclan.com/es/15295-royal-canin-gatos-norweian-forest.html?%20search_query=norw&results=1',
            u'https://3acd-descargar.phpnuke.org/es/c09262/microsoft-office-2010',
            
            u'https://serps.com/library/',
           
            u'http://www.publico.es/sociedad/liberado-madrid-joven-al-padre.html',
            u'http://www.publico.es/',
            u'http://www.elmundo.es/',
            u'http://www.zooplus.es/shop/tienda_perros/pienso_perros/taste_of_the_wild/taste_of_the_wild_adult/409340',
            u'http://www.decathlon.es/zapatillas-de-running-hombre-kalenji-ekiden-one-gris--id_8351755.html',

            u'http://www.animalclan.com/es/6310-collar-scalibor-oferta.html',
            ]
    
    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'

    for url in urls[-1:]:
        print 80*'-'
        print url
        rawHtml = download(url)
        try:
            bestNodes = processHtml(rawHtml)
        except Exception, ex:
            print ex
        
        
        
        
        
        """
        htmlText = u"<html><head><meta charset='UTF-8' /></head><body>"
        htmlText += u'<div><strong><a href="%s">%s' % (url, url) + u'</a></strong></div><br/>'
        
        hidden_data = _findHidden(url, bestNodes)
        htmlText += u'<div> %s' % (hidden_data,) + u'</div><hr><br/><br/>'
        
        for node in bestNodes:
            #print node.contentScore
            xpath = xpath_soup(node)
            
            text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
            htmlText += u'<div style="color:blue; font-weight:bold; background-color:#ddd; text-align:center; padding: 10px 0px;"> Score: ' + u"%s  (%s)   [%s]" % (node.contentScore,len(text), xpath) + u'</div>'
            htmlText += u'<div>' + u"%s"%node + u'</div><hr>'
            
            #print len(text)
            #print text        
        htmlText += u'</body></html>'
        
        f=open(path, 'w')
        f.write(htmlText.encode('utf8'))
        f.close()
        webbrowser.open('file://' + path)
        """
