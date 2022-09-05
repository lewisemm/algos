from trees.bst.node import TreeNode

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = TreeNode(val)
        if self.root == None:
            self.root = node
            return
        ancestors = self.get_insert_ancestors(node)
        parent = ancestors[-1]
        if node < parent:
            parent.left = node
        else:
            parent.right = node
        self.rebalance_tree(ancestors)

    def rebalance_tree(self, ancestors):
        while ancestors:
            anc = ancestors.pop()
            parent = ancestors[-1] if ancestors else None
            skew = self.get_balance(anc)
            if skew > 1:
                # ll imbalance or lr imbalance
                child_skew = self.get_balance(anc.left)
                if child_skew == 1:
                    self.handle_ll_rotation(parent, anc)
                elif child_skew == -1:
                    self.handle_lr_rotation(parent, anc)
            elif skew < -1:
                # rr imbalance or rl imbalance
                child_skew = self.get_balance(anc.right)
                if child_skew == -1:
                    # rr imbalance
                    self.handle_rr_rotation(parent, anc)
                elif child_skew == 1:
                    # rl imbalance
                    self.handle_rl_rotation(parent, anc)

    def get_insert_ancestors(self, node):
        current = self.root
        ancestors = []
        while current:
            ancestors.append(current)
            if node < current:
                current = current.left
            elif node >= current:
                current = current.right
        return ancestors

    def get_balance(self, node):
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return left_height - right_height

    def get_height(self, node):
        if node == None:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def handle_rr_rotation(self, parent, node):
        two = node.right
        temp = two.left
        two.left = node
        node.right = temp
        if parent == None:
            self.root = two
        else:
            if node == parent.left:
                parent.left = two
            elif node == parent.right:
                parent.right = two

    def handle_rl_rotation(self, parent, node):
        two = node.right
        three = two.left
        temp = three.right
        three.right = two
        two.left = temp
        node.right = three
        self.handle_rr_rotation(parent, node)

    def handle_ll_rotation(self, parent, node):
        two = node.left
        temp = two.right
        two.right = node
        node.left = temp
        if parent == None:
            self.root = two
        else:
            if node == parent.left:
                parent.left = two
            elif node == parent.right:
                parent.right = two

    def handle_lr_rotation(self, parent, node):
        two = node.left
        three = two.right
        temp = three.left
        node.left = three
        three.left = two
        two.right = temp
        self.handle_ll_rotation(parent, node)

    def delete(self, node):
        ancestors = self.search_ancestors(node)
        parent = ancestors[-1] if ancestors else None
        if node.is_leaf():
            if parent == None:
                self.root = None
            else:
                if node == parent.left:
                    parent.left = None
                elif node == parent.right:
                    parent.right = None
            del node
        elif node.left != None and node.right == None:
            if parent == None:
                self.root = node.left
            else:
                if node == parent.left:
                    parent.left = node.left
                elif node == parent.right:
                    parent.right = node.left
            del node
        elif node.right != None:
            ios, ios_parent = self.inorder_successor(node)
            if node == ios_parent:
                # successor is node.right
                ios.left = node.left
                if parent == None:
                    self.root = ios
                else:
                    if node == parent.left:
                        parent.left = ios
                    elif node == parent.right:
                        parent.right = ios
                del node
            else:
                ios_parent.left = ios.right
                ios.right = node.right
                ios.left = node.left
                if parent == None:
                    self.root = ios
                elif parent != None:
                    if node == parent.left:
                        parent.left = ios
                    elif node == parent.right:
                        parent.right = ios
                del node
        self.rebalance_tree(ancestors)

    def inorder_successor(self, node):
        ios = node.right
        ios_parent = node
        while ios.left:
            ios_parent = ios
            ios = ios.left
        return ios, ios_parent

    def search_ancestors(self, node):
        current = self.root
        ancestors = []
        while current:
            if current == node:
                break
            ancestors.append(current)
            if node < current:
                current = current.left
            else:
                current = current.right
        return ancestors

    def find_node(self, val):
        current = self.root
        while current:
            if current.val == val:
                return current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        raise Exception(f'<Node: {val}> not found.')

    def inorder_traversal(self):
        current = self.root
        print()
        self.__inorder_traversal(current)
        print()

    def __inorder_traversal(self, node):
        if node == None:
            return
        self.__inorder_traversal(node.left)
        print(node)
        self.__inorder_traversal(node.right)
