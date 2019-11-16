# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of "+", "−", "∗", or "/".
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +   +
#  / \ / \
# 3  2 4  5
# You should return 45, as it is (3 + 2) * (4 + 5)


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def evaluate_arithmetic_expression(tree_node):
    if tree_node.val.isnumeric():
        return int(tree_node.val)
    elif tree_node.val == "+":
        return evaluate_arithmetic_expression(tree_node.left) + evaluate_arithmetic_expression(tree_node.right)
    elif tree_node.val == "-":
        return evaluate_arithmetic_expression(tree_node.left) - evaluate_arithmetic_expression(tree_node.right)
    elif tree.val == "/":
        return evaluate_arithmetic_expression(tree_node.left) / evaluate_arithmetic_expression(tree_node.right)
    elif tree_node.val == "*":
        return evaluate_arithmetic_expression(tree_node.left) * evaluate_arithmetic_expression(tree_node.right)


if __name__ == "__main__":
    tree = TreeNode("*", TreeNode("+", TreeNode("3"), TreeNode("2")), TreeNode("+", TreeNode("4"), TreeNode("5")))
    res = evaluate_arithmetic_expression(tree)
    print("res={}".format(res))
