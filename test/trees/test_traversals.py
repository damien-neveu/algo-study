import unittest
from trees.traversals import *


class TestTraversals(unittest.TestCase):

    # tree-traversal article: https://medium.com/quick-code/data-structures-traversing-trees-9473f6d9f4ef
    # below tree image: https://miro.medium.com/max/1056/1*fGEE6TYlsgDhZHSAQdjXeQ.png
    tree = Node(20, Node(16, Node(6, Node(0), Node(7)), Node(17)), Node(25, Node(21), Node(29, Node(28), Node(51, Node(46)))))

    def test_depth_first_in_order(self):
        self.assertEqual([0, 6, 7, 16, 17, 20, 21, 25, 28, 29, 46, 51], depth_first_in_order(self.tree))

    def test_breadth_first(self):
        self.assertEqual([20, 16, 25, 6, 17, 21, 29, 0, 7, 28, 51, 46], breadth_first(self.tree))


if __name__ == '__main__':
    unittest.main()
