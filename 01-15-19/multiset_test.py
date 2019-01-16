"""
Unit tests for multiset.

Copyright (c) 2019, Sekhar Ravinutala.
"""

import unittest
from multiset import Multiset

class TestMultiset(unittest.TestCase):
    """
    Tests for multiset.
    """
    def test_union(self):
        """
        Checks for union().
        """
        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"a": 1, "c": 2})
        set3 = Multiset({"a": 11, "b": 20, "c": 2})
        self.assertEqual(set1.union(set2), set3)

        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"x": 1, "y": 2})
        set3 = Multiset({"a": 10, "b": 20, "x": 1, "y": 2})
        self.assertEqual(set1.union(set2), set3)

    def test_intersection(self):
        """
        Checks for intersection().
        """
        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"a": 1, "c": 2})
        set3 = Multiset({"a": 1, "b": 0, "c": 0})
        self.assertEqual(set1.intersection(set2), set3)

        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"x": 1, "y": 2})
        set3 = Multiset({"a": 0, "b": 0, "x": 0, "y": 0})
        self.assertEqual(set1.intersection(set2), set3)

    def test_difference(self):
        """
        Checks for difference().
        """
        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"a": 1, "c": 2})
        set3 = Multiset({"a": 9, "b": 20, "c": 0})
        self.assertEqual(set1.difference(set2), set3)

        set1 = Multiset({"a": 10, "b": 20})
        set2 = Multiset({"x": 1, "y": 2})
        set3 = Multiset({"a": 10, "b": 20, "x": 0, "y": 0})
        self.assertEqual(set1.difference(set2), set3)
