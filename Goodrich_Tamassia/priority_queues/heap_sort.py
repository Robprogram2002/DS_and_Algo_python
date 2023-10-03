from lists.PositionalList import PositionalList
from priority_queues.heap_pq import HeapPriorityQueue


def pq_sort(c: []):
    """Sort a collection of elements stored in a python list."""
    p = HeapPriorityQueue(c)
    for k in range(len(c)):
        c[k] = p.remove_min()[1]


def pq_sort_positional(c: PositionalList):
    """Sort a collection of elements stored in a positional list"""
    n = len(c)
    P = HeapPriorityQueue()
    for j in range(n):
        element = c.delete(c.first())
        P.add(element, element)
    for j in range(n):
        c.add_last(P.remove_min()[1])


# With a minor modification to this code, we can provide more general support, sorting elements according to an ordering
# other than the default

# In Python, the standard approach for customizing the order for a sorting algorithm is to provide, as an optional
# parameter to the sorting function, an object that is itself a one-parameter function that computes a key for a given
# element.

def general_pq_sort_positional(c: PositionalList, key_generator=None):
    """Sort a collection of elements stored in a positional list
    If a key_generator function is provided, then the key of each element in the pq would be its result over the
    function, otherwise the key of each element will be itself
    """
    n = len(c)
    P = HeapPriorityQueue()
    for j in range(n):
        element = c.delete(c.first())
        if key_generator is None:
            P.add(element, element)
        else:
            P.add(key_generator(element), element)
    for j in range(n):
        c.add_last(P.remove_min()[1])


def general_pq_sort(c: PositionalList, key_generator=None):
    """Sort a collection of elements stored in a python list
    If a key_generator function is provided, then the key of each element in the pq would be its result over the
    function, otherwise the key of each element will be itself
    """
    if key_generator is None:
        p = HeapPriorityQueue(c)
    else:
        p = HeapPriorityQueue([(key_generator(k), k) for k in c])
    for k in range(len(c)):
        c[k] = p.remove_min()[1]

