"""
Run the hello module to see how it works.

Copyright (c) 2019, Sekhar Ravinutala.
"""
import sys
from hello.greeting import greeting

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(greeting(sys.argv[1]))
    else:
        print(greeting())
