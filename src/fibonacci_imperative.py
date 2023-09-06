from src.fibonacci_validator import *

@validate_position
def fibonacci(position):
    previous, current = 1, 1

    for _ in range(position):
        previous, current = current, previous + current

    return previous