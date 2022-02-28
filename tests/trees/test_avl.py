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

    def test_left_left_rotation(self):
        """
                 50
                /
               40
              /
             30
        """
        self.avl.left_left_rotation = MagicMock()
        a = [50, 40, 30]
        for node in a:
            self.avl.insert(node)
        self.avl.left_left_rotation.assert_called_with(
            self.avl.root.left, self.avl.root, None
        )

    def test_left_right_rotation(self):
        """
             50
            /
           30
            \
             40
        """
        self.avl.left_right_rotation = MagicMock()
        self.avl.left_left_rotation = MagicMock()
        a = [50, 30, 40]
        for node in a:
            self.avl.insert(node)
        self.avl.left_right_rotation.assert_called_with(
            self.avl.root.left.right, self.avl.root.left, self.avl.root
        )
        self.avl.left_left_rotation.assert_called_with(
            self.avl.root.left, self.avl.root, None
        )

    def test_right_right_rotation(self):
        """
             50
              \
               60
                 \
                  70
        """
        self.avl.right_right_rotation = MagicMock()
        a = [50, 60, 70]
        for node in a:
            self.avl.insert(node)
        self.avl.right_right_rotation.assert_called_with(
            self.avl.root.right, self.avl.root, None
        )

