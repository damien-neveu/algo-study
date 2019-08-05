import unittest
from hashtables.lru_cache import LruCache


class TestLruCache(unittest.TestCase):

    def test_lru_cache(self):
        cache = LruCache(3)
        cache.set("1", "one")
        cache.set("2", "two")
        cache.set("3", "three")
        self.assertEqual("one",cache.get("1"))
        cache.set("2", "deux")
        cache.set("7", "seven")
        self.assertEqual("deux", cache.get("2"))
        self.assertEqual(None, cache.get("1"))


if __name__ == "__main__":
    unittest.main()
