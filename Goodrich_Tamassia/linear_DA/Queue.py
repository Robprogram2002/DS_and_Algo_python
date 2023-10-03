from linear_DA.FullError import Full
from linear_DA.EmptyError import Empty


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self, max_len=None):
        """Create an empty queue."""
        if max_len:
            self._data = [None] * max_len
        else:
            self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._max = max_len

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._max is None and 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._max and (self._size == self._max):
            raise Full('The queue is full cannot add a new element')

        if self._max is None and self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned

    def rotate(self, shift=1):
        if shift > 1:
            for i in range(shift):
                self.rotate()
            return

        if self._size == len(self._data):  # if list is full just advance the front pointer
            self._front = (self._front + 1) % len(self._data)
            return

        answer = self._data[self._front]
        self._data[self._front] = None
        avail = (self._front + self._size) % len(self._data)
        self._front = (self._front + 1) % len(self._data)
        self._data[avail] = answer

    def print_queue(self):
        current = self._front
        print('[', end='')
        for k in range(self._size):
            print(self._data[current], end=', ')
            current = (current + 1) % len(self._data)
        print(']')


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------------------------------- queue methods -------------------------------
    def __init__(self, max_len=None):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements
        self._max = max_len

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element  # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._max and self._size == self._max:
            raise Full('The queue is already full cannot add new elements')

        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1

    def rotate(self, shift=1):
        if shift > 1:
            for _ in range(shift):
                self.rotate()

        self._tail._next = self._head
        self._tail = self._head
        self._head = self._head._next
        self._tail._next = None

    def print_queue(self):
        current = self._head
        print('[')
        while current is not None:
            print(current._element, end=', ')
            current = current._next
        print(']')


# In addition to the traditional queue operations, the CircularQueue class supports
# a rotate method that more efficiently enacts the combination of removing the front
# element and reinserting it at the back of the queue. With the circular representation,
# we simply set self._tail = self._tail._next to make the old head become the new tail
# (with the node after the old head becoming the new head).


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    # ---------------------------------------------------------------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # end of _Node class
    # ---------------------------------------------------------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._next._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:  # removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail

    def _count_nodes(self, current):
        if current._element == self._tail._element:
            return 1
        else:
            return 1 + self._count_nodes(current._next)

    def nodes(self):
        """Return the number of nodes in the queue"""
        if self.is_empty():
            return 0
        else:
            return self._count_nodes(self._tail._next)


if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(10)
    queue.enqueue(100)
    queue.enqueue(1000)
    queue.enqueue(1000)
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    queue = ArrayQueue(4)
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    queue.enqueue('e')
    queue.enqueue('f')
    queue.print_queue()
    print('---------')
    # queue.enqueue('g')  #this cause a full error
    queue.rotate()
    queue.print_queue()
    queue.rotate()
    queue.rotate()
    queue.print_queue()
    queue.rotate(3)
    queue.print_queue()
    print('-----------------')
    circ_queue = CircularQueue()
    circ_queue.enqueue('a')
    circ_queue.enqueue('b')
    circ_queue.enqueue('c')
    circ_queue.enqueue('d')
    circ_queue.enqueue('e')
    print(len(circ_queue))
    print(circ_queue.nodes())
