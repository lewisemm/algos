import random
import math
import unittest

from unittest.mock import MagicMock

from trees.bst.avl import AVL
from trees.traversal.inorder import inorder_traversal


class AVLTest(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()

    def tearDown(self):
        del self.avl

    def test_bst_property(self):
        """
        Test that tree maintains bst property after several inserts.
        """
        size = range(1000)
        a100 = [no for no in size]
        random.shuffle(a100)
        for no in a100:
            self.avl.insert(no)
        ordered = inorder_traversal(self.avl)
        self.assertEqual(ordered, [no for no in size])
