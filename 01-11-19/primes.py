"""
Exercise 4.17 (page 232): calculate prime numbers.

Copyright (c) 2019, Sekhar Ravinutala.
"""
import math

def _primes(max_value):
    values = [2]
    for i in range(3, max_value + 1, 2):
        # Check with only primes up to root of number.
        for value in filter(lambda v: v <= math.ceil(math.sqrt(i)), values):
            if i % value == 0:
                break
        else:
            values.append(i)

    return values

if __name__ == "__main__":
    for p in _primes(int(input("Max value: "))):
        print(p)
