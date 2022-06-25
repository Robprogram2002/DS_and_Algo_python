from linear_DA.Queue import LinkedQueue


def quick_sort(s: LinkedQueue):
    """Sort the elements of queue S using the quick-sort algorithm."""

    n = len(s)
    if n < 2:
        return

    # divide
    p = s.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not s.is_empty():
        if s.first() < p:
            L.enqueue(s.dequeue())
        elif p < s.first():
            G.enqueue(s.dequeue())
        else:
            E.enqueue(s.dequeue())

    # conquer (with recursion)
    quick_sort(L)
    quick_sort(G)

    # concatenate results
    while not L.is_empty():
        s.enqueue(L.dequeue())
    while not E.is_empty():
        s.enqueue(E.dequeue())
    while not G.is_empty():
        s.enqueue(G.dequeue())

