#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 de jul. de 2016

1. Se limpia el texto y se quitan tags vacios
   Se suprimen tags de UNLIKELY_CANDIDATES. Es muy restrictivo. TODO: ahora no se eliminan clases con foot/header
   
2. Se buscan los NODES_TO_EXTRACT = ['p', 'td', 'pre' ]
3. Se transforman DIV_TO_P_ELEMENTS = ['a', 'blockquote', 'dl', 'div', 'img', 'ol', 'p', 'pre', 'table', 'ul']
4. Se buscan textos sueltos y si su padre tiene mas de 100 caracteres se añaden como <p> 

5. De todos estos nodos candidatos, se guardan sus padres añadiendo la puntuación de estos nodos encontrados (segun longitud y espacios)
6. De todos estos nodos candidatos, se guardan sus abuelos añadiendo la mitad puntuación de estos nodos encontrados
7. Se modifican los puntos con la densidad de links
8. Quitamos de la lista ordenada de candidatos los que tienen un hijo o padres con mas puntos (no dejamos nodos anidados)

9. De los nodos candidatos, buscamos los hermanos puntuando según la clase css y el nombre del id.
   Añadimos el nodo candidato y sus hermanos si tiene suficientes puntos.
   
10. Nos quedamos con el mejor candidato y los demas si tienen un mínimo de datos(nodes_length/3) y puntos(contentScore/4)

