class DoublyLinkedList:
    class _Node:
        def __init__(self, data, next_ref=None, prev_ref=None):
            self.item = data
            self.next = next_ref
            self.prev = prev_ref

    class _ForwardIterator:

        def __init__(self, first):
            self._head = first

        def __next__(self):
            if self._head.next is not None:
                value = self._head.item
                self._head = self._head.next
                return value
            else:
                raise StopIteration()  # there are no more elements

        def __iter__(self):
            """By convention, an iterator must return itself as an iterator."""
            return self

    class _BackwardIterator:

        def __init__(self, last):
            self._tail = last

        def __next__(self):
            if self._tail.prev is not None:
                value = self._tail.item
                self._tail = self._tail.prev
                return value
            else:
                raise StopIteration()  # there are no more elements

        def __iter__(self):
            """By convention, an iterator must return itself as an iterator."""
            return self

    def __init__(self):
        self._n = 0
        head_sentinel = self._Node(None)
        tail_sentinel = self._Node(None, None, head_sentinel)
        head_sentinel.next = tail_sentinel
        self._head: DoublyLinkedList._Node = head_sentinel
        self._tail: DoublyLinkedList._Node = tail_sentinel

    def __len__(self):
        return self._n

    def size(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def add_head(self, value):
        self._add(value, self._head, self._head.next)

    def add_tail(self, value):
        self._add(value, self._tail.prev, self._tail)

    def remove_head(self):
        if self.is_empty():
            raise Exception('Cannot remove an element from an empty list')
        self._remove(self._head.next)

    def remove_tail(self):
        if self.is_empty():
            raise Exception('Cannot remove an element from an empty list')
        self._remove(self._tail.prev)

    def _add(self, value, prev_node: _Node, next_node: _Node):
        new_node = self._Node(value, next_node, prev_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self._n += 1

    def _remove(self, node: _Node):
        node.prev.next, node.next.prev = node.next, node.prev
        node = None
        self._n -= 1

    def __contains__(self, value):
        current = self._head.next
        found = False
        while current is not self._tail and not found:
            if current.item == value:
                found = True
            else:
                current = current.next
        return found

    def search(self, value):
        return self.__contains__(value)

    def index(self, value):
        current = self._head.next
        found = False
        count = 0
        while current is not self._tail and not found:
            if current.item == value:
                found = True
            else:
                current = current.next
                count += 1

        return count if found else -1

    def insert(self, position, item):
        if position == 0:
            return self.add_head(item)
        elif position == self.size() - 1:
            return self.add_tail(item)
        elif 0 < position < self.size():
            current = self._head.next
            count = 0

            while current is not self._tail:
                if count == position:
                    return self._add(item, current, current.next)
                else:
                    current = current.next
                    count += 1
        else:
            raise RuntimeError("index out of the list elements range")

    def remove(self, value):
        current = self._head.next
        while current is not self._tail:
            if current.item == value:
                return self._remove(current)
            else:
                current = current.next

        raise RuntimeWarning("Item not found in the list")

    def __reversed__(self):
        return self._BackwardIterator(self._tail.prev)

    def __iter__(self):
        return self._ForwardIterator(self._head.next)

    def __str__(self):
        return str([element for element in self])


if __name__ == '__main__':
    list_a = DoublyLinkedList()
    print(len(list_a))
    print(list_a.size())
    list_a.add_head(1)
    list_a.add_head(10)
    list_a.add_head(100)
    list_a.add_tail(2)
    list_a.add_tail(20)
    list_a.add_tail(200)
    print(list_a)
    print(list_a.is_empty())
    print(2 in list_a)
    print(list_a.search(2))
    print(list_a.index(-2))
    list_a.remove_head()
    list_a.remove_tail()
    list_a.remove(1)
    print(list_a)
    for k in reversed(list_a):
        print(k, end='\t')
