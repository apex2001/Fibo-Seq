from functools import cache
from src.fibonacci_simple_recursion import fibonacci as fibonacci_simple_recursion

@cache
def fibonacci(position):
    return fibonacci_simple_recursion(position, fibonacci)