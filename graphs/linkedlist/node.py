class Node:
    def __init__(self, index):
        self.index = index
        self.next_node = None

    def __repr__(self):
        return f'<Node: {self.index}>'
