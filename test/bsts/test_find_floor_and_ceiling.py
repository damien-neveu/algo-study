import unittest
from trees.node import Node
from bsts.find_floor_and_ceiling import find_floor_and_ceiling


class TestFindFloorAndCeiling(unittest.TestCase):
    bst = Node(10, Node(8, Node(7, Node(5), None), Node(9)), Node(14, Node(12), Node(17, Node(15), Node(19))))

    def test_find_in_empty_bst(self):
        self.assertEqual(None, find_floor_and_ceiling(10, None))

    def test_find_in_bst(self):
        self.assertEqual((12, 14), find_floor_and_ceiling(13, TestFindFloorAndCeiling.bst))

    def test_find_exact_value_in_bst(self):
        self.assertEqual((15, 15), find_floor_and_ceiling(15, TestFindFloorAndCeiling.bst))

    def test_find_too_large_value_in_bst(self):
        self.assertEqual(None, find_floor_and_ceiling(20, TestFindFloorAndCeiling.bst))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/bsts -v
