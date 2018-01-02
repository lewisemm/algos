import unittest, random

from sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort_on_array_size_100(self):
        a100 = range(0,100)
        r_a100 = merge_sort.merge_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])

    def test_merge_sort_on_reversed_array_of_size_100(self):
        a100 = range(99, -1, -1)
        r_a100 = merge_sort.merge_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])

    def test_merge_sort_on_array_of_size_100_containing_negative_integers(self):
        a100 = range(-99, 1)
        r_a100 = merge_sort.merge_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index - 99, r_a100[random_index])
