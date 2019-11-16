import unittest
from trees.insert_and_delete import insert_node
from trees.node import Node


class TestInsertAndDelete(unittest.TestCase):

    def test_insert(self):
        tree = Node(4, Node(2, Node(1), Node(3)), Node(7))
        expected_output = Node(4, Node(2, Node(1), Node(3)), Node(5, None, Node(7)))
        self.assertEqual(expected_output, insert_node(tree, 5))


if __name__ == "__main__":
    unittest.main()

