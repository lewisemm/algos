import pytest

from bst import avl

@pytest.fixture
def avl_tree():
    return avl.AVLTree()

def test_insert(avl_tree):
    """
    Insert node and confirm it exists in AVL.
    """
    node = avl_tree.find(20)
    assert node is None
    avl_tree.insert(20)
    node = avl_tree.find(20)
    assert node.key == 20

def test_delete_non_existent_node(avl_tree):
    """
    Delete a node that does not exist in the AVL.
    """
    node = avl_tree.find(20)
    assert node is None
    node = avl_tree.delete(20)
    assert node == f'Key 20 does not exist in this tree'

def test_delete_leaf_root(avl_tree):
    """
      20 ===> None
    """
    node = avl_tree.find(20)
    assert node is None
    avl_tree.insert(20)
    node = avl_tree.find(20)
    assert node.key == 20
    avl_tree.delete(20)
    node = avl_tree.find(20)
    assert node is None

def test_delete_root_one_left_child(avl_tree):
    """
       20
       /   ===> 10
      10
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.delete(20)
    node = avl_tree.find(20)
    assert node is None
    node = avl_tree.find(10)
    assert node.key == 10
    node = avl_tree.find_parent(10)
    assert node is None

def test_delete_root_one_right_child(avl_tree):
    """
       20
         \  ===> 30
         30
    """
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.delete(20)
    node = avl_tree.find(20)
    assert node is None
    node = avl_tree.find(30)
    assert node.key == 30
    node = avl_tree.find_parent(30)
    assert node is None

def test_delete_root_two_children(avl_tree):
    """
        20
       /  \ 
      10   30
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(30)
    avl_tree.delete(20)
    node = avl_tree.find(20)
    assert node is None
    # right child is inorder successor
    node = avl_tree.find(30)
    assert node.key == 30
    parent = avl_tree.find_parent(30)
    assert parent is None
    # left child of original root becomes left child of new root
    node = avl_tree.find(10)
    assert node.key == 10
    parent = avl_tree.find_parent(10)
    assert parent.left_node.key == 10

def test_delete_root_deeper_successor(avl_tree):
    """
    Test delete root where successor is leftmost node in right subtree of root.

           20
          /  \ 
         10   40
              /
             30
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(30)
    avl_tree.delete(20)
    node = avl_tree.find(20)
    assert node is None
    # leftmost child of original root's right subtree is inorder successor
    parent = avl_tree.find_parent(30)
    assert parent is None
    # right child of original root is right child of successor
    node = avl_tree.find(30)
    assert node.right_node.key == 40

def test_delete_non_root_leaf_node(avl_tree):
    """
        20
       /  \ 
      10   30
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(30)
    avl_tree.delete(10)
    node = avl_tree.find(10)
    assert node is None
    # assert parent.left_node is None
    parent = avl_tree.find(20)
    assert parent.left_node is None

def test_delete_non_root_node_two_children(avl_tree):
    """
           20
          /  \ 
         10   40
             /  \ 
            30   50
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(30)
    avl_tree.insert(50)
    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    # assert immediate right child of deleted node is successor
    parent = avl_tree.find_parent(30)
    assert parent.key == 50

def test_delete_non_root_node_two_children_successor_deeper(avl_tree):
    """
    Test delete non root where successor is leftmost node in right subtree of
    root.

           20
          /  \ 
         10   40
        /    /  \ 
       5    30   70
           /    /  \ 
          25   50  80
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)

    avl_tree.insert(5)
    avl_tree.insert(30)
    avl_tree.insert(70)

    avl_tree.insert(25)
    avl_tree.insert(50)
    avl_tree.insert(80)

    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    # assert leftmost node of deleted node's right subtree is successor
    parent = avl_tree.find_parent(30)
    assert parent.key == 50

def test_delete_non_root_node_one_left_child(avl_tree):
    """
           20
          /  \ 
         10   40
             /
            30
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(30)
    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    # assert left child of deleted node is successor
    parent = avl_tree.find_parent(30)
    assert parent.key == 20

def test_delete_non_root_node_one_right_child(avl_tree):
    """
           20
          /  \ 
         10   40
               \ 
               50
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    # assert right child of deleted node is successor
    parent = avl_tree.find_parent(50)
    assert parent.key == 20

def test_delete_causes_ll_imbalance(avl_tree):
    """
    Delete 40, causing LL imbalance on 30.
             30
            /  \ 
           20   40
          / 
         10
    """
    avl_tree.insert(30)
    avl_tree.insert(20)
    avl_tree.insert(40)
    avl_tree.insert(10)
    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    parent = avl_tree.find_parent(30)
    assert parent.key == 20

def test_delete_causes_rr_imbalance(avl_tree):
    """
    Delete 10, causing RR imbalance on 20.
          20
         /  \  
        10   30
              \ 
               40
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.delete(10)
    node = avl_tree.find(10)
    assert node is None
    parent = avl_tree.find_parent(20)
    assert parent.key == 30

def test_delete_causes_rl_imbalance(avl_tree):
    """
    Delete 10, causing RL imbalance on 20.
          20
         /  \  
        10   40
             / 
            30
    """
    avl_tree.insert(20)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(30)
    avl_tree.delete(10)
    node = avl_tree.find(10)
    assert node is None
    parent = avl_tree.find_parent(20)
    assert parent.key == 30

def test_delete_causes_lr_imbalance(avl_tree):
    """
    Delete 40, causing LR imbalance on 30.
             30
            /  \ 
           10   40
            \ 
             20
    """
    avl_tree.insert(30)
    avl_tree.insert(10)
    avl_tree.insert(40)
    avl_tree.insert(20)
    avl_tree.delete(40)
    node = avl_tree.find(40)
    assert node is None
    parent = avl_tree.find_parent(30)
    assert parent.key == 20

def test_left_rotate(avl_tree):
    """
    10
     \              20
      20   ===>    /  \ 
       \          10   30
        30
    """
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    parent = avl_tree.find_parent(10)
    assert parent.key == 20
    parent = avl_tree.find_parent(30)
    assert parent.key == 20
    parent = avl_tree.find_parent(20)
    assert parent == None

def test_right_rotate(avl_tree):
    """
          30
         /            20
        20   ===>    /  \ 
       /           10   30
      10
    """
    avl_tree.insert(30)
    avl_tree.insert(20)
    avl_tree.insert(10)
    parent = avl_tree.find_parent(10)
    assert parent.key == 20
    parent = avl_tree.find_parent(30)
    assert parent.key == 20
    parent = avl_tree.find_parent(20)
    assert parent == None

def test_left_right_rotate(avl_tree):
    """
       30
      /            20
     10   ===>    /  \ 
       \         10   30
        20
    """
    avl_tree.insert(30)
    avl_tree.insert(10)
    avl_tree.insert(20)
    parent = avl_tree.find_parent(10)
    assert parent.key == 20
    parent = avl_tree.find_parent(30)
    assert parent.key == 20
    parent = avl_tree.find_parent(20)
    assert parent == None

def test_right_left_rotate(avl_tree):
    """
      10
        \            20
        30  ===>    /  \ 
        /         10   30
      20
    """
    avl_tree.insert(10)
    avl_tree.insert(30)
    avl_tree.insert(20)
    parent = avl_tree.find_parent(10)
    assert parent.key == 20
    assert parent.right_node.key == 30
    parent = avl_tree.find_parent(30)
    assert parent.key == 20
    parent = avl_tree.find_parent(20)
    assert parent == None
