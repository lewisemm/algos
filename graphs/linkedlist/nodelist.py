from graphs.linkedlist.node import Node


class NodeList:
    def __init__(self):
        self.first = None
    
    def insert(self, index):
        if not self.first:
            self.first = Node(index)
            return self.first
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = Node(index)
        return current.next_node
    
    def adjacent(self):
        current = self.first
        while current:
            yield current
            current = current.next_node

    def __repr__(self):
        return f'<NodeList: {self.first}>'
