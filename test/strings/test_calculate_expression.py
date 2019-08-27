import unittest
from strings.calculate_expression import calculate


class TestCalculateExpression(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(calculate(""), 0)

    def test_simple_expression(self):
        self.assertEqual(calculate("1+2+3"), 6)

    def test_long_expression(self):
        self.assertEqual(calculate("1+4+(7-(1-5))+5"), 21)

    def test_long_expression_with_larger_ints(self):
        self.assertEqual(calculate("-23+12+(405-399-(123-125+10))-1111"), -1124)


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/strings -v
