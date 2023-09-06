from test_fibonacci import *
from src.fibonacci_functional import fibonacci

class FibonacciFunctionalTest(unittest.TestCase, FibonacciTest):
    def fibonacci_implementation(self):
        return fibonacci