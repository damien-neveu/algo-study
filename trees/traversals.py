from trees.node import Node
from typing import List
from collections import deque


def depth_first_in_order(root: Node) -> List:
    res = []

    def recurse(node):
        if node is not None:
            recurse(node.left)
            res.append(node.data)
            recurse(node.right)

    recurse(root)
    return res


def depth_first_pre_order(root: Node) -> List:
    return []


def depth_first_post_order(root: Node) -> List:
    return []


def breadth_first(root: Node) -> List:
    res, q = [], deque()
    q.append(root)
    while len(q) > 0:
        el = q.popleft()
        if el.left is not None:
            q.append(el.left)
        if el.right is not None:
            q.append(el.right)
        res.append(el.data)
    return res

