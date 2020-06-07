#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 28 de jul. de 2016

@author: jhuebra

Quitar Regional. Son todoslos datos por paise

Top/World/Español/Regional/América/Colombia/Departamentos/Vichada

+ Top/World/Español/
- Top/World/Español/Regional/

+ Top/World/Español/Artes/
- Top/World/Español/Artes/Regional/

narrow2 mejor que narrow1 mejor que narrow 

'''

import os
import re

if __name__ == '__main__':
    
    TREE_START = u'Top/World/Español/'
    DONT_PARSE = u'Regional'
    
    from lxml import etree
    filename = os.getcwd() + './../' + u'data/dmoz/structure.rdf.u8'
    i = 0
    added = 0
    for event, elem in etree.iterparse(filename, events=('start', 'end')):
        if event == "end":
            if isinstance(elem, etree._Element):
                if elem.tag == "{http://dmoz.org/rdf/}Topic":
                    topic_id = elem.attrib['{http://www.w3.org/TR/RDF/}id'] 
                    if not topic_id:
                        elem.clear()
                        continue
                    if not TREE_START in topic_id:
                        elem.clear()
                        continue
                    if DONT_PARSE in topic_id:
                        elem.clear()
                        continue
                    
                    
                    print elem.attrib['{http://www.w3.org/TR/RDF/}id'] 
                    i+=1
                    for child in elem.getchildren():
                        
                        if child.tag == "{http://purl.org/dc/elements/1.0/}Title":
                            print child.text
                            #addToMongoDB(url)
                        elif child.tag == "{http://purl.org/dc/elements/1.0/}Description":
                            print child.text
                        elif child.tag == "{http://dmoz.org/rdf/}catid":
                            print child.text
                        elif child.tag == "{http://dmoz.org/rdf/}narrow" or\
                             child.tag == "{http://dmoz.org/rdf/}narrow1" or\
                             child.tag == "{http://dmoz.org/rdf/}narrow2":
                            print u'child %s' % child.attrib['{http://www.w3.org/TR/RDF/}resource'] 
 
                    #clear the elements, without this, your RAM will saturate, with this only 30Mb of ram is used
                    elem.clear()

    """
    import rdflib
    g=rdflib.Graph()
    g.load(filename)
    
    for s,p,o in g:
        print s,p,o
        break
    """
