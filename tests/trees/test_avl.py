import random
import math
import unittest

from unittest.mock import MagicMock

from trees.bst.avl import AVLTree
from trees.traversal.inorder import inorder_traversal


class AVLTest(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def tearDown(self):
        del self.avl

    def assert_node_has_appropriate_balance(self, node):
        """
        Does an in order traversal to cover the entire tree and ensures that
        each node has a balance that falls between -1 to 1.
        """
        if node == None:
            return
        self.assert_node_has_appropriate_balance(node.left)
        self.assertTrue(-1 <= self.avl.get_balance(node) <= 1)
        self.assert_node_has_appropriate_balance(node.right)

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
        self.avl.handle_ll_rotation = MagicMock()
        a = [50, 40, 30]
        for node in a:
            self.avl.insert(node)
        self.avl.handle_ll_rotation.assert_called_with(None, self.avl.root)

    def test_handle_left_right_rotation(self):
        """
             50
            /
           30
            \
             40
        """
        self.avl.handle_lr_rotation = MagicMock()
        a = [50, 30, 40]
        for node in a:
            self.avl.insert(node)
        self.avl.handle_lr_rotation.assert_called_with(None, self.avl.root)

    def test_handle_left_left_imbalance_with_balanced_child_node(self):
        """
        Test left left imbalance on left heavy node whose child has a height > 1
        and whose balance = 0.

        Use 400 to avoid rotations when creating the tree.
        Delete 400 to create desired scenario.

        Note: The desired tree state can be resolved by a left left rotation
        or a left right rotation.

                                (desired tree state)     (should resolve to this)
                    100                 100                 70
                   /   \               /                   /  \
                 70     400    ==>   70          ==>      60   100
                /  \                /  \                       /
              60    80             60   80                    80
        """
        a = [100, 70, 400, 60, 80]
        for node in a:
            self.avl.insert(node)
        four_hundred = self.avl.root.right
        self.assertEqual(four_hundred.val, 400)
        self.avl.delete(four_hundred)
        self.assertEqual(self.avl.root.val, 70)
        self.assertEqual(self.avl.root.left.val, 60)
        self.assertEqual(self.avl.root.right.val, 100)
        self.assertEqual(self.avl.root.right.left.val, 80)

    def test_handle_right_right_imbalance_with_balanced_child_node(self):
        """
        Test right right imbalance on right heavy node whose child has a
        height > 1 and whose balance = 0.

        Use 60 to avoid rotations when creating the tree.
        Delete 60 to create desired scenario.

        Note: The desired tree state can be resolved by a right right rotation
        or a right left rotation.

                                (desired tree state)     (should resolve to this)
                    70                 70                   100
                   /   \                 \                 /   \
                 60     100    ==>       100      ==>    70    400
                       /   \            /   \              \
                      80   400        80    400            80
        """
        a = [70, 60, 100, 80, 400]
        for node in a:
            self.avl.insert(node)
        sixry = self.avl.root.left
        self.assertEqual(sixry.val, 60)
        self.avl.delete(sixry)
        self.assertEqual(self.avl.root.val, 100)
        self.assertEqual(self.avl.root.left.val, 70)
        self.assertEqual(self.avl.root.right.val, 400)
        self.assertEqual(self.avl.root.left.right.val, 80)

    def test_right_right_rotation(self):
        """
             50
              \
               60
                 \
                  70
        """
        self.avl.handle_rr_rotation = MagicMock()
        a = [50, 60, 70]
        for node in a:
            self.avl.insert(node)
        self.avl.handle_rr_rotation.assert_called_with(None, self.avl.root)

    def test_right_left_rotation(self):
        """
             50
              \
               70
              /
             60
        """
        self.avl.handle_rr_rotation = MagicMock()
        a = [50, 70, 60]
        for node in a:
            self.avl.insert(node)
        self.avl.handle_rr_rotation.assert_called_with(None, self.avl.root)

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
        found = self.avl.find_node(findable)
        self.assertEqual(findable, found.val)

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
        with self.assertRaises(Exception):
            found = self.avl.find_node(findable)

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
        found = self.avl.find_node(thirty.val)
        self.assertEqual(found, thirty)
        self.avl.delete(thirty)
        with self.assertRaises(Exception):
            found = self.avl.find_node(thirty.val)
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
        found = self.avl.find_node(seventy.val)
        self.assertEqual(found, seventy)
        self.avl.delete(seventy)
        with self.assertRaises(Exception):
            found = self.avl.find_node(seventy.val)
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
        found = self.avl.find_node(twenty.val)
        self.assertEqual(twenty, found)
        self.avl.delete(twenty)
        with self.assertRaises(Exception):
            found = self.avl.find_node(twenty.val)
        self.assertEqual(thirty.left, None)
        self.assertEqual(self.avl.root, sixty)
        # tree after rotations
        #     60
        #    /  \
        #   40   70
        #  /  \    \
        # 30  50   80
        found = self.avl.find_node(fifty.val)
        self.assertEqual(fifty, found)
        self.avl.delete(fifty)
        with self.assertRaises(Exception):
            found = self.avl.find_node(fifty.val)
        self.assertEqual(self.avl.root, sixty)
        self.assertEqual(forty.right, None)

    def test_delete_root_node(self):
        """
                   40                        50
                  /  \       after          /  \
                30    60    rotation      30    70
                /    /  \     ==>        /     /  \
              20    50   70             20   60    80
                          \
                           80
        """
        nodes = [50, 30, 40, 20, 70, 60, 80]
        for node in nodes:
            self.avl.insert(node)
        forty = self.avl.root
        sixty = forty.right
        fifty = sixty.left
        seventy = sixty.right
        found = self.avl.find_node(forty.val)
        self.assertEqual(found, forty)
        self.avl.delete(forty)
        with self.assertRaises(Exception):
            found = self.avl.find_node(forty)
        self.assertEqual(self.avl.root, fifty)
        self.assertEqual(fifty.right, seventy)

    def test_avl_integrity_with_inorder_traversal(self):
        """
        Tests that the AVLTree maintains the BST property.
        This is also a test to check that rotations perform as intended.
        """
        length = int(random.random() * 1000)
        nodes = []
        for i in range(length):
            node = int(random.random() * 1000)
            nodes.append(node)
            self.avl.insert(node)
        ordered = inorder_traversal(self.avl)
        self.assertEqual(ordered, sorted(nodes))

    def test_each_avl_node_is_balanced(self):
        """
        Tests that each node in the AVL tree has a balance that is either -1, 0,
        or 1.
        """
        length = int(random.random() * 1000)
        for i in range(length):
            node = int(random.random() * 1000)
            self.avl.insert(node)
        self.assert_node_has_appropriate_balance(self.avl.root)

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
                        found = self.avl.find_node(node)
                        self.avl.delete(found)
                        node_count -= 1
                        node_map[node] -= 1
                    else:
                        with self.assertRaises(Exception):
                            self.avl.find_node(node)
                ordered = inorder_traversal(self.avl)
                self.assertEqual(len(ordered), node_count)
                if node_count > 0:
                    log_n_height = math.ceil(math.log(node_count, 2))
                    tree_height = self.avl.get_height(self.avl.root)
                    self.assertTrue(
                        log_n_height - 1 <= tree_height <= log_n_height + 3)
                bal = self.avl.get_balance(self.avl.root)
                self.assertTrue(-1 <= bal <= 1)
