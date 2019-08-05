import unittest
from trees.count_unival_trees import count_univals_brute, is_unival, count_univals
from trees.node import Node


class TestCountUnivalTrees(unittest.TestCase):

    def test_is_unival(self):
        self.assertEqual(True, is_unival(Node(1, Node(1, Node(1)), Node(1))))

    def test_count_univals_single_node(self):
        self.assertEqual(1, count_univals(Node(0)))

    def test_count_univals_multi_nodes(self):
        self.assertEqual(5, count_univals(Node(0, Node(0), Node(0, Node(1, Node(1), Node(1)), Node(0)))))
        self.assertEqual(3, count_univals(Node('a', Node('a'), Node('a', Node('a'), Node('a', None, Node('b'))))))


if __name__ == "__main__":
    unittest.main()
