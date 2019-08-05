import unittest
from dynamic.climb_a_staircase import count_ways


class TestClimbAStaircase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, count_ways(1))

    def test_4(self):
        self.assertEqual(5, count_ways(4))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/dynamic -v
