from random import randint


def inplace_quick_sort(s: [], start, end):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm"""
    if start >= end:
        return
    pivot = s[end]  # last element of range is pivot
    left = start
    right = end - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        if s[left] > pivot:
            if s[end] <= pivot:
                s[left], s[end] = s[end], s[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1

    # put pivot into its final place (currently marked by left index)
    s[left], s[end] = s[end], s[left]
    # make recursive calls 21
    inplace_quick_sort(s, start, left - 1)
    inplace_quick_sort(s, left + 1, end)


def random_quick_sort(s: [], start, end):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm"""
    if start >= end:
        return
    index = randint(start, end)
    s[index], s[end] = s[end], s[index]
    pivot = s[end]  # last element of range is pivot
    left = start
    right = end - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        if s[left] > pivot:
            if s[end] <= pivot:
                s[left], s[end] = s[end], s[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1

    # put pivot into its final place (currently marked by left index)
    s[left], s[end] = s[end], s[left]
    # make recursive calls 21
    inplace_quick_sort(s, start, left - 1)
    inplace_quick_sort(s, left + 1, end)


def median_of_three(L: [], low, high):
    mid = (low + high) // 2
    a = L[low]
    b = L[mid]
    c = L[high]
    if a <= b <= c:
        return mid
    if c <= b <= a:
        return mid
    if a <= c <= b:
        return high
    if b <= c <= a:
        return high
    return low


def median_of_three_quick_sort(s: [], start, end):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm"""
    if start >= end:
        return
    median = median_of_three(s, start, end)
    s[median], s[end] = s[end], s[median]
    pivot = s[end]  # last element of range is pivot
    left = start
    right = end - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        if s[left] > pivot:
            if s[end] <= pivot:
                s[left], s[end] = s[end], s[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1

    # put pivot into its final place (currently marked by left index)
    s[left], s[end] = s[end], s[left]
    # make recursive calls 21
    inplace_quick_sort(s, start, left - 1)
    inplace_quick_sort(s, left + 1, end)
