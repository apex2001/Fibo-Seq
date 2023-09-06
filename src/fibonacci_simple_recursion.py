from src.fibonacci_validator import *

@validate_position
def fibonacci(position, recursive_fibonacci=None):
    if position < 2:
        return 1

    recursive_function_to_call = recursive_fibonacci if recursive_fibonacci else fibonacci

    return recursive_function_to_call(position - 2) + recursive_function_to_call(position - 1)