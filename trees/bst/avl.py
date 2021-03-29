from bst.node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return self.root
        else:
            current = self.root
            ancestors = []
            while current:
                ancestors.append(current)
                if key < current.key:
                    current = current.left_node
                else:
                    current = current.right_node
            node = Node(key)
            parent = ancestors[-1]
            if key < parent.key:
                parent.left_node = node
            else:
                parent.right_node = node
            while ancestors:
                anc = ancestors.pop()
                anc.height = 1 + max(
                    self.get_height(anc.left_node),
                    self.get_height(anc.right_node)
                )
                balance = self.get_balance(anc)
                # LL imbalance
                if balance > 1 and key < anc.left_node.key:
                    self.right_rotate(anc)
                # RR imbalance
                elif balance < -1 and key > anc.right_node.key:
                    self.left_rotate(anc)
                # LR imbalance
                elif balance > 1 and key > anc.left_node.key:
                    self.left_rotate(anc.left_node)
                    self.right_rotate(anc)
                # RL imbalance
                elif balance < -1 and key < anc.right_node.key:
                    self.right_rotate(anc.right_node)
                    self.left_rotate(anc)
            return node

    def delete(self, key):
        ancestors = []
        current = self.root
        while current and current.key != key:
            ancestors.append(current)
            if key < current.key:
                current = current.left_node
            else:
                current = current.right_node
        if not current:
            return f'Key {key} does not exist in this tree'
        if not ancestors:
            # dealing with the root node
            if current.is_leaf():
                self.root = None
                return
            # root has one child
            if not current.left_node or not current.right_node:
                temp = current.left_node if current.left_node else \
                    current.right_node
                current.key = temp.key if temp else None
                current.left_node = temp.left_node if temp else None
                current.right_node = temp.right_node if temp else None
                return
            # root has two children
            else:
                successor = current.right_node
                successor_parent = None
                ancestors.append(successor)
                while successor.left_node:
                    successor_parent = successor
                    ancestors.append(successor)
                    successor = successor.left_node
                if not successor_parent:
                    current.right_node = successor.right_node
                    current.key = successor.key
                else:
                    current.key = successor.key
                    successor_parent.left_node = successor.right_node
            
        else:
            parent = ancestors[-1]
            if parent.left_node and key == parent.left_node.key:
                current = parent.left_node
            else:
                current = parent.right_node
            
            if current.is_leaf():
                if parent.left_node and current.key == parent.left_node.key:
                    parent.left_node = None
                else:
                    parent.right_node = None
            elif current.left_node and not current.right_node:
                if parent.left_node and current.key == parent.left_node.key:
                    parent.left_node = current.left_node
                else:
                    parent.right_node = current.left_node
            elif current.right_node and not current.left_node:
                if parent.left_node and key == parent.left_node.key:
                    parent.left_node = current.right_node
                else:
                    parent.right_node = current.right_node
            elif current.left_node and current.right_node:
                successor = current.right_node
                successor_parent = current
                while successor.left_node:
                    successor_parent = successor
                    successor = successor.left_node
                # when successor is right next to node being deleted
                if successor_parent.key == current.key:
                    current.key = successor.key
                    current.right_node = successor.right_node
                # when successor is not directly referenced by node being deleted
                else:
                    current.key = successor.key
                    successor_parent.left_node = successor.right_node

        while ancestors:
            anc = ancestors.pop()
            anc.height = 1 + max(
                self.get_height(anc.left_node),
                self.get_height(anc.right_node)
            )
            balance = self.get_balance(anc)

            # LL imbalance
            if balance > 1 and self.get_balance(anc.left_node) >= 0:
                self.right_rotate(anc)
            # RR imbalance
            elif balance < -1 and self.get_balance(anc.right_node) <= 0:
                self.left_rotate(anc)
            # LR imbalance
            elif balance > 1 and self.get_balance(anc.left_node) < 0:
                self.left_rotate(anc.left_node)
                self.right_rotate(anc)
            # RL imbalance
            elif balance < -1 and self.get_balance(anc.right_node) > 0:
                self.right_rotate(anc.right_node)
                self.left_rotate(anc)

    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_node) - self.get_height(node.right_node)

    def right_rotate(self, node):
        middle_node = node.left_node
        node.height = 1 + max(
            self.get_height(middle_node.right_node),
            self.get_height(node.right_node)
        )
        middle_node.height = 1 + max(
            self.get_height(middle_node.left_node),
            self.get_height(middle_node.right_node) + 1
        )
        middle_node_r_child = middle_node.right_node
        middle_node.right_node = node
        node.left_node = middle_node_r_child
        parent = self.find_parent(node.key)
        if parent:
            if parent.left_node and node.key == parent.left_node.key:
                parent.left_node = middle_node
            else:
                parent.right_node = middle_node
        else:    
            self.root = middle_node
            
        return node
    
    def left_rotate(self, node):
        middle_node = node.right_node
        middle_node_l_child = middle_node.left_node
        node.height = 1 + max(
            self.get_height(node.left_node),
            self.get_height(middle_node.left_node)
        )
        middle_node.height = 1 + max(
            self.get_height(middle_node.left_node) + 1,
            self.get_height(middle_node.right_node)
        )
        middle_node.left_node = node
        node.right_node = middle_node_l_child
        parent = self.find_parent(node.key)
        if parent:
            if parent.left_node and parent.left_node.key == node.key:
                parent.left_node = middle_node
            else:
                parent.right_node = middle_node
        else:
            self.root = middle_node

    def find(self, key):
        current = self.root
        while current:
            if key < current.key:
                current = current.left_node
            elif key > current.key:
                current = current.right_node
            else:
                break
        return current

    def find_parent(self, key):        
        parent = None
        current = self.root
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left_node
            else:
                current = current.right_node
        if not current:
            return f'Key {key} not found.'
        return parent

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
