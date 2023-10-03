from linear_DA.EmptyError import Empty
from lists.PositionalList import PositionalList
from priority_queues.pq_base import BasePriorityQueue


class SortedPriorityQueue(BasePriorityQueue):
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, element):
        """Add a key-value pair."""
        newest = self._Item(element, key)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data.first().element()
        return (item._key, item._elment)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._element)
