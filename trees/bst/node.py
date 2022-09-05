class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left == self.right == None

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return id(self) == id(other)

    def __repr__(self):
        return f'<TreeNode: {self.val}>'
