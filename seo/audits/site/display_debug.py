#!/usr/bin/python
# -*- coding: utf-8 -*-


def _displayLdaInfo(siteTokens, siteCategories):
    print u'SITE TOKENS'
    for token, relevance in siteTokens:
        print u'\t\t%s ---> %s' % (token, relevance)
    
    print u'SITE CATEGORIES'
    for categoriesType in siteCategories.keys():
        print u'TIPO: %s' % categoriesType    
        for category, score in siteCategories[categoriesType]:
            print u'\t%s --> %s' % (category, score)
    
def _displayCompetenceInfo(siteDomainInfo, domainCompetence):
    
    '''
    Información del Dominio
    '''
    print u'\tPosicionamiento del Dominio:'
    print u'\t\t%s' % siteDomainInfo
    
    print u'\tNO Apareces en las siguientes queries:'
    for query in siteDomainInfo.notAppearIn:
        print u'\t\t%s' % query
        
    print u'\tApareces en las siguientes queries:'
    for query, rankedUrl in siteDomainInfo.appearIn.items():
        print u'\t\t%s --> %s' % (query, rankedUrl.rank)

    '''
    Información de la competencia
    '''
    
    print u'\tCompetencia en las Queries Analizadas:'
    
    for domainInfo in domainCompetence:
        print u'\t\t%s' % domainInfo
        

def _displayTable(topicsTable):
    import tempfile 
    import webbrowser
    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'
    f=open(path, 'w')
    f.write(topicsTable)
    f.close()
    webbrowser.open('file://' + path)    
    