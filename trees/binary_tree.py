class Node(object):
    """
    This class represents a node in a binary tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_leaf(self):
        return self.left == self.right == None
    
    def navigate(self, value):
        if value > self.value:
            return self.right
        elif value <= self.value:
            return self.left
    
    def __repr__(self):
        return '<Node: {}>'.format(self.value)


class BinaryTree(object):
    """
    This class encapsulates a binary tree and contains methods to perform
    CRUD operations on it.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Adds a node to the binary tree.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            while current_node:
                temp = current_node.navigate(value)
                if  temp is not None:
                    current_node = temp
                else:
                    break
            if current_node.value >= value:
                current_node.left = Node(value)
            else:
                current_node.right = Node(value)

    def search(self, value):
        """
        Searches the binary tree for a node that contains the value `value`.

        Returns `None` if value isn't found in the binary tree.
        """
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return current_node
            temp = current_node.navigate(value)
            if temp is not None:
                current_node = temp
            else:
                return None

    def inorder_traversal(self, node):
        """
        Displays all the nodes in the binary tree using inorder traversal.
        """
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.value)
        self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """
        Displays all the nodes in the binary tree using preorder traversal.
        """
        if node is None:
            return
        print(node.value)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """
        Displays all the nodes in the binary tree using postorder traversal.
        """
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value)
        
    def breadth_first(self):
        """
        Display all the nodes in the binary tree using the breadth first
        traversal.
        """
        q = [self.root]
        while len(q):
            current = q.pop(0)
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
 

b = BinaryTree()
b.insert(37)
b.insert(61)
b.insert(62)
b.insert(32)
b.insert(31)
b.insert(33)
b.insert(32)
print('Results for Search 42: {}'.format(b.search(42)))
print('Results for Search 33: {}\n\n'.format(b.search(33)))

print('breadth first traversal\n')
b.breadth_first()
print('inorder traversal\n')
b.inorder_traversal(b.root)
print('preorder traversal\n')
b.preorder_traversal(b.root)
print('postorder traversal\n')
b.postorder_traversal(b.root)
