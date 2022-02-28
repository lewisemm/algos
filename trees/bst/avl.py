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

    def delete(self, key):
        node, ancestors = self.find_node(key)
        if not node:
            raise Exception(f'Key {key} does not exist in this tree')
        if len(ancestors) == 0:
            if self.is_leaf(node):
                self.root = None
            elif not node.left or not node.right:
                temp = node.left if node.left else node.right
                self.root = temp
            elif node.left and node.right:
                successor, successor_parent = self.find_successor(node)
                successor_right = successor.right
                successor.left = node.left
                successor.right = node.right
                self.root = successor
                if successor_parent.left == successor:
                    successor_parent.left = successor_right
                elif successor_parent.right == successor:
                    successor_parent.right = successor_right
        else:
            node_parent = ancestors[-1]
            if self.is_leaf(node):
                if node_parent.left == node:
                    node_parent.left = None
                elif node_parent.right == node:
                    node_parent.right = None
                else:
                    raise Exception('How!? How!?')
            else:
                if node.left and not node.right:
                    if node_parent.left == node:
                        node_parent.left = node.left
                    elif node_parent.right == node:
                        node_parent.right = node.left
                elif not node.left and node.right:
                    if node_parent.left == node:
                        node_parent.left = node.right
                    elif node_parent.right == node:
                        node_parent.right = node.right
                elif node.left and node.right:
                    successor, successor_parent = self.find_successor(node)
                    if successor_parent == node:
                        if node_parent.left == node:
                            node_parent.left = successor
                        elif node_parent.right == node:
                            node_parent.right = successor
                        successor.left = node.left
                    else:
                        successor_parent.left = successor.right
                        successor.right = node.right
                        successor.left = node.left
                        if node_parent.left == node:
                            node_parent.left = successor
                        elif node_parent.right == node:
                            node_parent.right = successor
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
