import unittest
from lfu_cache import LFUCache

class TestLFUCache(unittest.TestCase):


    def printitems(self, items):
        for i in items:
            print("{}-{}".format(i.key, i.value))

    def printcache(self, cache):
        print(f"Cache state: {cache.cache}")
        for freqitem in cache.freqlist:
            nodes = [','.join(str(n.key) + '-' + str(n.value) for n in freqitem.nodelist)]
            print(f"Frequency: {freqitem.frequency} - {nodes}")


    def test_zerocapacity(self):
        cache = LFUCache(0)

        cache.put(0,0)
        self.assertEqual(cache.get(0), -1)


    def test_multiple(self):
        cache = LFUCache(2)

        cache.put(1,1)
        cache.put(2,2)

        self.assertEqual(cache.freqlist.len,1)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.freqlist.len, 2)

        cache.put(3, 3)

        self.assertEqual(cache.freqlist.len, 2)

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

        cache.put(4, 4)

        self.assertEqual(cache.get(1), -1)

        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


    def test_leetthree(self):
        cache = LFUCache(3)

        cache.put(2,2)
        cache.put(1,1)

        self.assertEqual(cache.freqlist.len, 1)

        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.freqlist.len, 2)

        self.assertEqual(cache.get(1), 1)

        self.assertEqual(cache.get(2), 2)

        cache.put(3, 3)
        cache.put(4, 4)

        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(4), 4)


    def test_accesspresentatmaximumlimit(self):
       """Test accessing element wwhen we have reached limit.
          this should not evict anything"""
       cache = LFUCache(2)

       self.assertEqual(cache.get(2), -1)
       cache.put(2,6)

       self.assertEqual(cache.get(1), -1)
       cache.put(1,5)

       self.printcache(cache)

       cache.put(1,2)

       self.printcache(cache)

       self.assertEqual(cache.get(1) ,2)
       self.printcache(cache)
       self.assertEqual(cache.get(2), 6)
