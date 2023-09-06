def validate_position(fibonacci):
    def position_validated(position, *arg):
        if position < 0:
            raise ValueError("Invalid Fibonacci Position")

        return fibonacci(position, *arg)

    return position_validated