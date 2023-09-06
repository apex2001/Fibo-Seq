from test_fibonacci import *
from src.fibonacci_simple_recursion import fibonacci

class FibonacciSimpleRecursionTest(unittest.TestCase, FibonacciTest):
    def fibonacci_implementation(self):
        return fibonacci