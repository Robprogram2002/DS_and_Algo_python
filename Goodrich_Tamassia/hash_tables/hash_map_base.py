from random import randrange

from hash_tables.map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0
        self._prime = p  # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # prime for MAD compression
        self._shift = randrange(p)  # shift from 0 to p-1 for MAD

    # ----------------- Abstracts methods ----------------- #
    def _bucket_getitem(self, j, k):
        """"""

    def _bucket_setitem(self, j, k, v):
        """"""

    def _bucket_delitem(self, j, k):
        """"""

    def __iter__(self):
        """"""

    # ----------------- Utility functions ----------------- #

    def _hash_function(self, key):
        """utility method that relies on Python’s built-in hash function to produce hash codes for keys, and a
        randomized MultiplyAdd-and-Divide (MAD) formula for the compression function."""
        return (hash(key) * self._scale + self._shift) % self._prime % len(self._table)

    def _resize(self, c):
        """resize bucket array to capacity c"""
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    # ----------------- Concrete methods ----------------- #

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        j = self._hash_function(key)
        return self._bucket_getitem(j, key)

    def __setitem__(self, key, value):
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)
        if self._n > len(self._table) // 2:  # keep load factor <=0.5
            self._resize(2 * len(self._table) - 1)  # number 2ˆx - 1 is often prime

    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)
        self._n -= 1
