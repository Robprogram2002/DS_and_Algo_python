# While support for undo can be implemented with an unbounded stack, many applications provide only limited support for
# such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full capacity, rather than
# throwing a Full exception , a more typical semantic is to accept the pushed element at the top while “leaking” the
# oldest element from the bottom of the stack to make room.

# Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate storage capacity.
from linear_DA.EmptyError import Empty


class LeakyStack:
    """" LIFO Leaky Stack implementation using a Python circular list as underlying storage. """

    def __init__(self, max_len):
        """Create an empty leaky-stack."""

        self._data = [None] * max_len
        self._size = 0
        self._front = 0
        self._max = max_len

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack. If stack is full also delete the element
        at the bottom of the stack
        """
        if self._size == self._max:
            self._data[self._front] = e
            self._front = (self._front + 1) % len(self._data)
        else:
            available = (self._front + self._size) % len(self._data)
            self._data[available] = e
            self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[(self._front + self._size) % len(self._data) - 1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')

        last_index = (self._front + self._size) % len(self._data) - 1
        temp = self._data[last_index]
        self._data[last_index] = None
        self._size -= 1
        return temp

    def __str__(self):
        if self.is_empty():
            return '[]'
        return '[' + ', '.join(
            str(self._data[k % len(self._data)]) for k in range(self._front, self._front + self._size)) + ']'


if __name__ == '__main__':
    S = LeakyStack(6)  # contents: [ ]
    S.push(5)  # contents: [5]
    S.push(3)  # contents: [5, 3]
    print(len(S))
    S.push('23')
    S.push('2')
    S.push('-8')
    S.push('a')
    print(S)
    S.push('b')
    print(S)
    S.pop()
    S.pop()
    print(S)
    S.push(1)
    S.push(10)
    S.push(100)
    print(S)
