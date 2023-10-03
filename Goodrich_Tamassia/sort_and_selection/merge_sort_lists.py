from hash_tables.map_base import MapBase


def merge(s1: [], s2: [], s: []):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1

    while i < len(s1):
        s[i + j] = s1[i]
        i += 1
    while j < len(s2):
        s[i + j] = s2[j]
        j += 1


def merge_sort(s: []):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(s)
    if n <= 1:
        # list is already sorted
        return

    # divide
    middle = n // 2
    s1 = s[0:middle]
    s2 = s[middle:n]

    # conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)

    # merge results
    merge(s1, s1, s)


def decorated_merge_sort(data: [], key=None):
    """Demonstration of the decorate-sort-undecorate pattern."""
    if key is not None:
        for j in range(len(data)):
            data[j] = MapBase._Item(key(data[j]), data[j])
    merge_sort(data)
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j].value
