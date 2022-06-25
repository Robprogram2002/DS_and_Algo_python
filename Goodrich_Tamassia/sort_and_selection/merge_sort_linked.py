from linear_DA.Queue import LinkedQueue


def merge(s1: LinkedQueue, s2: LinkedQueue, S: LinkedQueue):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not s1.is_empty() and not s2.is_empty():
        if s1.first() < s2.first():
            S.enqueue(s1.dequeue())
        else:
            S.enqueue(s2.dequeue())
    while not s1.is_empty():
        S.enqueue(s1.dequeue())
    while not s2.is_empty():
        S.enqueue(s2.dequeue())


def merge_sort(S: LinkedQueue):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return

    # divide
    s1 = LinkedQueue()
    s2 = LinkedQueue()  # can be other implementation
    while len(s1) < n // 2:
        s1.enqueue(S.dequeue())
    while not S.is_empty():
        s2.enqueue(S.dequeue())

    # conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)

    # merge results
    merge(s1, s2, S)
