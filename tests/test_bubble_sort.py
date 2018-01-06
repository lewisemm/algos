import unittest, random

from sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_on_array_size_100(self):
        a100 = range(0,100)

        random.shuffle(a100)

        r_a100 = bubble_sort.bubble_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])
        self.assertEqual(r_a100, range(0, 100))

    def test_bubble_sort_on_reversed_array_of_size_100(self):
        a100 = range(99, -1, -1)

        r_a100 = bubble_sort.bubble_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index, r_a100[random_index])
        self.assertEqual(r_a100, range(0, 100))

    def test_bubble_sort_on_array_of_size_100_containing_negative_integers(self):
        a100 = range(-99, 1)

        random.shuffle(a100)
        
        r_a100 = bubble_sort.bubble_sort(a100)

        random_index = random.randint(0, 99)

        self.assertEqual(random_index - 99, r_a100[random_index])
        self.assertEqual(r_a100, range(-99, 1))

    def test_every_element_is_sorted(self):
        a20 = [5, 18, 15, 6, 4, 12, 1, 3, 17, 8, 19, 11, 16, 0, 13, 7, 2, 14, 9, 10]

        result = bubble_sort.bubble_sort(a20)

        ideal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        self.assertEqual(result, ideal)
