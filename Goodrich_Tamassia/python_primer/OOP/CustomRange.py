# we develop our own implementation of a class that mimics Python’s built-in range class.
# The biggest challenge in the implementation is properly computing
# the number of elements that belong in the range, given the parameters sent by the
# caller when constructing a range. By computing that value in the constructor, and
# storing it as self. length, it becomes trivial to return it from the len method. To
# properly implement a call to getitem (k), we simply take the starting value of
# the range plus k times the step size
import collections


class Range(collections.Sequence):
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

        # but for __contains__ we need the stop info
        self._stop = stop

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, item):
        if not isinstance(item, int):
            raise ValueError('parameter must be integer type')
        return (self._start <= item < self._stop) and (item - self._start) % self._step == 0


if __name__ == '__main__':
    my_range = Range(0, 51, 2)
    print(len(my_range))
    print(32 in my_range)
    print(13 in my_range)
    for i in my_range:
        print(i, end=' ')
