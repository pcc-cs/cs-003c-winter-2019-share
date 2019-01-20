"""
Exercise 8.6 (page 494): organize words in a Python program into an index of line numbers.

Copyright (c) 2019, Sekhar Ravinutala.
"""

import re
import sys

def _index(path):
    numbers = {}
    with open(path) as file:
        for i, line in enumerate(file):
            for key in filter(None, re.split(r"[^\w]", line)):
                numbers[key] = numbers.get(key, set())
                numbers[key].add(i)

    return numbers

if __name__ == "__main__":
    index = _index(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0])
    for word in sorted(index):
        lines = ", ".join([str(x) for x in sorted(list(index[word]))])
        print("%16s %s" % (word, lines))
