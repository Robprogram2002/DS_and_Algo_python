from Miller_problemsolving.chapter6.binary_trees import BinaryTree


# shows a version of the preorder traversal written as an external function that takes a binary tree as a parameter.
# The external function is particularly elegant because our base case is simply to check if the tree exists.
# If the tree parameter is None, then the function returns without taking any action.

def preorder_traversal(btree: BinaryTree):
    if btree is None:
        return

    print(btree.get_root_val())
    preorder_traversal(btree.get_left_child())
    preorder_traversal(btree.get_right_child())


# We can also implement preorder as a method of the BinaryTree class


# The algorithm for the postorder traversal is nearly identical to preorder except that we move
# the call to print to the end of the function.

def postorder_traversal(btree: BinaryTree):
    if btree is None:
        return

    preorder_traversal(btree.get_left_child())
    preorder_traversal(btree.get_right_child())
    print(btree.get_root_val())


# In the inorder traversal we visit the left subtree, followed by the root, and finally the right subtree.
# Below we show our code for the inorder traversal. Notice that in all three of the traversal functions we are
# simply changing the position of the print statement with respect to the two recursive function calls.


def inorder_traversal(btree: BinaryTree):
    if btree is None:
        return

    inorder_traversal(btree.get_left_child())
    print(btree.get_root_val())
    inorder_traversal(btree.get_right_child())

