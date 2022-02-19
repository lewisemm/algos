import unittest, random

from hashtable.hashtable import HashTable

class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.hashtable = HashTable()

    def test_hashtable_insert(self):
        """
        Test insert operation on hashtable.
        """
        a = [no for no in range(10)]
        random.shuffle(a)
        b = [no for no in range(10, 20)]
        random.shuffle(b)
        mapping = {}
        for pair in zip(a, b):
            key, value = pair
            self.hashtable.insert(key, value)
            mapping[pair] = True

        appears_once = {}
        for element in self.hashtable.array:
            if element:
                for pair in element:
                    self.assertTrue(mapping[pair])
                    self.assertFalse(appears_once.get(pair, False))
                    appears_once[pair] = True

    def test_hashtable_doubling(self):
        """
        Test size doubling of hashtable when capacity is exceeded.
        """
        self.assertEqual(self.hashtable.capacity, 8)
        self.assertEqual(len(self.hashtable.array), 8)
        a = [no for no in range(10)]
        random.shuffle(a)
        b = [no for no in range(10, 20)]
        random.shuffle(b)
        for pair in zip(a, b):
            key, value = pair
            self.hashtable.insert(key, value)
        self.assertEqual(self.hashtable.capacity, 16)
        self.assertEqual(len(self.hashtable.array), 16)

    def test_hashtable_overwrite_with_insert(self):
        """
        Test overwrite when existing key is used in an insert operation.
        """
        a = [no for no in range(10)]
        random.shuffle(a)
        b = [no for no in range(10, 20)]
        random.shuffle(b)
        mapping = {}
        for pair in zip(a, b):
            key, value = pair
            self.hashtable.insert(key, value)
            mapping[key] = value
        c = [no for no in range(20, 30)]
        random.shuffle(c)

        for pair in zip(a, c):
            key, value = pair
            self.hashtable.insert(key, value)
            self.assertNotEqual(self.hashtable.get(key), mapping[key])
            self.assertEqual(self.hashtable.get(key), value)
