import unittest
from backtracking.reconstruct_itinerary import Solution


class TestReconstructItinerary(unittest.TestCase):

    sol = Solution()

    def test_simple_itinerary(self):
        self.assertEqual(["JFK", "MUC", "LHR"], self.sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"]]))

    def test_multiple_starting_points(self):
        self.assertEqual(["JFK","NRT","JFK","KUL"], self.sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))

    def test_complex_itinerary_with_dead_ends(self):
        self.assertEqual(['JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL', 'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'TIA', 'AUA', 'AXA', 'TIA', 'ADL', 'EZE', 'HBA'], self.sol.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))


if __name__ == "__main__":
    unittest.main()

# python -m unittest discover test/backtracking -v
