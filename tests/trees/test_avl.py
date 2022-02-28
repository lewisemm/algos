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

    def test_log_n_max_depth(self):
        """
        Tests that the height from root to leaf is theta log_n.
        """
        options = tuple([no for no in range(1, 10)])
        exponent = random.choice(options)
        nodes = 2**exponent
        size = range(nodes)

        vertices = [no for no in size]
        random.shuffle(vertices)
        for v in vertices:
            self.avl.insert(v)
        log_n_height = math.ceil(math.log(nodes, 2))
        tree_height = self.avl.get_height(self.avl.root)
        self.assertTrue(
            log_n_height - 1 <= tree_height <= log_n_height + 3)
        bal = self.avl.get_balance(self.avl.root)
        self.assertTrue(-1 <= bal <= 1)

    def test_find_node_existing_node(self):
        """
        Tests that a node can be found and returned in the tree.
        """
        nodes = 2**10
        size = range(nodes)
        a1025 = [no for no in size]
        random.shuffle(a1025)
        for no in a1025:
            self.avl.insert(no)
        findable = int(random.random() * nodes)
        found, _ = self.avl.find_node(findable)
        self.assertEqual(findable, found.key)

    def test_find_node_non_existing_node(self):
        """
        Tests that `None` is returned when a node does not exist in the tree.
        """
        nodes = 2**10
        size = range(nodes)
        a1025 = [no for no in size]
        random.shuffle(a1025)
        for no in a1025:
            self.avl.insert(no)
        findable = 3347
        found, _ = self.avl.find_node(findable)
        self.assertEqual(found, None)

