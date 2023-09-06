from test_fibonacci import *
from src.fibonacci_memoized_recursion import fibonacci

class FibonacciMemoizedRecursionTest(unittest.TestCase, FibonacciTest):
    def fibonacci_implementation(self):
        return fibonacci