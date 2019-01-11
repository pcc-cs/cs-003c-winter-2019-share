"""
Check if a given phone number is valid. The first function uses a loop, the second the very powerful
regular expression package (check out docs.pythong.org or use help(re) for how to write these).

Copyright (c) 2019, Sekhar Ravinutala.
"""

import re

# Loop version.
def _is_valid_loop(number):
    if len(number) != 13:
        return False
    for i in range(13):
        if i == 0:
            valid = number[i] == "("
        elif i == 4:
            valid = number[i] == ")"
        elif i == 8:
            valid = number[i] == "-"
        else:
            valid = number[i].isdigit()

        if not valid:
            return False

    return True

# Regular expression version.
def _is_valid_re(number):
    return re.match(r"^\(\d{3}\)\d{3}\-\d{4}$", number) is not None

if __name__ == "__main__":
    phone_number = input("Enter number: ")
    print(_is_valid_loop(phone_number), _is_valid_re(phone_number))
