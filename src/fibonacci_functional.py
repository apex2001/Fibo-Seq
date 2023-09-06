from functools import reduce
from src.fibonacci_validator import *

@validate_position
def fibonacci(position):
    def next_fibonacci_pair(previous_and_current, _):
        return (previous_and_current[1], sum(previous_and_current))

    return reduce(next_fibonacci_pair, [(1, 1)] + list(range(position - 1)))[1]
