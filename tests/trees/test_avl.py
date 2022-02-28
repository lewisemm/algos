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

    def test_delete_node_with_only_left_subtree(self):
        """
                        60
                       /  \
                     30    70
                    /        \
                   20         80
        """
        nodes = [60, 70, 30, 20, 80]
        for node in nodes:
            self.avl.insert(node)
        thirty = self.avl.root.left
        twenty = thirty.left
        found, _ = self.avl.find_node(thirty.key)
        self.assertEqual(found, thirty)
        self.avl.delete(thirty.key)
        found, _ = self.avl.find_node(thirty.key)
        self.assertEqual(found, None)
        self.assertNotEqual(thirty, self.avl.root.left)
        self.assertEqual(self.avl.root.left, twenty)

    def test_delete_node_with_only_right_subtree(self):
        """
                   40
                  /  \
                30    60
                /    /  \
              20    50   70
                          \
                           80
        """
        nodes = [50, 30, 40, 20, 70, 60, 80]
        for node in nodes:
            self.avl.insert(node)
        forty = self.avl.root
        sixty = forty.right
        seventy = sixty.right
        eighty = seventy.right
        found, _ = self.avl.find_node(seventy.key)
        self.assertEqual(found, seventy)
        self.avl.delete(seventy.key)
        found, _ = self.avl.find_node(seventy.key)
        self.assertEqual(found, None)
        self.assertNotEqual(seventy, self.avl.root.right.right)
        self.assertEqual(eighty, self.avl.root.right.right)

    def test_delete_leaf_node(self):
        """
                   40
                  /  \
                30    60
                /    /  \
              20    50   70
                          \
                           80
        """
        nodes = [50, 30, 40, 20, 70, 60, 80]
        for node in nodes:
            self.avl.insert(node)
        forty = self.avl.root
        thirty = forty.left
        twenty = thirty.left
        sixty = forty.right
        fifty = sixty.left
        found, _ = self.avl.find_node(twenty.key)
        self.assertEqual(twenty, found)
        self.avl.delete(twenty.key)
        found, _ = self.avl.find_node(twenty.key)
        self.assertEqual(found, None)
        self.assertEqual(thirty.left, None)
        # tree after rotations
        #     60
        #    /  \
        #   40   70
        #  /  \    \
        # 30  50   80
        found, _ = self.avl.find_node(fifty.key)
        self.assertEqual(fifty, found)
        self.avl.delete(fifty.key)
        found, _ = self.avl.find_node(fifty.key)
        self.assertEqual(found, None)
        self.assertEqual(self.avl.root, sixty)
        self.assertEqual(forty.right, None)

    def test_delete_root_node(self):
        """
                   40
                  /  \
                30    60
                /    /  \
              20    50   70
                          \
                           80
        """
        nodes = [50, 30, 40, 20, 70, 60, 80]
        for node in nodes:
            self.avl.insert(node)
        forty = self.avl.root
        sixty = forty.right
        fifty = sixty.left
        found, _ = self.avl.find_node(forty.key)
        self.assertEqual(found, forty)
        self.avl.delete(forty.key)
        found, _ = self.avl.find_node(forty.key)
        self.assertEqual(found, None)
        self.assertEqual(self.avl.root, fifty)
        self.assertEqual(fifty.right, sixty)

    def test_avl_integrity_with_random_delete_and_insert(self):
        """
        Test that the AVL tree maintains a height of log_n with random inserts
        and deletes.
        """
        options = ('INSERT', 'DELETE')
        node_count = 0
        node_map = {}
        for i in range(100):
            choice = random.choice(options)
            repeat = int(random.random() * 100)
            if choice == 'INSERT':
                for i in range(repeat):
                    node = int(random.random() * 1000)
                    node_map[node] = node_map.get(node, 0) + 1
                    self.avl.insert(node)
                    node_count += 1
                ordered = inorder_traversal(self.avl)
                self.assertEqual(len(ordered), node_count)
                log_n_height = math.ceil(math.log(node_count, 2))
                tree_height = self.avl.get_height(self.avl.root)
                self.assertTrue(
                    log_n_height - 1 <= tree_height <= log_n_height + 3)
                bal = self.avl.get_balance(self.avl.root)
                self.assertTrue(-1 <= bal <= 1)
            elif choice == 'DELETE':
                for i in range(repeat):
                    node = int(random.random() * 1000)
                    if node_map.get(node, 0) > 0:
                        self.avl.delete(node)
                        node_count -= 1
                        node_map[node] -= 1
                    else:
                        with self.assertRaises(Exception):
                            self.avl.delete(node)
                ordered = inorder_traversal(self.avl)
                self.assertEqual(len(ordered), node_count)
                if node_count > 0:
                    log_n_height = math.ceil(math.log(node_count, 2))
                    tree_height = self.avl.get_height(self.avl.root)
                    self.assertTrue(
                        log_n_height - 1 <= tree_height <= log_n_height + 3)
                bal = self.avl.get_balance(self.avl.root)
                self.assertTrue(-1 <= bal <= 1)
