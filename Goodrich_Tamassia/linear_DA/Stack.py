from EmptyError import Empty
from FullError import Full


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=None):
        """Create an empty stack."""
        if maxlen:
            self._data = [None] * maxlen  # nonpublic list instance
        else:
            self._data = []  # initialize the underline list with a pre-define length
        self._n = 0
        self.max = maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._n == 0

    def push(self, e):
        """Add element e to the top of the stack.

            Raise Full exception if there is max length limit violation
        """
        if self.max:
            if self._n == self.max:
                raise Full('the stack is full')
            else:
                self._data[self._n] = e
                self._n += 1
        else:
            self._data.append(e)
            self._n += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._n - 1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        elif self.max:
            temp = self._data[self._n - 1]
            self._data[self._n - 1] = None
            self._n -= 1
            return temp
        else:
            self._n -= 1
            return self._data.pop()  # remove last item from list

    def copy(self):
        """Return a copy of the stack"""
        temp = ArrayStack()
        for k in range(self._n):
            temp.push(self._data[k])
        return temp

    def _reverse_array(self, start: int, last: int):
        if start < last - 1:
            self._data[start], self._data[last - 1] = self._data[last - 1], self._data[start]  # swap first and last
            self._reverse_array(start + 1, last - 1)  # recur on rest

    def transfer_inverse(self, T):
        """Transfer the elements of the current stack into other"""
        while not self.is_empty():
            T.push(self.pop())

    def transfer_direct(self, T):
        """Transfer the elements of the current stack into other"""
        for k in range(self._n):
            T.push(self._data[k])

        while not self.is_empty():
            self.pop()

    def reverse(self, new=False):
        """Reverse the elements of the stack. If new is True, then return a new Stack with the same elements but
        in reverse order"""
        if new:
            temp = ArrayStack()
            for k in range(self._n, 0, -1):
                temp.push(self._data[k - 1])
            return temp
        else:
            self._reverse_array(0, self._n)

    def clear(self):
        """Remove all the elements from the stack"""
        if self.max is None:
            self._data = []
        else:
            for k in range(self._n):
                self._data[k] = None
        self._n = 0

    def __str__(self):
        if self.max is None:
            return str(self._data)
        else:
            if self.is_empty():
                return '[]'
            return '[' + ', '.join(self._data[k] for k in range(self._n)) + ']'


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    # ------------------------------- stack methods -------------------------------
    def __init__(self, max_len=None):
        """Create an empty stack."""
        self._max_len = max_len
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._max_len and self._size == self._max_len:
            raise Full('The stack if full')
        else:
            self._head = self._Node(e, self._head)  # create and link a new node
            self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next  # bypass the former top node
        self._size -= 1
        return answer

    def copy(self):
        """Return a copy of the stack"""
        temp = LinkedStack()
        current = self._head
        while current is not None:
            temp.push(current._element)
            current = current._next
        return temp

    def transfer(self, T):
        """Transfer the elements of the current stack into other"""
        while not self.is_empty():
            T.push(self.pop())

    def reverse(self):
        """Reverse the elements of the stack. If new is True, then return a new Stack with the same elements but
        in reverse order"""
        temp = LinkedStack()
        self.transfer(temp)
        result = temp.copy()
        temp.transfer(self)
        return result

    def __str__(self):
        elements = []
        current = self._head
        while current is not None:
            elements.append(current)
            current = current._next
        return str(elements)


if __name__ == '__main__':
    S = ArrayStack()  # contents: [ ]
    S.push(5)  # contents: [5]
    S.push(3)  # contents: [5, 3]
    print(len(S))  # contents: [5, 3];    outputs 2
    print(S.pop())  # contents: [5];       outputs 3
    print(S.is_empty())  # contents: [5];       outputs False
    print(S.pop())  # contents: [ ];       outputs 5
    print(S.is_empty())  # contents: [ ];       outputs True
    S.push(7)  # contents: [7]
    S.push(9)  # contents: [7, 9]
    print(S.top())  # contents: [7, 9];    outputs 9
    S.push(4)  # contents: [7, 9, 4]
    print(len(S))  # contents: [7, 9, 4]; outputs 3
    print(S.pop())  # contents: [7, 9];    outputs 4
    S.push(6)  # contents: [7, 9, 6]
    S.push(8)  # contents: [7, 9, 6, 8]
    print(S.pop())  # contents: [7, 9, 6]; outputs 8
    print(S)
    print('-----------------')
    T = ArrayStack(3)
    T.push('abc')
    T.push('def')
    T.push('ghi')
    print(T)
    T.reverse()
    print(T)
    # T.push('abc')  # raise error since the stack is full
    R = S.copy()
    print(S)
    print(R)
    print(T.reverse(new=True))
    print('T: ', T)
    v = ArrayStack()
    print(v)
    T.transfer_inverse(v)
    # T.transfer_direct(v)
    print('v: ', v)
    print(T)
