
def count_univals(root):
    total_count, _ = count_unival_trees(root)
    return total_count


def count_unival_trees(node):
    if node is None:
        return 0, True
    left_count, is_left_unival = count_unival_trees(node.left)
    right_count, is_right_unival = count_unival_trees(node.right)
    if node.left is not None and node.left.data != node.data or\
        node.right is not None and node.right.data != node.data or\
        is_left_unival is False or is_right_unival is False:
        return left_count + right_count, False
    return 1 + left_count + right_count, True


def count_univals_brute(root):
    current_count = 0
    if root is None:
        return current_count
    elif is_unival(root):
        current_count = 1
    return current_count + count_univals_brute(root.left) + count_univals_brute(root.right)


def is_unival(root):
    if root is None:
        return False
    v = root.data
    return (root.left is None or all_nodes_have_value(root.left, v))\
        and (root.right is None or all_nodes_have_value(root.right, v))


def all_nodes_have_value(node, v):
    if node is None:
        return True
    else:
        return node.data == v\
           and all_nodes_have_value(node.left, v)\
           and all_nodes_have_value(node.right, v)

