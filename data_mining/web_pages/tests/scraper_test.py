#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.data_mining.web_pages.scraper import Scraper

if __name__ == '__main__':
    url = u'https://2msoffice-downloads.phpnuke.org/en/c09262/microsoft-office-2010'
    scraper = Scraper(url)
    print scraper.getDataDocument().text
    
