import unittest
from core.cache.memcached_factory import MemcachedFactory


class MemCachedTest(unittest.TestCase):

    def test_01_MemCached(self):
        key = 'tokenTest'
        memcachedStorage = MemcachedFactory.getInstance(space='test')

        value = "Esto es una prueba"
        memcachedStorage.set(key, value, rawKey=True)
        
        restore = memcachedStorage.get(key, rawKey=True)
        self.assertEqual(value, restore, 'Valor recuperado distinto')
        
    def test_02_MemCached(self):
        key = 'tokenTest'
        memcachedStorage = MemcachedFactory.getInstance(space='test')

        value = "Esto es una prueba"
        memcachedStorage.set(key, value, rawKey=False)
        
        restore = memcachedStorage.get(key, rawKey=False)
        self.assertEqual(value, restore, 'Valor recuperado distinto')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
