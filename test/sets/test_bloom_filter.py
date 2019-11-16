import unittest
from sets.bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_build_initial_bit_array(self):
        bit_arr = BloomFilter.build_initial_bit_array(10000, 0.001)
        self.assertEqual(143776, len(bit_arr))

    def test_calculate_num_hashes(self):
        self.assertEqual(10, BloomFilter.calculate_num_hashes(143776, 10000))

    def test_empty_bloom_filter(self):
        empty_bloom_filter = self.build_bloom_filter()
        self.assertEqual(False, empty_bloom_filter.is_already_added("hello"))

    def test_bloom_filter_with_one_entry(self):
        b_filter = self.build_bloom_filter()
        b_filter.add("hello")
        self.assertEqual(True, b_filter.is_already_added("hello"))
        self.assertEqual(False, b_filter.is_already_added("not present"))

    def test_bloom_filter_with_multiple_entries(self):
        b_filter = self.build_bloom_filter()
        b_filter.add("hello")
        b_filter.add("how")
        b_filter.add("are")
        b_filter.add("you")
        self.assertEqual(True, b_filter.is_already_added("you"))
        self.assertEqual(False, b_filter.is_already_added("me"))

    def build_bloom_filter(self):
        return BloomFilter(100000, 0.001) # 110k elems with 0.1% False Positives


if __name__ == "__init__":
    unittest.main()

# python -m unittest discover test/sets -v
