import math


def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2 inc] into result."""
    end1 = start + inc  # boundary for run 1
    end2 = min(start + 2 * inc, len(src))  # boundary for run 2
    x, y, z = start, start + inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]  # copy from run 1 and increment x
            x += 1
        else:
            result[z] = src[y]  # copy from run 2 and increment y
            y += 1
        z += 1  # increment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1]  # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]  # copy remainder of run 2 to output


def merge_sort(s: []):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(s)
    logn = math.ceil(math.log(n, 2))
    src, dest = s, [None] * n                   # make temporary storage for dest
    for i in (2 ** k for k in range(logn)):     # pass i creates all runs of length 2i
        for j in range(0, n, 2 * i):            # each pass merges two length i runs
            merge(src, dest, j, i)
        src, dest = dest, src                   # reverse roles of lists
    if s is not src:
        s[0:n] = src[0:n]                       # additional copy to get results to S
