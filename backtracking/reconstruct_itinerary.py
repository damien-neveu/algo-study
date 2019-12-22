from typing import List
from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.itinerary = []
        self.itinerary_expected_length = 0

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets or not any(self.starts_at_jfk for t in tickets):
            return []
        self.itinerary = []
        self.itinerary_expected_length = len(tickets) + 1
        self.build_itinerary(self.build_flights_map(tickets), "JFK")
        return self.itinerary

    def starts_at_jfk(self, ticket):
        return ticket[0] == "JFK"

    def build_itinerary(self, flights_map, current_origin):
        self.itinerary.append(current_origin)
        if len(self.itinerary) == self.itinerary_expected_length:
            return True
        destinations = flights_map.get(current_origin, [])
        num_destinations = len(destinations)
        i = 0
        while i < num_destinations:
            current_destination = destinations.pop()
            if self.build_itinerary(flights_map, current_destination):
                return True
            destinations.appendleft(current_destination)
            i += 1
        self.itinerary.pop()
        return False

    def build_flights_map(self, tickets):
        m = defaultdict(deque)
        sorted_tix = sorted(tickets, key=lambda t: (t[0], t[1]))
        for (origin, destination) in sorted_tix:
            m[origin].appendleft(destination)
        print("m={}".format(str(m)))
        return m
