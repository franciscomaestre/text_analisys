#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time
from utils.persistence.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):

    def test_01_FileStorage(self):
        cachePath = '/var/testCache'
        key = 'prueba'
        value = {"mensaje" : "Esto es una prueba"}
        timeout = 2
        version = 1
        compress = True
        defaultValue = 'Ha habido un error'
        
        fileStorage = FileStorage(cachePath, {'timeout':timeout, 'compress':compress})
        fileStorage.set(key, value, timeout, version)
        restore = fileStorage.get(key, defaultValue, version)
        self.assertEqual(value, restore, 'Valor recuperado distinto')
        
    def test_02_Delete(self):
        cachePath = '/var/testCache'
        key = 'prueba'
        value = {"mensaje" : "Esto es una prueba"}
        timeout = 2
        version = 1
        compress = True
        defaultValue = 'Ha habido un error'
        
        fileStorage = FileStorage(cachePath, {'timeout':timeout, 'compress':compress})
        fileStorage.set(key, value, timeout, version)
        time.sleep(timeout + 2)
        restore = fileStorage.get(key, defaultValue, version)
        self.assertEqual(defaultValue, restore, 'Valor recuperado no es el default')
        
    def test_03_Version(self):
        cachePath = '/var/testCache'
        key = 'prueba'
        value1 = {u"mensaje" : u"Ésto es una prueba"}
        value2 = {u"mensaje" : u"Ésto es una prueba 2da Version"}
        timeout = 5
        version = 1
        compress = True
        defaultValue = 'Ha habido un error'
        
        fileStorage = FileStorage(cachePath, {'timeout':timeout, 'compress':compress})
        fileStorage.set(key, value1, timeout, version)
        fileStorage.set(key, value2, timeout, version + 1)
        restore = fileStorage.get(key, defaultValue, version)
        self.assertEqual(value1, restore, 'No hemos obtenido los datos de la version 1')
        restore = fileStorage.get(key, defaultValue, version + 1)
        self.assertEqual(value2, restore, 'No hemos obtenido los datos de la version 2')
    
    def test_04_Uncompress(self):
        cachePath = '/var/testCache'
        key = 'prueba'
        value = '{"mensaje" : "Esto es una prueba"}'
        timeout = 10
        version = 1
        compress = False
        defaultValue = 'Ha habido un error'
        
        fileStorage = FileStorage(cachePath, {'timeout':timeout, 'compress':compress})
        fileStorage.set(key, value, timeout, version)
        restore = fileStorage.get(key, defaultValue, version)
        self.assertEqual(value, restore, 'Valor recuperado distinto')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
