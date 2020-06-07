import urllib3, json, xmltodict
"""
CopyScape API
http://www.copyscape.com/api-guide.php

"""

class CopyChecker(object):
    
    def __init__(self, username, password, apiDomain = 'http://www.copyscape.com/api/'):
        self._username = username
        self._password = password
        self._apiDomain = apiDomain
        
    def getResultFromText(self, text):
        params = {'u' : self._username, 'k' : self._password, 'o' : 'csearch', 'e' : 'UTF-8', 't' : text, 'c': 3}
        result = self._execHttpRequest(self._apiDomain, params, 'POST')
        xmlData = result.data
        dictData = xmltodict.parse(xmlData)
        return dictData
    
    def getResultFromUrl(self, url):
        params = {'u' : self._username, 'k' : self._password, 'o' : 'csearch', 'q' : url, 'c' : 3}
        result = self._execHttpRequest(self._apiDomain, params, 'GET')
        xmlData = result.data
        dictData = xmltodict.parse(xmlData)
        return dictData
    
    def _execHttpRequest(self, url, paramsData = None, method = 'GET'):
        http = urllib3.PoolManager()
        headers = {'User-Agent' : "Magic Browser"}
        r = http.request(method, url, fields=paramsData, headers=headers)
        return r