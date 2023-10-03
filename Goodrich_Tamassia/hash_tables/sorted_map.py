from hash_tables.map_base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    # ----------------------------- nonpublic behaviors -----------------------------

    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies. That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >=k
        """
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                self._find_index(k, low, mid - 1)
            else:
                self._find_index(k, mid + 1, high)

    # ----------------------------- public behaviors -----------------------------

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key != k or index == len(self._table):
            raise KeyError('Key Error: ' + repr(k))
        return self._table[index]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key == k and index < len(self._table):
            self._table[index]._value = v
        else:
            self._table.insert(index, self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key != k or index == len(self._table):
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(index)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)"""
        return (self._table[0]._key, self._table[0]._value) if len(self._table) > 0 else None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        return (self._table[-1]._key, self._table[-1]._value) if len(self._table) > 0 else None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k"""
        index = self._find_index(k, 0, len(self._table) - 1)
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        return None

    def find_le(self, k):
        """Return (key,value) pair with greatest key less than or equal to k."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key == k:
            return (self._table[index]._key, self._table[index]._value)
        if index > 0:
            return (self._table[index - 1]._key, self._table[index - 1]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if index > 0:
            return (self._table[index - 1]._key, self._table[index - 1]._value)
        return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k."""
        index = self._find_index(k, 0, len(self._table) - 1)
        if self._table[index]._key == k and index < len(self._table):
            index += 1
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        start_index = self._find_index(start, 0, len(self._table) - 1) if start is not None else 0
        stop_index = self._find_index(start, 0, len(self._table) - 1) if stop is not None else len(self._table)
        for item in self._table[start_index: stop_index - 1]:
            yield (item._key, item._value)

        #  Another Implementation

        # if start is None:
        #     j = 0
        # else:
        #     j = self._find_index(start, 0, len(self._table) - 1)  # find first result
        # while j < len(self._table) and (stop is None or self._table[j].key < stop):
        #     yield (self._table[j].key, self._table[j].value)
        #     j += 1
