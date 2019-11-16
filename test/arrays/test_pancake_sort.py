import unittest
from arrays.pancake_sort import pancake_sort_with_swap, pancake_sort


class TestPancakeSort(unittest.TestCase):

    single_elem_array = [10]

    sorted_array = [2, 3, 6, 7, 9]

    def build_unsorted_array(self):
        return [7, 3, 2, 9, 6]

    def test_one_elem_array_with_swap(self):
        self.assertEqual(self.single_elem_array, pancake_sort_with_swap(self.single_elem_array))

    def test_unsorted_array_with_swap(self):
        self.assertEqual(self.sorted_array, pancake_sort_with_swap(self.build_unsorted_array()))

    def test_one_elem_array(self):
        self.assertEqual(self.single_elem_array, pancake_sort(self.single_elem_array))

    def test_unsorted_array(self):
        self.assertEqual(self.sorted_array, pancake_sort(self.build_unsorted_array()))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/arrays -v
