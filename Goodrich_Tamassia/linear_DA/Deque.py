# We do not provide an explicit init method for the LinkedDeque class, as the inherited
# version of that method suffices to initialize a new instance. We also rely on the
# inherited methods len and is empty in meeting the deque ADT.

from Goodrich_Tamassia.lists.DoublyLinkedList import _DoublyLinkedBase
from EmptyError import Empty


class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self, max_len=None):
        """Create an empty deque."""
        if max_len:
            self._data = [None] * max_len
        else:
            self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._max = max_len

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def append_left(self, element):
        if self._max and self._size == self._max:
            # append the element and remove the one in the other end
            self._front = (self._front - 1) % len(self._data)
            self._data[self._front] = element
            return

        if self._max is None and self._size == len(self._data):
            self._resize(self._size * 2)

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = element
        self._size += 1

    def append_right(self, element):
        if self._max and self._size == self._max:
            # append the element and remove the one in the other end
            self._data[self._front] = element
            self._front = (self._front + 1) % len(self._data)
            return

        if self._size == len(self._data):
            self._resize(self._size * 2)
        next_back = (self._front + self._size) % len(self._data)
        self._data[next_back] = element
        self._size += 1

    def first(self):
        return self._data[self._front]

    def last(self):
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def remove_left(self):
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return value

    def remove_right(self):
        back = (self._front + self._size - 1) % len(self._data)
        value = self._data[back]
        self._data[back] = None
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return value

    def _resize(self, capacity):
        new_list = [None] * capacity
        front = self._front
        for k in range(self._size):
            new_list[k] = self._data[front]
            front = (front + 1) % len(self._data)
        self._data = new_list
        self._front = 0

    def rotate(self, shift=None):
        if shift is not None and shift > 1:
            for i in range(shift):
                self.rotate()
            return

        answer = self._data[self._front]
        self._data[self._front] = None
        avail = (self._front + self._size) % len(self._data)
        self._front = (self._front + 1) % len(self._data)
        self._data[avail] = answer

    def count(self, value):
        current = self._front
        count = 0
        for k in range(self._size):
            if self._data[current] == value:
                count += 1
            current = (current + 1) % len(self._data)
        return count

    def clear(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def print_deque(self):
        current = self._front
        print('[', end='')
        for k in range(self._size):
            print(self._data[current], end=', ')
            current = (current + 1) % len(self._data)
        print(']')


class LinkedDeque(_DoublyLinkedBase):  # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)  # use inherited method


if __name__ == '__main__':
    deque = ArrayDeque()
    print(deque.is_empty())
    print(len(deque))
    deque.append_left(10)
    deque.append_left(100)
    deque.append_left(1000)
    deque.print_deque()
    deque.append_right(20)
    deque.append_right(200)
    deque.append_right(2000)
    deque.print_deque()
    print(len(deque))
    print(deque.is_empty())
    print(deque.first())
    print(deque.last())
    deque.remove_left()
    deque.remove_right()
    deque.print_deque()
    print(len(deque))
    deque.remove_left()
    deque.print_deque()
    # deque.clear()
    # deque.print_deque()
    deque.append_left(100)
    print('----------------------')
    deque.print_deque()
    deque.rotate()
    deque.print_deque()
    deque.remove_left()
    deque.rotate()
    deque.print_deque()
    deque.append_left(20)
    deque.print_deque()
    print(deque.count(20))
    print('----------')
    deque.print_deque()
    deque.rotate(2)
    deque.print_deque()
    print('------------')
    deque = ArrayDeque(5)
    deque.append_left(10)
    deque.append_left(100)
    deque.append_left(1000)
    deque.append_right(20)
    deque.append_right(200)
    deque.print_deque()
    deque.append_left('a')
    deque.print_deque()
    deque.append_left('b')
    deque.print_deque()
    deque.append_right('c')
    deque.print_deque()
    deque.append_right('d')
    deque.print_deque()
