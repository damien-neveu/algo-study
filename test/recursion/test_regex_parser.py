import unittest
from recursion.regex_parser import is_match


class TestRegexParser(unittest.TestCase):

    def test_incomplete_regex(self):
        self.assertEqual(False, is_match("aa", "a"))

    def test_exact_match_regex(self):
        self.assertEqual(True, is_match("aa", "aa"))

    def test_with_a_dot_regex(self):
        self.assertEqual(True, is_match("abc", "a.c"))

    def test_with_a_star_regex(self):
        self.assertEqual(True, is_match("abbb", "ab*"))

    def test_with_a_star_then_a_dot_regex(self):
        self.assertEqual(True, is_match("acd", "ab*c."))

    def test_with_a_dot_star_regex(self):
        self.assertEqual(True, is_match("acdxyz", "a.*z"))

    def test_with_a_dot_star_regex_not_matching(self):
        self.assertEqual(False, is_match("acdxyz", "a.*Q"))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/recursion -v

