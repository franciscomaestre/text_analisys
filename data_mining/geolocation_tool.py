#!/usr/bin/python
# -*- coding: utf-8 -*-

import geoip2.database

class GeoLocationTool():
    def __init__(self):
        self.reader = geoip2.database.Reader('/var/seologies/maxmind/GeoLite2-City.mmdb')
    
    def getHostNameCountry(self, hostname, language= 'en'):
        import socket
        ip = socket.gethostbyname(hostname)
        return self.getIpCountry(ip, language)
    
    def getIpCountry(self, ip, language = 'en'):
        response = self.reader.city(ip);
        return response.country.names[language];
    
    def getHostnameCountryIsoCode(self, hostname):
        import socket
        ip = socket.gethostbyname(hostname)
        return self.getIpCountryIsoCode(ip)
        
    def getIpCountryIsoCode(self, ip):
        response = self.reader.city(ip);
        return response.country.iso_code;
    
if __name__ == '__main__':
    
    import socket
    ip = socket.gethostbyname_ex('www.elpais.com')
    print ip
