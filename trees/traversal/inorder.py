def traverse(node, inorder):
    if node == None:
        return
    traverse(node.left, inorder)
    inorder.append(node.val)
    traverse(node.right, inorder)

def inorder_traversal(tree):
    current = tree.root
    inorder = []
    traverse(current, inorder)
    return inorder
