import unittest
from parameterized import parameterized

class FibonacciTest():
    @parameterized.expand([
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 8),
        (10, 89),
        (20, 10946),
        (25, 121393)
    ])
    def test_valid_position_fibonacci(self, position, result):
        self.assertEqual(self.fibonacci_implementation()(position), result)

    def test_fibonacci_negative_one(self):
        self.assertRaises(ValueError, self.fibonacci_implementation(), -1)
