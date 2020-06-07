#!/usr/bin/python
# -*- coding: utf-8 -*-
from data_mining.web_pages.scraper import Scraper

if __name__ == '__main__':
    url = 'https://2msoffice-downloads.phpnuke.org/en/c09262/microsoft-office-2010'
    scraper = Scraper(url)
    print scraper.getDataDocument().text
    
