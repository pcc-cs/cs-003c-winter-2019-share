"""
Exercise 5.3 (page 305): create digit functions with tests.

Copyright (c) 2019, Sekhar Ravinutala.
"""

def first_digit(number):
    """
    Return first digit of number.
    - n: Number.
    """
    return int(str(number)[0])

def last_digit(number):
    """
    Return last digit of number.
    - n: Number.
    """
    return int(str(number)[-1])

def digits(number):
    """
    Return number of digits.
    - n: Number.
    """
    return len(str(number))
