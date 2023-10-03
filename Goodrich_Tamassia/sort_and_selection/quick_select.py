import random


def random_quick_select(s: [], k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(s) == 1:
        return s[0]
    pivot = random.choice(s)
    L = [x for x in s if x < pivot]
    E = [x for x in s if x == pivot]
    G = [x for x in s if pivot < x]

    if k <= len(L):
        return random_quick_select(L, k)  # kth smallest lies in L
    elif k <= len(L) + len(E):
        return pivot  # kth smallest equal to pivot
    else:
        j = k - len(L) - len(E)
        return random_quick_select(G, j)  # kth smallest equal to pivot


