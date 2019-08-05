import unittest
from arrays.calculate_max_subarray_sum import brute_calc_max_subarray_sum, calc_max_subarray_sum


class TestCalcMaxSubarraySum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(0, calc_max_subarray_sum([]))

    def test_negative_array(self):
        self.assertEqual(0, calc_max_subarray_sum([-5, -1, -8, -9]))

    def test_array(self):
        self.assertEqual(137, calc_max_subarray_sum([34, -50, 42, 14, -5, 86]))
        self.assertEqual(50, calc_max_subarray_sum([-10, -50, 15, 35, -12]))


if __name__ == '__main__':
    unittest.main()

# python -m unittest discover test/arrays -v
