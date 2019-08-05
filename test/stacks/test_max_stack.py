import unittest
from stacks.max_stack import MaxStack


class TestMaxStack(unittest.TestCase):

    def test_max_stack(self):
        stack = MaxStack()
        stack.push(7)
        self.assertEqual(7, stack.max())
        stack.push(1)
        self.assertEqual(7, stack.max())
        stack.push(10)
        self.assertEqual(10, stack.max())
        stack.pop()
        self.assertEqual(7, stack.max())


if __name__ == '__main__':
    unittest.main()
