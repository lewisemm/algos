import unittest, random

from sort import radix_sort
from tests.sort import helper

class TestRadixSort(unittest.TestCase):

    def test_radix_sort_on_array_size_100(self):
        a100 = [no for no in range(0,100)]

        random.shuffle(a100)

        radix_sorted = radix_sort.radix_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, radix_sorted[random_index])
        self.assertEqual(radix_sorted, [no for no in range(0,100)])

    def test_radix_sort_on_reversed_array_of_size_100(self):
        a100 = [no for no in range(99, -1, -1)]

        radix_sorted = radix_sort.radix_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, radix_sorted[random_index])
        self.assertEqual(radix_sorted, [no for no in range(0, 100)])

    def test_every_element_is_sorted(self):
        a20 = [no for no in range(0, 20)]

        random.shuffle(a20)

        radix_sorted = radix_sort.radix_sort(a20)

        ideal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        self.assertEqual(radix_sorted, ideal)

    def test_radix_sort_on_randomised_array_of_million_items(self):
        width, scale = 10**6, 10**6
        array = helper.create_randomised_array(width, scale)
        
        radix_sorted = radix_sort.radix_sort(array)
        self.assertEqual(radix_sorted, sorted(array))
    
    def test_radix_sort_on_repetitive_array_of_million_items(self):
        # width - array of one million values
        # scale - integers in the array are of values between 0 - 100
        width, scale = 10**6, 10**2
        array = helper.create_randomised_array(width, scale)
        radix_sorted = radix_sort.radix_sort(array)
        self.assertEqual(radix_sorted, sorted(array))

    def test_radix_sort_on_array_of_size_100_containing_negative_integers(self):
        a100 = [no for no in range(-99, 1)]

        random.shuffle(a100)

        radix_sorted = radix_sort.radix_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index - 99, radix_sorted[random_index])
        self.assertEqual(radix_sorted, [no for no in range(-99, 1)])

    def test_radix_sort_on_positives_and_negatives_in_array_of_million_items(self):
        # width - array of one million values
        # scale - integers in the array are of values between 0 - 100
        width, scale = 10**6, 10**2
        array = helper.create_randomised_array_with_negatives(width, scale)
        radix_sorted = radix_sort.radix_sort(array)
        self.assertEqual(radix_sorted, sorted(array))
