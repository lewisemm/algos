class Node:
    def __init__(self, key):
        self.left_node = None
        self.right_node = None
        self.key = key

    def __str__(self):
        return f'<Node: {self.key}>'

    def __repr__(self):
        return f'<Node: {self.key}>'

    def is_leaf(self):
        return self.left_node == self.right_node == None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if not self.root:
            self.root = node
            return self.root
        else:
            current = self.root
            while True:
                if node.key < current.key and current.left_node:
                    current = current.left_node
                elif node.key >= current.key and current.right_node:
                    current = current.right_node
                else:
                    break
            if node.key < current.key:
                current.left_node = node
            else:
                current.right_node = node
            return current

    def find(self, key):
        current = self.root
        while True:
            if key < current.key and current.left_node:
                current = current.left_node
            elif key > current.key and current.right_node:
                current = current.right_node
            else:
                break
        return current

    def delete(self, key):
        parent  = None
        current = self.root

        # find the node to be deleted and its parent
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left_node
            else:
                current = current.right_node

        if not current:
            return f'Node with key: {key} does not exist.'

        # handles deleting a root node where children < 2
        if not parent:
            if not current.left_node or not current.right_node:
                temp = current.left_node if current.left_node else current.right_node
                current.key = temp.key if temp else None
                current.left_node = temp.left_node if temp else None
                current.right_node = temp.right_node if temp else None
                return
        if current.left_node and not current.right_node:
            if current.key == parent.left_node.key:
                parent.left_node = current.left_node
            else:
                parent.right_node = current.left_node
            current = None
        elif current.right_node and not current.left_node:
            if current.key == parent.right_node.key:
                parent.right_node = current.right_node
            else:
                parent.left_node = current.right_node
            current = None
        elif not current.left_node and not current.right_node:
            if current.key == parent.left_node.key:
                parent.left_node = None
            else:
                parent.right_node = None
            current = None
        # when node to be deleted has two children
        else:
            successor = current.right_node
            successor_parent = current
            while successor.left_node:
                successor_parent = successor
                successor = successor.left_node
            if successor_parent.right_node and \
                successor_parent.right_node.key == successor.key:
                    successor_parent.key = successor.key
                    successor_parent.right_node = successor.right_node
                    successor = None
            else:
                successor_parent.left_node = successor.right_node
                current.key = successor.key
                successor = None

    def in_order_traversal(self):
        current = self.root
        stack = []

        while True:
            if current:
                stack.append(current)
                current = current.left_node
            elif stack:
                current = stack.pop()
                print(current)
                current = current.right_node
            else:
                break

    def pre_order_traversal(self):
        stack1 = [self.root]

        while stack1:
            current = stack1.pop()
            print(current)
            if current.right_node:
                stack1.append(current.right_node)
            if current.left_node:
                stack1.append(current.left_node)

    def post_order_traversal(self):
        stack1 = [self.root]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left_node:
                stack1.append(current.left_node)
            if current.right_node:
                stack1.append(current.right_node)

        while stack2:
            node = stack2.pop()
            print(node)



def deleter(bst, node, find_parent):
    print('-' * 80)
    print('in_order_traversal before removal')
    print('-' * 80)
    bst.in_order_traversal()
    deleted = bst.delete(node)
    print('-' * 80)
    print(f'node to delete is {deleted}')
    print('-' * 80)
    print('-' * 80)
    print('\nin_order_traversal after removal\n')
    bst.in_order_traversal()
    print('-' * 80)
    print('-' * 80)
    print(f'find_parent of {find_parent}')
    find_parent = bst.find_parent(find_parent)
    print(f'parent is {find_parent}')
    print('-' * 80)
    print('\n\n')

bst = BinarySearchTree()
root = bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(10)
bst.insert(14)
bst.insert(13)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(9.5)

deleter(bst, 8, 10)
deleter(bst, 6, 7)
deleter(bst, 10, 14)
deleter(bst, 9.5, 9.5)
deleter(bst, 13, 14)
deleter(bst, 7, 4)
deleter(bst, 9, 3)
deleter(bst, 14, 3)

# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)
# bst.insert(10)
# bst.insert(45)
# bst.insert(51)
# deleter(bst, 70, 60)
# deleter(bst, 50, 51)
# deleter(bst, 80, 60)
# deleter(bst, 40, 20)
# deleter(bst, 20, 10)
# deleter(bst, 40, 45)
