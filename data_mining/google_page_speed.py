#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import random
from core.concurrence.urllib3_pool_factory import Urllib3PoolFactory

def googlePageSpeed(page, language, country):
    results = {}
    results['desktopResult'] = _googlePageSpeed(page, language, country)
    time.sleep(random.uniform(1.0, 2.2))
    results['mobileResult'] = _googlePageSpeed(page, language, country, mobile=True)
    return results

def _googlePageSpeed(page, language, country, mobile = False):
    
    result = {}
    
    payload = {}
    
    payload['key'] = u'AIzaSyAOHz-r9riG0D8pr4XHP4tNSpSmjqe8Qkw'
    payload['url'] = page
    payload['locale'] = u'%s_%s' % (language, country)
    if mobile:
        payload['strategy'] = u'mobile'
    
    pool = Urllib3PoolFactory.getSameOriginPool()
    
    try:
        r = pool.request('GET', u'https://www.googleapis.com/pagespeedonline/v1/runPagespeed', fields=payload, timeout=10)
    except Exception as ex:
        #print r.data
        print(ex)
        result['pageSpeedError'] = True
        return result
        
    googlePageSpeed = json.loads(r.data)
    
    if 'error' in googlePageSpeed:
        result['pageSpeedError'] = True
    else:
        result['pageSpeedError'] = False
        result['pageSpeedScore'] = googlePageSpeed['score']
        result['pageSpeedNotes'] = _generateNotesGoogleSpeed(googlePageSpeed)
        
    return result

def _generateNotesGoogleSpeed(googlePageSpeed):
    notes = []
    
    if 'formattedResults' in googlePageSpeed and 'ruleResults' in googlePageSpeed['formattedResults']:
        for ruleResultName in googlePageSpeed['formattedResults']['ruleResults']:
            if 'localizedRuleName' in googlePageSpeed['formattedResults']['ruleResults'][ruleResultName]:
                notes.append(googlePageSpeed['formattedResults']['ruleResults'][ruleResultName]['localizedRuleName'])
                
    return notes


if __name__ == '__main__':
    print googlePageSpeed(u'http://franciscomaestre.es')