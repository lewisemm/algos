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

    def test_hashtable_get(self):
        """
        Test get operation on hashtable.
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

        for k, v in mapping:
            self.assertEqual(self.hashtable.get(k), v)

    def test_hashtable_delete(self):
        """
        Test delete operation on hashtable.
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
        for key, value in mapping:
            self.hashtable.delete(key)
            # key does not exist and any attempt to access it should raise
            # KeyError
            with self.assertRaises(KeyError):
                self.hashtable.delete(key)

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

    def test_hashtable_shrink_when_three_quarter_space_unused(self):
        """
        Test that the hashtable shrinks in size when the total free space is
        >= 3/4 and capacity > self.hashtable.DEFAULY_SIZE
        """
        self.assertEqual(self.hashtable.capacity, 8)
        self.assertEqual(len(self.hashtable.array), 8)
        a = [no for no in range(10)]
        random.shuffle(a)
        b = [no for no in range(10, 20)]
        random.shuffle(b)
        mapping = {}
        for pair in zip(a, b):
            key, value = pair
            self.hashtable.insert(key, value)
            mapping[key] = value
        self.assertEqual(self.hashtable.capacity, 16)
        self.assertEqual(len(self.hashtable.array), 16)
        # hashtable now has 10 items, capacity is 16. Delete 6 items to get 12
        # free spaces (12/16 == 3/4 free space).
        count = 0
        for key in mapping:
            if count == 7:
                break
            self.hashtable.delete(key)
            count += 1
        self.assertEqual(self.hashtable.capacity, 8)
        self.assertEqual(len(self.hashtable.array), 8)

    def test_hashtable_not_shrink_when_free_space_is_three_quarters(self):
        """
        Test that the hashtable does not shrink when total free space is 3/4
        and capacity == self.hashtable.DEFAULT_SIZE (8).
        """
        self.assertEqual(self.hashtable.capacity, 8)
        self.assertEqual(len(self.hashtable.array), 8)
        # add 3 items, free space == 5/8
        to_be_deleted = None
        for i in range(3):
            key, value = int(random.random() * 100), int(random.random() * 100)
            self.hashtable.insert(key, value)
            to_be_deleted = key
        # delete 1 item, free space = 6/8 (i.e. 3/4)
        self.hashtable.delete(to_be_deleted)
        # assert key has been deleted
        with self.assertRaises(KeyError):
            self.hashtable.get(to_be_deleted)
        # assert hashtable has not shrunk
        self.assertEqual(self.hashtable.capacity, 8)
        self.assertEqual(len(self.hashtable.array), 8)
