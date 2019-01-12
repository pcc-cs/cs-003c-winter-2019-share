"""
Unit tests for digits functions.

Copyright (c) 2019, Sekhar Ravinutala.
"""

import unittest
from digits import first_digit, last_digit, digits

class TestDigits(unittest.TestCase):
    """
    Test digits functions.
    """
    def test_first_digit(self):
        """
        Test for first_digit().
        """
        self.assertEqual(first_digit(0), 0)
        self.assertEqual(first_digit(2), 2)
        self.assertEqual(first_digit(34214), 3)

    def test_last_digit(self):
        """
        Test for last_digit().
        """
        self.assertEqual(last_digit(0), 0)
        self.assertEqual(last_digit(9), 9)
        self.assertEqual(last_digit(442876), 6)
        self.assertEqual(last_digit(98230), 0)

    def test_digits(self):
        """
        Test for digits().
        """
        self.assertEqual(digits(0), 1)
        self.assertEqual(digits(6), 1)
        self.assertEqual(digits(7832554), 7)
