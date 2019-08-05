import unittest
from google.knights_dialer import count_unique_numbers


class TestKnightsDialer(unittest.TestCase):

    def test_0_step(self):
        self.assertEqual(1, count_unique_numbers(1, 0))

    def test_1_step(self):
        self.assertEqual(2, count_unique_numbers(1, 1))

    def test_2_steps(self):
        self.assertEqual(6, count_unique_numbers(6, 2))

    def test_3_steps(self):
        self.assertEqual(15, count_unique_numbers(6, 3))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/google -v
