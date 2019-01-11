"""
Exercise 3.28 (page 155): convert regular decimal number into Roman. The key idea here is
that the same pattern repeats for hundreds, tens, and unit representations, which allows us to
write once and re-use. This DRY principle is extremely important in coding.

Copyright (c) 2019, Sekhar Ravinutala.
"""

def _compound(digit, low, mid, high):
    return\
        digit * low if digit < 4 else\
        low + mid if digit == 4 else\
        mid if digit == 5 else\
        mid + (digit - 5) * low if digit < 9 else\
        low + high

def _roman(decimal):
    value = decimal // 1000 * "M"
    value += _compound((decimal % 1000) // 100, "C", "D", "M")
    value += _compound((decimal % 100) // 10, "X", "L", "C")
    value += _compound(decimal % 10, "I", "V", "X")

    return value

if __name__ == "__main__":
    print(_roman(int(input("Number: "))))
