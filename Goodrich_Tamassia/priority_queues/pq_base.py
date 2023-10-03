class BasePriorityQueue:
    """Abstract base class for a priority queue"""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_element'

        def __init__(self, element, key):
            """Initialized a new priority queue Item"""
            self._element = element
            self._key = key

        def __lt__(self, other):
            """compare items based on their keys"""
            return self._key < other._key

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty"""
        return len(self) == 0
