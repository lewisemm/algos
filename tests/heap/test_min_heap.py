import unittest, random

from heap.min_heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def tearDown(self):
        del self.heap

    def test_get_heap_size(self):
        """
        Test get_size method.
        """
        self.assertEqual(self.heap.get_size(), 0)
        length = 100
        values = [a for a in range(length)]
        self.heap.bulk_insert(values)
        self.assertEqual(self.heap.get_size(), length)

    def test_peek_raise_exception_when_heap_empty(self):
        """
        Test peek raises exception when heap is empty.
        """
        with self.assertRaises(Exception):
            self.heap.peek()
        self.assertEqual(self.heap.get_size(), 0)

    def test_peek_non_empty_heap(self):
        """
        Test peek returns minimum value without modifying the heap.
        """
        a100 = [a for a in range(100)]
        random.shuffle(a100)
        self.heap.bulk_insert(a100)
        size = self.heap.get_size()
        minimum = self.heap.peek()
        self.assertEqual(minimum, 0)
        size2 = self.heap.get_size()
        self.assertEqual(size, size2)
        minimum2 = self.heap.peek()
        self.assertEqual(minimum2, 0)
        size3 = self.heap.get_size()
        self.assertTrue(size == size2 == size3)

    def test_extract_min_raises_exception_when_empty_heap(self):
        """
        Test extract_min raises exception when heap is empty.
        """
        with self.assertRaises(Exception):
            self.heap.extract_min()
        self.assertEqual(self.heap.get_size(), 0)

    def test_extract_min_non_empty_heap(self):
        """
        Test extract_min pops minimum value from the heap.
        """
        a100 = [a for a in range(100)]
        random.shuffle(a100)
        self.heap.bulk_insert(a100)
        size = self.heap.get_size()
        minimum = self.heap.extract_min()
        self.assertEqual(minimum, 0)
        size2 = self.heap.get_size()
        self.assertEqual(size - 1, size2)

        minimum2 = self.heap.extract_min()
        self.assertEqual(minimum2, 1)
        size3 = self.heap.get_size()
        self.assertTrue(size - 2 == size2 - 1 == size3)

    def test_single_insert_on_empty_heap(self):
        """
        Test single insert on empty heap.
        """
        val = random.randint(0, 1000)
        self.heap.single_insert(val)
        size = self.heap.get_size()
        self.assertEqual(size, 1)
        minimum = self.heap.peek()
        self.assertEqual(minimum, val)

    def test_single_insert_on_non_empty_heap(self):
        """
        Test single insert on non-empty heap.
        """
        a100 = [a for a in range(100)]
        random.shuffle(a100)
        self.heap.bulk_insert(a100)
        # maintains min-heap property by bubbling smallest value to the top.
        val = -42
        self.heap.single_insert(val)
        minimum = self.heap.peek()
        self.assertEqual(minimum, val)

    def test_single_insert_maintains_min_heap_property(self):
        """
        Test min_heap property is maintained when using single_insert.
        """
        a100 = [a for a in range(100)]
        random.shuffle(a100)
        for val in a100:
            self.heap.single_insert(val)
        sorted_values = []
        size = self.heap.get_size()
        while size > 0:
            sorted_values.append(self.heap.extract_min())
            size -= 1
        self.assertEqual(sorted_values, [a for a in range(100)])

    def test_bulk_insert_maintains_min_heap_property(self):
        """
        Test min-heap property is maintained when using bulk_insert.
        """
        a100 = [a for a in range(100)]
        random.shuffle(a100)
        self.heap.bulk_insert(a100)
        sorted_values = []
        size = self.heap.get_size()
        while size > 0:
            sorted_values.append(self.heap.extract_min())
            size -= 1
        self.assertEqual(sorted_values, [a for a in range(100)])
