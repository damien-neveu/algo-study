import unittest
from heaps.running_median import get_running_medians


class TestRunningMedian(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual([], get_running_medians([]))

    def test_array_with_one_element(self):
        self.assertEqual([2], get_running_medians([2]))

    def test_get_running_medians(self):
        self.assertEqual([2, 1.5, 2, 3.5, 2, 2, 2], get_running_medians([2, 1, 5, 7, 2, 0, 5]))
        self.assertEqual([3, 8, 7, 6, 7, 10, 13, 17, 21, 17.5, 14, 17.5, 21, 22], get_running_medians([3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29]))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/heaps -v
