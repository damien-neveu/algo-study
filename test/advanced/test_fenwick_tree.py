import unittest
from advanced.fenwick_tree import FenwickTree


class TestFenwickTree(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(0, FenwickTree(10).sum(5))

    def test_added_tree(self):
        tree = FenwickTree(24)
        tree.add(7, 30)
        tree.add(9, 45)
        tree.add(12, 56)
        tree.add(4, 12)
        tree.add(19, 34)
        tree.add(9, 10)
        self.assertEqual(97, tree.sum(9))

    def test_added_on_original_tree(self):
        original_tree = [0, 3, 6, 12, 3, 7, 99]
        tree = FenwickTree(len(original_tree), original_tree)
        tree.add(1, 5)
        tree.add(3, 8)
        tree.add(5, 11)
        self.assertEqual(34, tree.sum(3))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/advanced
