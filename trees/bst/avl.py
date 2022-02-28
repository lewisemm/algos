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
