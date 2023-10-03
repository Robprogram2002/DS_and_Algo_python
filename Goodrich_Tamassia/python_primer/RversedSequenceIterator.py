class ReversedSequenceIterator:
    """An iterator for any of Python's sequence types that traverse the elements in reversed order."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = len(sequence)  # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1  # go back to next index
        if self._k >= 0:
            return self._seq[self._k]  # return the data element
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == '__main__':
    iterator = ReversedSequenceIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for i in iterator:
        print(i, end='\t')
