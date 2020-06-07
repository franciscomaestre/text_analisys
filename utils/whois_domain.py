#!/usr/bin/python
# -*- coding: utf-8 -*-

import whois

ONE_YEAR = 365.2425

class WhoisDomain():
    def __init__(self, url):
        self.w = whois.query(url)
    
    def getCreationDate(self):
        return self.w.creation_date

    def getExpirationDate(self):
        return self.w.expiration_date

    def getDomainAge(self):
        try:
            delta = self.getExpirationDate() - self.getCreationDate()
            return int(delta.days/ONE_YEAR)
        except Exception as e:
            return -1
            #En caso de no poder verlo devolvemos -1
    
if __name__ == '__main__':
    
    whoisD = WhoisDomain('www.luciasecasa.com')
    print(whoisD.getCreationDate())
    print(whoisD.getExpirationDate())
    print(whoisD.getDomainAge())