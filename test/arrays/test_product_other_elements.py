import unittest
from arrays.product_other_elements import product_other_elements, product_other_elements_no_divide


class TestProductOtherElements(unittest.TestCase):

    def test_empty_product(self):
        self.assertEqual([], product_other_elements([]))

    def test_empty_product_no_divide(self):
        self.assertEqual([], product_other_elements_no_divide([]))

    def test_product(self):
        self.assertEqual([120,60,40,30,24], product_other_elements([1,2,3,4,5]))
        self.assertEqual([2,3,6], product_other_elements([3,2,1]))

    def test_product_no_divide(self):
        self.assertEqual([120,60,40,30,24], product_other_elements_no_divide([1,2,3,4,5]))
        self.assertEqual([2,3,6], product_other_elements_no_divide([3,2,1]))


if __name__ == '__main__':
    unittest.main()