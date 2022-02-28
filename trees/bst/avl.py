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
