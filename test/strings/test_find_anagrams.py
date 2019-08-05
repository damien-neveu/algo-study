import unittest
from strings.find_anagrams import find_anagrams_brute, find_anagrams


class TestFindAnagrams(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual([], find_anagrams_brute("", ""))

    def test_brute(self):
        self.assertEqual([0,3,4], find_anagrams_brute("ab", "abxaba"))

    def test_anagrams(self):
        self.assertEqual([1,7,15], find_anagrams("car", "acarartracgdcadcra"))


if __name__ == "__main__":
    unittest.main()
