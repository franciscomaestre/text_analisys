#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 20 de sept. de 2016

@author: jhuebra

https://hunspell.github.io/
Hunspell is the spell checker of LibreOffice, OpenOffice.org, Mozilla Firefox 3 & Thunderbird, Google Chrome,
and it is also used by proprietary software packages, like Mac OS X, InDesign, memoQ, Opera and SDL Trados.

Carga en memoria el diccionarioy y busca en C++.  Se pueden pedir sugerencias y usar su stemmer.
El stemmer no es por software como nltk.stem.snowball y si no encuentra la palabra no devuelve nada.

Diccionarios de Libreoffice:
https://cgit.freedesktop.org/libreoffice/dictionaries/tree/

Otros formatos (Mozilla... ) son simples ficheros comprimidos con el .aff y .dic
El alemán : http://extensions.libreoffice.org/extension-center/german-de-de-frami-dictionaries
'''

hunSpell_factory = {}

import os
DICT_PATH = "%s/dictionaries/" % os.path.dirname(__file__)

def hunSpellcheck(language_country, word):
    import hunspell
    if not language_country in hunSpell_factory:
        hunSpell = hunspell.HunSpell('%s%s.dic'%(DICT_PATH, language_country),
                                     '%s%s.aff'%(DICT_PATH, language_country))
        hunSpell_factory[language_country] = hunSpell
    else:
        hunSpell = hunSpell_factory[language_country] 
    
    return hunSpell.spell(word)


if __name__ == '__main__':
    
    print('Holla', hunSpellcheck('es_ES', 'Holla'))
    print('Hellow', hunSpellcheck('en_US', 'Hellow'))
    print('NATO', hunSpellcheck('en_US', 'NATO'))
    print('Maquediches', hunSpellcheck('it_IT', 'Maquediches'))
    print(u'España', hunSpellcheck('es_ES', u'España'))
