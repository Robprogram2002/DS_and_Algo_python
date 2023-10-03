def brute_force(s: str, p: str):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(s), len(p)
    for i in range(n - m + 1):  # try every potential starting index within T
        k = 0
        while k < m and s[i + k] == p[k]:
            k += 1
        if k == m:
            return i  # substring s[i:i+m] matches P
    return -1  # substring T[i:i+m] matches P


def find_boyer_moore(s: str, p: str):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(s), len(p)
    if m == 0:
        return 0  # trivial search for empty string
    last = {}
    for k in range(m):
        last[p[k]] = k  # later occurrence overwrites
    # align end of pattern at index m-1 of text
    i = m - 1
    k = m - 1
    while i < n:
        if s[i] == p[k]:
            if k == 0:  # pattern begins at index i of text
                return i
            i -= 1  # examine previous character
            k -= 1
        else:
            j = last.get(s[i], -1)
            i += m - min(k, j + 1)  # case analysis for jump step
            k = m - 1  # case analysis for jump step
    return -1


def compute_kmp_fail(p: str):
    """Utility that computes and returns KMP fail list."""
    m = len(p)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if p[k] == p[j]:  # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:  # k follows a matching prefix
            k = fail[k - 1]
        else:  # k follows a matching prefix
            j += 1
    return fail


def find_kmp(s: str, p: str):
    """Return the lowest index of s at which substring p begins (or else -1)."""
    n, m = len(s), len(p)
    if m == 0:
        return 0
    fail = compute_kmp_fail(p)
    j = 0
    k = 0
    while j < n:
        if s[j] == p[k]:  # P[0:1+k] matched thus far
            if k == m - 1:  # match is complete
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1


