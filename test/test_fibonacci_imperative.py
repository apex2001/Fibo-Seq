from test_fibonacci import *
from src.fibonacci_imperative import fibonacci

class FibonacciImperativeTest(unittest.TestCase, FibonacciTest):
    def fibonacci_implementation(self):
        return fibonacci
