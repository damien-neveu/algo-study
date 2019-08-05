import unittest
from arrays.locate_smallest_sortable_window import locate_smallest_sortable_window


class TestLocateSmallestSortableWindow(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual([], locate_smallest_sortable_window([]))

    def test_sorted_array(self):
        self.assertEqual([None, None], locate_smallest_sortable_window([1,2,3,4,5]))

    def test_locate(self):
        self.assertEqual([1,3], locate_smallest_sortable_window([3,7,5,6,9]))
        self.assertEqual([2,4], locate_smallest_sortable_window([1,3,9,7,5]))


if __name__ == '__main__':
    unittest.main()
