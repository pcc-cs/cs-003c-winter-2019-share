"""
Unit tests for "magic" function.

Copyright (c) 2019, Sekhar Ravinutala.
"""

import unittest
from magic import is_magic

class TestMagic(unittest.TestCase):
    """
    Test "magic" function.
    """
    def test_is_magic(self):
        """
        Test for is_magic().
        """
        self.assertTrue(is_magic([2, 7, 6, 9, 5, 1, 4, 3, 8], 3))
        self.assertTrue(is_magic([16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1]))
        self.assertFalse(is_magic([]))
        self.assertFalse(is_magic([2, 7, 6, 8, 5, 1, 4, 3, 8], 3))
