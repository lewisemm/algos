class Node:
    def __init__(self, key):
        self.left_node = None
        self.right_node = None
        self.key = key
        self.height = 1

    def __str__(self):
        return f'<Node: {self.key}>'

    def __repr__(self):
        return f'<Node: {self.key}>'

    def is_leaf(self):
        return self.left_node == self.right_node == None
