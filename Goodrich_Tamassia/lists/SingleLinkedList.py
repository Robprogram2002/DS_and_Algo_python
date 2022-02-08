from __future__ import annotations
from Goodrich_Tamassia.linear_DA.EmptyError import Empty


class SingleLinkedList:
    class _Node:
        def __init__(self, item, next_ref):
            self.element = item
            self.next = next_ref

    class _LinkedIterator:
        """An iterator for any a linked list"""

        def __init__(self, head: SingleLinkedList._Node):
            """Create an iterator for the given sequence."""
            self._head = head  # keep a reference to the underlying data

        def __next__(self):
            """Return the next element, or else raise StopIteration error."""

            if self._head is not None:
                value = self._head.element
                self._head = self._head.next
                return value
            else:
                raise StopIteration()  # there are no more elements

        def __iter__(self):
            """By convention, an iterator must return itself as an iterator."""
            return self

    def __init__(self):
        self._size: int = 0
        self._head: SingleLinkedList._Node | None = None
        self._tail: SingleLinkedList._Node | None = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def append(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def add(self, value):
        new_node = self._Node(value, self._head)
        self._head = new_node
        self._size += 1
        if self._head is None:
            self._tail = new_node

    def remove(self):
        if self.is_empty():
            raise Empty('The linked list is empty')

        value = self._head.element
        self._head = self._head.next
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise Empty('The linked list is empty')
        return self._head.element

    def last(self):
        if self.is_empty():
            raise Empty('The linked list is empty')
        return self._tail.element

    def extend(self, other: SingleLinkedList):
        result = SingleLinkedList()
        current = self._head
        while current is not None:
            result.append(current.element)
            current = current.next

        for item in other:
            result.append(item)
        return result

    def _count_nodes(self, current):
        if current is None:
            return 0
        return 1 + self._count_nodes(current.next)

    def nodes(self):
        return self._count_nodes(self._head)

    def __str__(self) -> str:
        result = []
        current = self._head
        while current is not None:
            result.append(current.element)
            current = current.next
        return str(result)

    def __iter__(self):
        return self._LinkedIterator(self._head)


if __name__ == '__main__':
    link_list = SingleLinkedList()
    link_list.append(1)
    link_list.append(10)
    link_list.append(100)
    link_list.add(2)
    link_list.add(20)
    link_list.add(200)
    print(link_list.is_empty())
    print(len(link_list))
    print(link_list.nodes())
    print(link_list)
    print(link_list.first())
    print(link_list.last())
    list_B = SingleLinkedList()
    list_B.append('a')
    list_B.append('b')
    list_B.append('c')
    list_B.append('d')
    print(list_B)
    print(link_list.extend(list_B))
    for k in link_list:
        print(k)

# Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given
# references only to x and y. Repeat this exercise for the case when L is a doubly linked list. Which algorithm
# takes more time?

