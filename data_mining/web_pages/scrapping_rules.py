#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

'''
    Arc90 bien montado
    http://nirmalpatel.com/fcgi/hn.py
    
    Tenemos la opción de usar un SoupStrainer para en vez de quitar tags.
    Crear beautifulSoup con los que nos interesan -->title, meta y body? No es que nos ahorremos mucho...
    
    
    1. Aplicamos TAGS_TO_REMOVE
    3. Todo P y H[1-3] se convierte en su contenido en plano
    4. Aplicamos TAGS_TO_CONVERT
    5. Rellenamos los <ul> con los hijos de sus hijos y lo convertimos en div
    6. Todos los enlaces sin hermanos deben sustituir a su padre O BORRARSE??
    7. Todos los enlaces cuyos hermanos sean enlaces deben borrarse
    8. Eliminar todo header cuyo padre sea body
    9. Todo NavigableString que sea hijo de div,main,article,section se convierte en P
    10.Todo P que tengo uno o ningún hermano será eliminado si entre él y su hermano
       no llegan a un mínimo de palabras
    11.Aplicamos la función del calculo de scoring para P teniendo en cuenta
       POSITIVE_TAGS y POSITIVE_REGEX

    ------------
    
    Método de resta con la Home:
    
    1. Descargamos la Home
    2. Obtenemos todos los A,P,SPAN de la Home y eliminamos de la URL los que sean idénticos
    
'''

MIN_WORD_LENGTH = 5
MIN_EMPTY = 2
MIN_WORDS = 4

# SIEMPRE EN MINUSCULA YA QUE SINO LA LIAMOS

SPLITTER_TAG = 'WWXN0B0KK4KXWW'.lower()
SPLITTER = ' %s ' % SPLITTER_TAG

POSITIVE_TAGS = ['main', 'h1', 'h2', 'h3' ]

NEGATIVE_REGEX = re.compile(".*comment.*|.*meta.*|.*footer.*|.*foot.*|.*cloud.*|.*head.*|.*date.*|.*navbar.*|.*related-posts.*|.*post-related.*|.*cookie.*|.*menu.*|.*hidde.*")

REPLACE_BR_REGEX = re.compile("<br */? *>[ \\r\\n]*<br */? *>")
REPLACE_BR_REGEX = re.compile("<br */? *>")
REPLACE_DOT_REGEX = re.compile("\.{2,6}")

REMOVE_DISPLAY_NONE_REGEX = re.compile(".*display: *none.*|.*visibility: *none.*")
"""
style="display: none;"
visibility: hidden;
opacity: 0;
width: 0; height: 0;
"""

TAGS_TO_REMOVE = [
                  # General tags Elements
                  'script', 'links', 'style', 'meta', 'noscript', 'head', 'footer', 'nav', 'style', 'details', 'aside', 'hr', 'time', #'br',
                  # Form tags Elements
                  'button', 'select', 'label', 'fieldset', 'datalist', 'input'
                  # Frame tags Elements
                  'iframe',
                  # Audio/Video tags Elements
                  'audio', 'video',
                  # List tags Elements
                  'men',
                  # Programming
                  'embed', 'object']

TAGS_TO_REPLACE = {
                   # Tags to Convert to P
                   'cite': 'p',
                   'code': 'p',
                   'pre': 'p',
                   'span': 'p',
                   'textarea':'div'
                   }

TAGS_TO_ENCAPSULATE_CHILDREN = ['div', 'main', 'article', 'section', 'header']

TAGS_TO_GET_CONTENT = ['p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

TAGS_TO_GET_CONTENT_SPLITTED = ['table', 'col', 'ul', 'ol', 'dl', 'abbr']


