import unittest, random

from sort import heap_sort
from tests.sort import helper

class TestHeapSort(unittest.TestCase):

    def test_heap_sort_on_array_size_100(self):
        a100 = [no for no in range(0,100)]

        random.shuffle(a100)

        r_a100 = heap_sort.heap_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])
        self.assertEqual(r_a100, [no for no in range(0,100)])

    def test_heap_sort_on_reversed_array_of_size_100(self):
        a100 = [no for no in range(99, -1, -1)]

        r_a100 = heap_sort.heap_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])
        self.assertEqual(r_a100, [no for no in range(0, 100)])

    def test_heap_sort_on_array_of_size_100_containing_negative_integers(self):
        a100 = [no for no in range(-99, 1)]

        random.shuffle(a100)

        r_a100 = heap_sort.heap_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index - 99, r_a100[random_index])
        self.assertEqual(r_a100, [no for no in range(-99, 1)])

    def test_heap_sort_when_single_insert_is_used(self):
        negative = False
        values = []
        for i in range(100):
            random_val = random.randint(0, 1000)
            random_val = random_val * -1 if negative else random_val
            values.append(random_val)
            negative = not negative
        r_a100 = heap_sort.heap_sort_single_insert(values)
        self.assertEqual(r_a100, sorted(values))

    def test_heap_sort_on_randomised_array_of_million_items(self):
        width, scale = 10**6, 10**6
        array = helper.create_randomised_array(width, scale)
        newly_sorted = heap_sort.heap_sort(array)
        self.assertEqual(newly_sorted, sorted(array))
