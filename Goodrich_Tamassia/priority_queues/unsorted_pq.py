from linear_DA.EmptyError import Empty
from lists.PositionalList import PositionalList
from priority_queues.pq_base import BasePriorityQueue


class UnsortedPriorityQueue(BasePriorityQueue):
    """A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, element):
        """Add a key-value pair."""
        self._data.add_last(self._Item(element, key))

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        min_key = self._data.first()
        walk = self._data.after(min_key)
        while walk is not None:
            if walk.element() < min_key.element():
                min_key = walk
            walk = self._data.after(walk)
        return min_key

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        item = self._find_min().element()
        return (item._key, item._element)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._element)
