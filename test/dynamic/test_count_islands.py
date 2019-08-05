import unittest
from dynamic.count_islands import count_islands


class TestCountIslands(unittest.TestCase):

    empty_grid = []
    empty_grid02 = [
        [],
        [],
        []
    ]

    four_islands = [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ]

    two_islands = [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1]
    ]

    def test_empty_graph(self):
        self.assertEqual(0, count_islands(self.empty_grid))
        self.assertEqual(0, count_islands(self.empty_grid02))

    def test_four_islands(self):
        self.assertEqual(4, count_islands(self.four_islands))

    def test_two_islands(self):
        self.assertEqual(2, count_islands(self.two_islands))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/dynamic -v
