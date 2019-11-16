import math
import mmh3
from functools import reduce


class BloomFilter:

    def __init__(self, expected_num_elements, probability_false_positive):
        self.n = expected_num_elements
        self.p = probability_false_positive
        self.bit_array = self.build_initial_bit_array(self.n, self.p)
        self.k = self.calculate_num_hashes(len(self.bit_array),  self.n)

    @staticmethod
    def build_initial_bit_array(n, p):
        m = -n * math.log(p) / math.log(2)**2
        # print("m = {}, ceil(m)={}".format(str(m), str(math.ceil(m))))
        return [0 for i in range(math.ceil(m))]

    @staticmethod
    def calculate_num_hashes(m, n):
        return math.ceil(m / n * math.log(2))

    @staticmethod
    def calculate_hashed_indexes(el, k, m):
        return [mmh3.hash(el, i) % m for i in range(k)]

    def is_already_added(self, elem):
        hashed_indexes = self.calculate_hashed_indexes(elem, self.k, len(self.bit_array))
        return reduce(
            lambda is_one_so_far, hashed_index: self.bit_array[hashed_index] and is_one_so_far,
            hashed_indexes,
            True)

    def add(self, elem):
        hashed_indexes = self.calculate_hashed_indexes(elem, self.k, len(self.bit_array))
        for i in hashed_indexes:
            self.bit_array[i] = 1


