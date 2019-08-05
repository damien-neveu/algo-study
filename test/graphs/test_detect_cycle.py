import unittest
from graphs.detect_cycle import cycle_exists


class TestDetectCycle(unittest.TestCase):

    empty_graph = {}
    graph_with_no_cycle = {
        '0': ['1', '3', '5'],
        '1': ['0', '2'],
        '2': ['1'],
        '3': ['0', '4'],
        '4': ['3'],
        '5': ['0']
    }
    graph_with_cycle = {
        '0': ['1', '2', '3'],
        '1': ['0', '2'],
        '2': ['0', '1'],
        '3': ['0', '4'],
        '4': ['3']
    }

    def test_empty_graph_has_no_cycle(self):
        self.assertEqual(False, cycle_exists(self.empty_graph))

    def test_graph_with_no_cycle_returns_false(self):
        self.assertEqual(False, cycle_exists(self.graph_with_no_cycle))

    def test_graph_with_cycle_returns_true(self):
        self.assertEqual(True, cycle_exists(self.graph_with_cycle))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/graphs -v
