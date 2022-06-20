from priority_queues.heap_pq import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue"""
        __slots__ = "_index"  # add index as additional field

        def __init__(self, k, v, j):
            """Initialized a location instance"""
            super().__init__(k, v)
            self._index = j

    # ------------------------------ nonpublic behaviors ------------------------------
    def _swap(self, j, k):
        super()._swap(j, k)
        self._data[j]._index = j
        self._data[k]._index = k

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # ------------------------------ public behaviors ------------------------------

    def add(self, key, element):
        """Add a key-value pair."""
        token = self.Locator(element, key, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc: Locator, key, ele):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = key
        loc._element = ele
        self._bubble(j)

    def remove(self, loc: Locator):
        """Remove and return the (k,v) pair identified by Locator loc."""
        index = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        self._swap(index, len(self._data) - 1)
        self._data.pop()
        self._bubble(j)
        return (loc._key, loc._element)

