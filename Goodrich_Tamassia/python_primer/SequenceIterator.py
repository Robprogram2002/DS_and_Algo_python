#  To provide an instructive example of a low-level iterator, Code Fragment 2.5 demonstrates just such an iterator
# class that works on any collection that supports both len and getitem .
# This class can be instantiated as SequenceIterator(data). It operates by keeping an
# internal reference to the data sequence, as well as a current index into the sequence.
# Each time next is called, the index is incremented, until reaching the end of
# the sequence.


class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1  # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1  # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k]  # return the data element
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == '__main__':
    iterator = SequenceIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    iterator2 = SequenceIterator(['a', 'b', 'c', 'd', 'e', 'f'])
    for i in iterator:
        print(i, end='\t')
    print('')
    for j in iterator2:
        print(j, end='\t')
