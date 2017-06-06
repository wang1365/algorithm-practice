class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def put(self, o):
        count = len(self.stack)
        if count == 0:
            self.min_stack.append(0)
        else:
            if o <= self.stack[self.min_stack[-1]]:
                self.min_stack.append(count)
        self.stack.append(o)

    def pop(self):
        if len(self.stack) - 1 == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.stack[self.min_stack[-1]]

    def __len__(self):
        return len(self.stack)


# ------------------------------------------- UT -----------------------------------------------

import unittest


class MinStackTest(unittest.TestCase):
    def setUp(self):
        super(MinStackTest, self).setUp()

    def tearDown(self):
        super(MinStackTest, self).tearDown()

    def testput(self):
        stack = MinStack()
        self.assertEqual(len(stack), 0)

        stack.put(12)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 12)

    def testpop(self):
        stack = MinStack()
        self.assertRaises(IndexError, stack.pop)

        stack.put(1)
        self.assertEqual(stack.pop(), 1)

        stack.put(4)
        stack.put(3)
        stack.put(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 4)
        self.assertRaises(IndexError, stack.pop)

    def testmin(self):
        stack = MinStack()
        self.assertRaises(IndexError, stack.min)

        stack.put(1)
        self.assertEqual(stack.min(), 1)

        stack.put(2)
        self.assertEqual(stack.min(), 1)

        stack.pop()
        self.assertEqual(stack.min(), 1)

        stack.put(-1)
        self.assertEqual(stack.min(), -1)

        stack.put(-2)
        stack.pop()
        self.assertEqual(stack.min(), -1)

if __name__ == '__main__':
    unittest.main()