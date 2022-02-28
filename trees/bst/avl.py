from trees.bst.node import Node

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a new `Node` object into the tree.
        """
        if self.root == None:
            node = Node(key)
            self.root = node
            return
        current = self.root
        ancestors = []

        while current:
            ancestors.append(current)
            if key < current.key:
                current = current.left
            else:
                current = current.right

        node = Node(key)
        parent = ancestors[-1] if ancestors else None
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.rebalance_tree(ancestors)

    def find_node(self, key):
        current = self.root
        ancestors = []
        while current:
            if current.key == key:
                break
            ancestors.append(current)
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current, ancestors

    def is_leaf(self, node):
        return node.left == node.right == None

    def find_successor(self, node):
        parent = node
        successor = node.right
        while successor.left:
            parent = successor
            successor = successor.left
        return successor, parent

    def rebalance_tree(self, ancestors):
        while ancestors:
            anc = ancestors.pop()
            anc_parent = ancestors[-1] if ancestors else None
            bal = self.get_balance(anc)
            if bal >= 2:
                # LL or LR
                skew = self.get_balance(anc.left)
                if skew >= 1:
                    # LL
                    self.left_left_rotation(anc.left, anc, anc_parent)
                elif skew <= -1:
                    # LR
                    self.left_right_rotation(anc.left.right, anc.left, anc)
                    self.left_left_rotation(anc.left, anc, anc_parent)
            elif bal <= -2:
                # RR or RL
                skew = self.get_balance(anc.right)
                if skew <= -1:
                    # RR
                    self.right_right_rotation(anc.right, anc, anc_parent)
                elif skew >= 1:
                    # RL
                    self.right_left_rotation(anc.right.left, anc.right, anc)
                    self.right_right_rotation(anc.right, anc, anc_parent)

    def get_height(self, node):
        if node == None:
            return -1
        return 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def get_balance(self, node):
        left_height = self.get_height(node.left) if node else 0
        right_height = self.get_height(node.right) if node else 0
        return left_height - right_height

    def left_left_rotation(self, node, parent, grand_parent):
        branch = None
        if grand_parent:
            if parent == grand_parent.left:
                branch = 'L'
            elif parent == grand_parent.right:
                branch = 'R'
        node_right = node.right
        node.right = parent
        parent.left = node_right
        if branch == 'L':
            grand_parent.left = node
        elif branch == 'R':
            grand_parent.right = node
        else:
            # branch is None and node is the new root.
            # insert 50, 60, 30, 40, 20, 10 respectively to test this.
            self.root = node

    def left_right_rotation(self, node, parent, grand_parent):
        branch = None
        if grand_parent:
            if parent == grand_parent.left:
                branch = 'L'
            elif parent == grand_parent.right:
                branch = 'R'
        node_left = node.left
        node.left = parent
        parent.right = node_left
        if branch == 'L':
            grand_parent.left = node
        elif branch == 'R':
            grand_parent.right = node
        else:
            # branch is None and node is the new root.
            # insert 40, 20, 5, 30, 25 respectively to test this.
            self.root = node

    def right_right_rotation(self, node, parent, grand_parent):
        branch = None
        if grand_parent:
            if parent == grand_parent.left:
                branch = 'L'
            elif parent == grand_parent.right:
                branch = 'R'
        node_left = node.left
        node.left = parent
        parent.right = node_left
        if branch == 'L':
            grand_parent.left = node
        elif branch == 'R':
            grand_parent.right = node
        else:
            # branch is None and node is the new root.
            # insert 50, 60, 70 respectively to test this
            self.root = node

    def right_left_rotation(self, node, parent, grand_parent):
        branch = None
        if grand_parent:
            if parent == grand_parent.left:
                branch = 'L'
            elif parent == grand_parent.right:
                branch = 'R'
        node_right = node.right
        node.right = parent
        parent.left = node_right
        if branch == 'L':
            grand_parent.left = node
        elif branch == 'R':
            grand_parent.right = node
        else:
            self.root = node
