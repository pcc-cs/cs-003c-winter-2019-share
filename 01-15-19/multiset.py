"""
Exercise 8.13 (page 495): implement a multiset.

Copyright (c) 2019, Sekhar Ravinutala.
"""

class Multiset():
    """
    Special multiset functionality.
    """
    def __init__(self, entries=None):
        self.entries = entries or {}

    def __eq__(self, other):
        return self.entries == other.entries

    def union(self, other):
        """
        Special multiset union.
        - other: Second multiset.
        """
        result = Multiset()
        for key in set(self.entries).union(set(other.entries)):
            result.entries[key] = self.entries.get(key, 0) + other.entries.get(key, 0)

        return result

    def intersection(self, other):
        """
        Special multiset intersection.
        - other: Second multiset.
        """
        result = Multiset()
        for key in set(self.entries).union(set(other.entries)):
            result.entries[key] = min(self.entries.get(key, 0), other.entries.get(key, 0))

        return result

    def difference(self, other):
        """
        Special multiset difference.
        - other: Second multiset.
        """
        result = Multiset()
        for key in set(self.entries).union(set(other.entries)):
            result.entries[key] = max(self.entries.get(key, 0) - other.entries.get(key, 0), 0)

        return result
