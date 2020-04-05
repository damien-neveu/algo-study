import unittest
from sort.find_in_rotated_sorted_array import find_elem


class MyTestCase(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(None, find_elem([], 1))

    def test_non_existing_value(self):
        self.assertEqual(None, find_elem([21, 23, 25, 33, 2, 4, 8, 12], 14))

    def test_existing_value(self):
        self.assertEqual(6, find_elem([21, 23, 25, 33, 2, 4, 8, 12], 8))


if __name__ == '__main__':
    unittest.main()

# python -m unittest discover test/sort -v
