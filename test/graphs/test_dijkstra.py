import unittest
from graphs.dijkstra import find_shortest_path


class TestDjikstra(unittest.TestCase):

    empty_graph = {}
    graph = {
        'A': [('B', 2), ('C', 1), ('D', 3)],
        'B': [('A', 2), ('G', 3), ('H', 2), ('I', 4)],
        'C': [('A', 1), ('D', 2), ('I', 2)],
        'D': [('A', 3), ('C', 2), ('E', 2), ('F', 4)],
        'E': [('D', 2), ('F', 1)],
        'F': [('D', 4), ('E', 1), ('K', 2), ('M', 5)],
        'G': [('B', 3)],
        'H': [('B', 2), ('I', 1)],
        'I': [('B', 4), ('C', 2), ('H', 1), ('J', 2)],
        'J': [('I', 2), ('K', 1), ('L', 3)],
        'K': [('F', 2), ('J', 1), ('L', 3)],
        'L': [('J', 3), ('K', 3), ('M', 2)],
        'M': [('F', 5), ('L', 2)]
    }

    def test_shortest_path_from_to_same_node(self):
        self.assertEqual(['A'], find_shortest_path(self.graph, 'A', 'A'))

    def test_shortest_path_from_to_non_existing_nodes(self):
        self.assertEqual([], find_shortest_path(self.graph, 'A', 'X'))

    def test_shortest_path_from_to_valid_nodes(self):
        self.assertEqual(['A', 'C', 'I', 'J', 'L'], find_shortest_path(self.graph, 'A', 'L'))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/graphs -v
