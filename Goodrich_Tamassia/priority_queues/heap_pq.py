from linear_DA.EmptyError import Empty
from priority_queues.pq_base import BasePriorityQueue


class HeapPriorityQueue(BasePriorityQueue):
    """A min-oriented priority queue implemented with a binary heap."""

    def __init__(self, contents=()):
        """Create a new empty Priority Queue.

        By default, queue will be empty. If contents is given, it should be as an iterable sequence of (k,v) tuples
        specifying the initial contents. """
        if len(contents) != 0:
            if isinstance(contents[0], ()):
                self._data = [self._Item(k[1], k[0]) for k in contents]
            else:
                self._data = [self._Item(k, k) for k in contents]
            self._heapify()
        else:
            self._data = []

    # -------- Utility functions -------------

    def _heapify(self):
        start = self._parent(len(self._data) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, k):
        return self._left(k) < len(self._data)  # index beyond end of list?

    def _has_right(self, k):
        return self._right(k) < len(self._data)  # index beyond end of list?

    def _swap(self, j, k):
        """Swap the elements at indices i and j of array."""
        self._data[j], self._data[k] = self._data[k], self._data[j]

    def _upheap(self, j):
        p = self._parent(j)
        if j > 0 and self._data[j] < self._data[p]:
            self._swap(j, p)
            self._upheap(p)

    def _downheap(self, j):
        if self._has_right(j):
            c = min(self._data[self._left(j)], self._data[self._right(j)])
        elif self._has_left(j):
            c = self._data[self._left(j)]
        else:
            return

        if self._data[j] > self._data[c]:
            self._swap(j, c)
            self._downheap(c)

    # ------------------------------ public behaviors ------------------------------

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, element):
        """Add a key-value pair to the priority queue"""
        self._data.append(self._Item(element, key))
        self._upheap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._element)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._element)
