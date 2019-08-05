import unittest
from arrays.next_permutation import next_permutation


class TestNextPermutation(unittest.TestCase):

    def test_empty_next_permutation(self):
        self.assertEqual([], next_permutation([]))

    def test_max_next_permutation(self):
        self.assertEqual([1, 2, 3, 4], next_permutation([4, 3, 2, 1]))

    def test_max_permutation(self):
        self.assertEqual([1, 7, 5, 1, 3, 8], next_permutation([1, 7, 3, 8, 5, 1]))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/arrays -v
