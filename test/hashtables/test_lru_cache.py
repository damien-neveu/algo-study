import unittest
from hashtables.lru_cache import *


class TestLruCache(unittest.TestCase):

    def test_lru_cache(self):
        obj = LRUCache(3)
        obj.put(1, 1)
        obj.put(2, 2)
        obj.put(3, 3)
        obj.put(4, 4)
        self.assertEqual(4, obj.get(4))
        self.assertEqual(3, obj.get(3))
        self.assertEqual(2, obj.get(2))
        self.assertEqual(-1, obj.get(1))
        obj.put(5, 5)
        self.assertEqual(-1, obj.get(1))
        self.assertEqual(2, obj.get(2))
        self.assertEqual(3, obj.get(3))
        self.assertEqual(-1, obj.get(4))
        self.assertEqual(5, obj.get(5))
        self.assertEqual(["(5,5)", "(3,3)", "(2,2)"], obj.linked_list_to_arr())


if __name__ == "__main__":
    unittest.main()


# python -m unittest discover test/hashtables -v
