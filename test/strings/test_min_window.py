import unittest
from strings.min_window import min_window


class TestMinWindow(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual("", min_window("hello", ""))

    def test_pattern_longer_than_string(self):
        self.assertEqual(None, min_window("hello", "patternTooLong"))

    def test_pattern_does_not_exist_in_str(self):
        self.assertEqual(None, min_window("abcdefgh", "xyz"))

    def test_valid_01(self):
        self.assertEqual("t stri", min_window("this is a test string", "tist"))

    def test_valid_02(self):
        self.assertEqual("ADObEc", min_window("ADObEcODEBANC", "Abc"))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/strings -v
