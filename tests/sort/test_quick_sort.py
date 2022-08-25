import unittest, random

from sort import quick_sort
from tests.sorts import helper

class TestQuickSort(unittest.TestCase):

    def test_quick_sort_on_array_size_100(self):
        a100 = [no for no in range(0,100)]

        random.shuffle(a100)

        quick_sort.quick_sort(a100, 0, len(a100) - 1)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, a100[random_index])
        self.assertEqual(a100, [no for no in range(0,100)]) 

    def test_quick_sort_on_reversed_array_of_size_100(self):
        a100 = [no for no in range(99, -1, -1)]
        
        quick_sort.quick_sort(a100, 0, len(a100) - 1)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, a100[random_index])
        self.assertEqual(a100, [no for no in range(0, 100)])

    def test_quick_sort_on_array_of_size_100_containing_negative_integers(self):
        a100 = [no for no in range(-99, 1)]

        random.shuffle(a100)

        quick_sort.quick_sort(a100, 0, len(a100) - 1)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index - 99, a100[random_index])
        self.assertEqual(a100, [no for no in range(-99, 1)])

    def test_every_element_is_sorted(self):
        a20 = [no for no in range(0, 20)]

        random.shuffle(a20)

        quick_sort.quick_sort(a20, 0, len(a20) - 1)

        ideal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        self.assertEqual(a20, ideal)

    def test_quicksort_on_randomised_array_of_million_items(self):
        width, scale = 10**6, 10**6
        array = helper.create_randomised_array(width, scale)
        start, stop = 0, len(array) - 1
        quick_sort.quick_sort(array, start, stop)
        self.assertEqual(array, sorted(array))

