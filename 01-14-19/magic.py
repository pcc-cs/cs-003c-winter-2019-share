"""
Exercise 6.21 (page 376): check if given numbers constitute a "magic" square.

Copyright (c) 2019, Sekhar Ravinutala.
"""

SIZE = 4

def is_magic(numbers, size=SIZE):
    """
    Check if given numbers form a "magic" square.
    """
    total = sum(numbers[:size])

    # Check if all numbers are present
    for i in range(1, size * size + 1):
        if not i in numbers:
            return False

    # Check rows
    for start in range(size, size * size, size):
        if sum(numbers[start:start + size]) != total:
            return False

    # Check columns
    for start in range(size):
        if sum([numbers[start + i * size] for i in range(size)]) != total:
            return False

    # Check diagonals
    if sum([numbers[i * (size + 1)] for i in range(size)]) != total:
        return False
    if sum([numbers[i * (size - 1)] for i in range(1, size + 1)]) != total:
        return False

    return True
