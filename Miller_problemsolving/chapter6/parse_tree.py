from Miller_problemsolving.chapter3.Stacks import Stack
from Miller_problemsolving.chapter6.binary_trees import BinaryTree
import operator


# The four rules for building a parse tree are coded as the first four clauses of the if statement77
#  In each case you can see that the code implements the rule
# The only error checking we do in this function is in the else clause where a ValueError exception will be raised if
# we get a token from the list that we do not recognize.

def build_parse_tree(math_expr: str):
    char_list = math_expr.split()
    parent_stack = Stack()
    tree = BinaryTree('')
    parent_stack.push(tree)
    current_tree = tree

    for char in char_list:
        if char == '(':
            current_tree.insert_left('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif char in ['+', '-', '*', '/']:
            current_tree.set_root_val(char)
            current_tree.insert_right('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif char == ')':
            current_tree = parent_stack.pop()

        elif char not in ['+', '-', '*', '/', ')']:
            try:
                # char is a number
                current_tree.set_root_val(int(char))
                parent = parent_stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(char))

    return tree


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
pt_2 = build_parse_tree("( 3 + ( 4 * 5 ) )")

pt.traverse_preorder()
print('----------------------------------')
pt_2.traverse_preorder()
print('----------------------------------')

opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def evaluate_pt(ptree: BinaryTree):
    #  First, we obtain references to the left and the right children of the current node.
    left_call = ptree.get_left_child()
    right_call = ptree.get_right_child()

    if left_call and right_call:
        # If the current node is not a leaf node, look up the operator in the current node and apply it to the results
        # from recursively evaluating the left and right children.
        fn = opers[ptree.get_root_val()]
        return fn(evaluate_pt(left_call), evaluate_pt(right_call))
    else:
        # If both the left and right children evaluate to None, then we know that the current node is really a leaf node
        return ptree.get_root_val()


# When we first call evaluate, we pass the root of the entire tree as the parameter

print(evaluate_pt(pt))
print(evaluate_pt(pt_2))


# What we are doing is evaluating the left subtree, evaluating the right subtree, and combining
# them in the root through the function call to an operator. Assume that our binary tree is going to store only
# expression tree data. Let’s rewrite the evaluation function, but model it even more closely on the postorder code.
# except that instead of printing the key at the end of the function, we return it
# This allows us to save the values returned from the recursive calls
# We then use these saved values along with the operator

def postorder_evaluate(ptree: BinaryTree):
    res1 = None
    res2 = None

    if ptree is None:
        return

    res1 = postorder_evaluate(ptree.get_left_child())
    res2 = postorder_evaluate(ptree.get_right_child())
    if res1 and res2:
        return opers[ptree.get_root_val()](res1, res2)
    else:
        return ptree.get_root_val()


print("----------------------------")
print(postorder_evaluate(pt))
print(postorder_evaluate(pt_2))


# If we perform a simple inorder traversal of a parse tree we get our original expression back, without any parentheses.
# Let’s modify the basic inorder algorithm to allow us to recover the fully parenthesized version of the expression.
# The only modifications we will make to the basic template are as follows: print a left parenthesis before the
# recursive call to the left subtree, and print a right parenthesis after the recursive call to the right subtree.

def print_expr(btree: BinaryTree):
    if btree is None:
        return
    str_val = ""
    if btree.get_root_val() in ['+', '-', '*', '/', ')']:
        str_val = '(' + print_expr(btree.get_left_child())
        str_val = str_val + str(btree.get_root_val())
        str_val = str_val + print_expr(btree.get_right_child()) + ')'
    else:
        str_val = str_val + str(btree.get_root_val())

    return str_val


print("----------------------------")
print(print_expr(pt))
print(print_expr(pt_2))

# Notice that the print_exp function as we have implemented it puts parentheses around each number. While not
# incorrect, the parentheses are clearly not needed.