'''
import re
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from data_mining.web_pages.scrapers.base import ScraperBase,\
    NotEnougthTextException
from data_mining.web_pages import scrapping_rules


# Si la clase del elemento o el id contiene algo parecido, no los procesamos
#UNLIKELY_CANDIDATES = re.compile(u".*combx.*|.*comment.*|.*community.*|.*disqus.*|.*extra.*|.*foot.*|.*header.*|.*menu.*|.*remark.*|.*rss.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*ad-break.*|.*agegate.*|.*pagination.*|.*pager.*|.*popup.*|.*tweet.*|.*twitter.*")
#UNLIKELY_CANDIDATES = re.compile(u".*cookie.*|.*combx.*|.*comment.*|.*community.*|.*disqus.*|.*extra.*|.*foot.*|.*header.*|.*menu.*|.*remark.*|.*rss.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*ad-break.*|.*agegate.*|.*pagination.*|.*pager.*|.*popup.*|.*tweet.*|.*twitter.*")
UNLIKELY_CANDIDATES = re.compile(u".*cookie.*|.*combx.*|.*comment.*|.*community.*|.*disqus.*|.*extra.*|.*menu.*|.*remark.*|.*rss.*|.*shoutbox.*|.*estoeraelsidebar.*|.*sponsor.*|.*ad-break.*|.*agegate.*|.*pagination.*|.*pager.*|.*popup.*|.*tweet.*|.*twitter.*")
##okMaybeItsACandidate = re.compile(u".*article.*|.* body.*|.* column.*|.* main.*|.* shadow.*")

# Solo partimos de este tipo de nodos para sacar el texto
NODES_TO_EXTRACT = ['p', 'td', 'pre' ]

TAGS_TO_P = ['h1','h2','h3','h4','h5','h6']  ## TODO: si/no ...  

# Si un <div> no contiene estos elementos, lo juntamos todo en un <p>
DIV_TO_P_ELEMENTS = ['a', 'blockquote', 'dl', 'div', 'img', 'ol', 'p', 'table', 'ul']  
DIV_TO_P_ELEMENTS.extend(TAGS_TO_P)

# Expresiones para calcular el peso de cada elemento
#NEGATIVE_REGEX = re.compile(u".*combx.*|.*comment.*|.*com-.*|.*contact.*|.*foot.*|.*footer.*|.*footnote.*|.*masthead.*|.*media.*|.*meta.*|.*outbrain.*|.*promo.*|.*related.*|.*scroll.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*shopping.*|.*tags.*|.*tool.*|.*widget.*")
NEGATIVE_REGEX = re.compile(u".*combx.*|.*comment.*|.*com-.*|.*contact.*|.*foot.*|.*footer.*|.*footnote.*|.*masthead.*|.*outbrain.*|.*promo.*|.*related.*|.*scroll.*|.*shoutbox.*|.*sidebar.*|.*sponsor.*|.*shopping.*|.*tags.*|.*tool.*|.*widget.*")
POSITIVE_REGEX = re.compile(u".*article.*|.*body.*|.*content.*|.*entry.*|.*hentry.*|.*main.*|.*page.*|.*pagination.*|.*post.*|.*text.*|.*blog.*|.*story.*")
HIDDEN_REGEX = re.compile(u".*display: *none.*|.*visibility: *none.*|.*opacity: *0.*")
"""
style="display: none;"
visibility: hidden;
opacity: 0;
width: 0; height: 0;
"""

ENDPOINT_REGEX = re.compile("\.( |$)") 


MIN_INNERTEXT_CHARACTERS_LENGTH = 25 # primer preproceso de los nodos 
MIN_NODE_CHARACTERS_LENGTH = 150     # characters de los nodos candidatos
FIND_ONLY_MAIN_ARTICLE = False       # True --> extract only main text and siblings
CHILDREN_FACTOR = 1.0                # peso que dan los hijos a los padres en los pesos por css/id
CONTENT_SCORE_CHARACTERS = 75        # Cada X caracteres da un punto (hasta un máximo de 3)

class Readability(ScraperBase):
    
    def getFilteredText(self, rawHtml, returnText=True):
        
        # Clean TEXT
        cleanedHtml = self.cleanHtml(rawHtml)  # remove br, dots
        
        soup = BeautifulSoup(cleanedHtml, 'lxml')
        
        self.removeEmptyTags(soup)
        self.removeTags(soup)  # comments, TAGS_TO_REMOVE (scrips, style ...)
        ## convertNavigableToParagraph(soup)
        self.convertToParagraph(soup)      
        self.addEndDotToLiH(soup)


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
                innerText = node.get_text(separator='', strip=False, types=[NavigableString])
                if len(innerText) < MIN_INNERTEXT_CHARACTERS_LENGTH:
                    continue
                nodesToScore.append(node)
                continue

            ## Turn all divs that don't have children block level elements into p's 
            if node.name.lower() == "div":
                if not node.find_all(DIV_TO_P_ELEMENTS):
                    div_to_p.append(node)
                else:
                    # super beta ...
                    # try to convert NavigableString children
                    navigables = []
                    textLength = 0
                    for node in node.contents:
                        if isinstance(node, NavigableString):
                            navigables.append(node)
                            textLength += len(node)
                    if textLength > CONTENT_SCORE_CHARACTERS:
                        for nav in navigables:
                            # create <p>
                            newTag = soup.new_tag('p')
                            newTag.string = u'%s'%nav
                            nav.replace_with(newTag)                            
                            nodesToScore.append(newTag) 

        # convert div to p. Maintain attributes                
        for node in div_to_p:            
            innerText = node.get_text(separator='', strip=True, types=[NavigableString])
            if len(innerText) < MIN_INNERTEXT_CHARACTERS_LENGTH:
                continue
            node.clear()  # remove children
            node.name = 'p'
            node.string = innerText
            nodesToScore.append(node)    
    

        # for node in nodesToScore:
            # intentamos subirlo 1 nivel si no tiene hermanos
            # node = self.replaceParentWithParagraph(soup, node)
 
            
        # 2. ----------------------------------------  
        #   buscamos los padres y abuelos y les damos un peso inicial segun su longitud y las caracteristicas suyas y de sus hijos
        candidates = {}
        for node in nodesToScore:
            parentNode = node.parent
            grandParentNode = parentNode.parent if parentNode else None
            if not parentNode:
                continue

            # Limite mínimo de caracteres del nodo
            innerText = node.get_text(separator='', strip=False, types=[NavigableString])
            if len(innerText) < MIN_INNERTEXT_CHARACTERS_LENGTH:
                continue   

            # add end dot ---------------
            self._addEndDot(node, soup)
            # ---------------------------

            parent_key = id(parentNode)
            grand_parent_key = id(grandParentNode)

            # init parent node weigths
            if parent_key not in candidates:
                self.initializeNode(parentNode)
                candidates[parent_key] = parentNode
    
            # init grandParent node weigths
            if grandParentNode and grand_parent_key not in candidates:
                self.initializeNode(grandParentNode)
                candidates[grand_parent_key] = grandParentNode
    
            contentScore = 0
            # Add a point for the paragraph itself as a base. 
            contentScore += 1
            
            # Add points for any commas within this paragraph 
            contentScore += innerText.count(',') + innerText.count('.')
            
            # For every CONTENT_SCORE_CHARACTERS characters in this paragraph, add another point. Up to 3 points. 
            contentScore += min(int(len(innerText) / CONTENT_SCORE_CHARACTERS), 3)
            
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
            candidate.contentScore = candidate.contentScore * (1-self.getLinkDensity(candidate))
            
        # sort
        topCandidates = sorted(candidates.values(), key=lambda x: x.contentScore, reverse=True)

        if not topCandidates:
            raise NotEnougthTextException(u"No hay suficiente texto para procesar la página")


        # Quitamos de la lista ordenada de candidatos los que tienen un hijo o padres con mas puntos 
        # get top parents. dont add parents/children
        scoreLimit = 10.0
        finalCandidates = self.getCandidates(topCandidates, scoreLimit)
        if not finalCandidates:
            # dejamos pasar un poco mas ...
            finalCandidates = self.getCandidates(topCandidates, scoreLimit*0.5)

        # 4. ----------------------------------------
        # Buscamos los hermanos de cada bloque.
        # Nos quedamos con el primer bloque y los demas si tienen un mínimo de datos(nodes_length/3) y puntos(contentScore/4)
        bestNodes = []
        min_length = MIN_NODE_CHARACTERS_LENGTH
        min_score = 0
        for index, topCandidate in enumerate(finalCandidates):
            foundNodes, nodes_length = self.getSiblings(topCandidate)

            # límites para añadir otros nodos 
            if index == 0:
                min_length = max(MIN_NODE_CHARACTERS_LENGTH, nodes_length/3)
                min_score = topCandidate.contentScore/4
            
            if index == 0 or nodes_length > min_length:
                if topCandidate.contentScore > min_score:
                    for node in foundNodes:  # quitamos repedidos
                        if not node in bestNodes:
                            bestNodes.append(node)
                if FIND_ONLY_MAIN_ARTICLE:
                    break

        '''
        for node in bestNodes:
            print node.contentScore
            text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
            print len(text)
            print text
        '''

        if returnText:

            resultText = [block.get_text(separator=u' ', strip=True, types=[NavigableString]) for block in bestNodes]

            # change multiple spaces to only one
            resultText = [re.sub(u' +', u' ', text) for text in resultText]

            ##resultText = [block.get_text(separator=rules.SPLITTER, strip=True, types=[NavigableString]) for block in bestNodes]
            return scrapping_rules.SPLITTER.join(resultText), soup
        else:
            return bestNodes, soup
    
    
    # Quitamos de la lista ordenada de candidatos los que tienen un hijo o padres con mas puntos 
    # get top parents. dont add parents/children
    def getCandidates(self, topCandidates, scoreLimit):
        finalCandidates = []
        for topCandidate in topCandidates:
            add = True
            if topCandidate.contentScore < scoreLimit:
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
        return finalCandidates


    def initializeNode(self, node):
        """
        Puntua los nodos padres y les añade la puntuación de sus hijos
        """
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
    
        node.contentScore += self.getClassWeight(node)
    
    def getClassWeight(self, node, recursive=True):
        """
        Puntúa un nodo según su clase e id
        """
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
                children_weight = self.getClassWeight(child, recursive=True)
                weight += CHILDREN_FACTOR * children_weight
         
        return weight
    
    
    def getSiblings(self, node):
        """
        find siblings nodes to candidate node
        """
        
        bestNodes = []
        nodes_length = 0

        if not node.parent:
            return bestNodes, nodes_length
        
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
                        linkDensity = self.getLinkDensity(sibling);
                        nodeContent = sibling.get_text(separator='', strip=True, types=[NavigableString])
                        nodeLength  = len(nodeContent)
                        
                        if nodeLength > 80 and linkDensity < 0.25:  # pocos links y text largo
                            append = True
                        elif nodeLength < 80 and linkDensity == 0 and ENDPOINT_REGEX.match(nodeContent):  # no hay links y hay puntos
                            append = True
            
            if append:
                bestNodes.append(sibling)
                text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
                nodes_length += len(text)
    
        return bestNodes, nodes_length

    def getLinkDensity(self, node):
        if node.name == u'a':
            return 1.0
        
        link_length = len("".join([i.get_text(separator='', strip=True, types=[NavigableString]) or "" for i in node.findAll("a")]))
        text_length = len(node.get_text(separator='', strip=True, types=[NavigableString]))
        
        return float(link_length) / max(text_length, 1)   
    
        
    def convertToParagraph(self, soup):
        if TAGS_TO_P:
            for tag in soup.find_all(TAGS_TO_P):
                tag.name = 'p'        

    def addEndDotToLiH(self, soup):
        search_tags = soup.find_all(['li','h1','h2','h3'])
        for tag in search_tags:
            self._addEndDot(tag, soup)
    
    def _addEndDot(self, node, soup):
        
        if not node.contents:
            return
        
        last_content = node.contents[-1]
        
        is_navigable = isinstance(last_content, NavigableString)
        text = last_content if is_navigable else last_content.get_text(separator=' ', strip=True, types=[NavigableString])
        text = text.strip(' .:;)\n\r') + u'. '
        if is_navigable:
            node.contents[-1].replace_with(NavigableString(text))
            #print node.contents[-1]
        else:
            last_content.string = text
            
                
    def replaceParentWithParagraph(self, soup, node):
        """ 
        Si el nodo no tiene hermanos, lo subimos al nivel del padre.
        --- NO SE USA --- 
        """
        parent = node.parent
        if parent == soup.body:
            return node
        
        if len(list(parent.children)) == 1: 
            text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
            newTag = soup.new_tag('p')
            newTag.string = text
            parent.replace_with(newTag)                            
            return newTag
        
        return node

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
            u'https://serps.com/library/',
            u'http://www.publico.es/sociedad/liberado-madrid-joven-al-padre.html',
            u'http://www.publico.es/',
            u'http://www.elmundo.es/',
            u'http://www.zooplus.es/shop/tienda_perros/pienso_perros/taste_of_the_wild/taste_of_the_wild_adult/409340',
            u'http://www.decathlon.es/zapatillas-de-running-hombre-kalenji-ekiden-one-gris--id_8351755.html',
            u'http://www.luciasecasa.com/',
            u'http://www.luciasecasa.com/boda-de-la-semana/la-boda-la-semana-marta-jaime/',
            u'http://www.animalclan.com/es/6310-collar-scalibor-oferta.html',
            u'http://www.scubadocadiz.es/',            
            u'http://www.oceanoadictos.com/',
            u'https://www.yumping.com/buceo/cadiz',
            u'https://www.yumping.com/buceo/naturexplorer-buceo--e593',
            u'http://www.carmenrios.com/',
            u'http://afectadosclausulasuelo.org/',
            u'https://www.pet-supermarket.co.uk/Dog/Dog-Collars,-Tags-and-Leashes/c/PSGB00054',
            u'https://themebot.com/news/phpnuke',
            u'https://2a1-blog.phpnuke.org/en/c388140/php-returning-values-by-reference',
            u'https://3acd-descargar.phpnuke.org/es/c09262/microsoft-office-2010',
            u'https://2a1-downloads.phpnuke.org/en/c388143/five-nights-at-freddy-s-4',
            u'https://2msoffice-downloads.phpnuke.org/en/c09262/microsoft-office-2010',
            u'https://plus.google.com/photos/+MarcojesusrfBlogspot/albums/6275651924159238113/6275651927033663970?pid=6275651927033663970&oid=116996185249041591814',
            
            u'http://www.muyinteresante.es/salud/articulo/el-gusto-por-el-cafe-viene-marcado-en-los-genes-911412757909',
            u'http://economia.elpais.com/economia/2016/07/20/actualidad/1469042079_929155.html',
            u'http://economia.elpais.com/economia/2014/02/03/actualidad/1391418999_915675.html',
            
            u'http://selnd.com/2b1ftyW',
            u'http://www.muyinteresante.es/tag/genetica',
            u'http://www.muyinteresante.es/salud/articulo/revelan-por-que-unas-personas-envejecen-antes-que-otras-281436359667',
            ]

    def download(url):
        from concurrence.urllib3_pool_factory import Urllib3PoolFactory
        from data_mining.web_pages.scraper import UserAgent    
        
        pool = Urllib3PoolFactory.getSameOriginPool()
        request = pool.request('GET', url,
                               headers={"User-Agent": UserAgent.chrome , "Accept" : "text/html" })
        return request.data
    
    
    import tempfile 
    import webbrowser

    tmp=tempfile.NamedTemporaryFile(delete=True)
    path=tmp.name+'.html'

    readabilityFilter = Readability()

    for url in urls[-1:]:
        print(80*'-')
        print url
        rawHtml = download(url)
        try:
            bestNodes, soup = readabilityFilter.getFilteredText(rawHtml, returnText=False)
        except Exception as ex:
            bestNodes = []
            print u'%s' % ex
        
        htmlText = u"<html><head><meta charset='UTF-8' /></head><body>"
        htmlText += u'<div><strong><a href="%s">%s' % (url, url) + u'</a></strong></div><hr><br/><br/>'
        for node in bestNodes:
            #print node.contentScore
            text = node.get_text(separator=u' ', strip=True, types=[NavigableString])
            htmlText += u'<div style="color:blue; font-weight:bold; background-color:#ddd; text-align:center; padding: 10px 0px;"> Score: ' + u"%s  (%s)" % (node.contentScore,len(text)) + u'</div>'
            htmlText += u'<div>' + u"%s"%node + u'</div><hr>'
            #print len(text)
            #print text        
        htmlText += u'</body></html>'
        
        f=open(path, 'w')
        f.write(htmlText.encode('utf8'))
        f.close()
        webbrowser.open('file://' + path)
    