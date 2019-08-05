import unittest
from arrays.find_num_smaller_to_the_right import find_smaller_to_right_brute, find_smaller_to_right


class TestFindNumSmallerToTheRight(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual([], find_smaller_to_right_brute([]))

    def test_brute(self):
        self.assertEqual([1, 1, 2, 1, 0], find_smaller_to_right_brute([3, 4, 9, 6, 1]))

    def test_optimal(self):
        self.assertEqual([3, 1, 1, 1, 1, 0], find_smaller_to_right([7, 3, 6, 9, 11, 1]))


if __name__ == '__main__':
    unittest.main()

