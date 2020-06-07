#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 29 de jun. de 2016

Logueados en Facebook
https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=search%3Ftype%3Dplacetopic%26topic_filter%3Dall%26fields%3Did%2Cname%2Cparent_ids%26locale%3Des%26limit%3D3000&version=v2.6

search?type=placetopic&topic_filter=all&fields=id,name,parent_ids&locale=es&limit=5000

'''


import pprint
import copy
import os
import codecs

from collections import OrderedDict
import json


class Node(object):
    def __init__(self, index, name, parent_ids):
        self.index = index
        self.name = name
        self.parent_ids = parent_ids
        self.children = []
    def __repr__(self, *args, **kwargs):
        
        return u"%.5s %s" %(self.index, self.name )


def pchildrenNode(nodes_dict, node, outfile, prefix=[], level=0):
    #print ("\t"*level + u"%s"%node)
    
    if node.index != -1:
        prefix.append(node.name)
    
    for node in node.children:
        try:
            pchildrenNode(nodes_dict, node, outfile, copy.copy(prefix), level+1)
        except:
            print node

    if not node.children and len(prefix) > 1:
        output = u""
        for i, p in enumerate(prefix):
            output += p
            if i < len(prefix)-1:
                output += u" > "
            else:
                output += os.linesep 
        print output
        outfile.write(output)
            
def main(verticals, outfile):
    
    nodes_dict = {}
    root_nodes = []
    
    for node_data in verticals:
        parent_ids = node_data.get('parent_ids', [])
        parent_ids = [int(p) for p in parent_ids]
        name = '%s' % json.loads(r'"%s"' %node_data['name'])
        index = int(node_data.get('id', -1))
        
        node = Node(index, name, parent_ids)
        nodes_dict[index] = node
        
        if not parent_ids:
            root_nodes.append(node)

    nodes_dict = OrderedDict(sorted(nodes_dict.items(), key=lambda t: t[0])) 
    
    # add childrens
    for index, node in nodes_dict.items():
        for parent_id in node.parent_ids:
            try:
                nodes_dict[parent_id].children.append(node)
            except:
                print parent_id
    
    for root in root_nodes:
        pchildrenNode(nodes_dict, root, outfile, prefix=[])


from categories_es_ES import categories_es_ES
from categories_en_US import categories_en_US, categories_en_BR


if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(__file__)
    
    path = PROJECT_ROOT + '/taxonomy.%s.txt' % 'es-ES'
    with codecs.open(path, 'w', encoding='utf-8') as outfile:
        main(categories_es_ES['data'], outfile)
    
    path = PROJECT_ROOT + '/taxonomy.%s.txt' % 'en-US'
    with codecs.open(path, 'w', encoding='utf-8') as outfile:
        main(categories_en_US['data'], outfile)
    