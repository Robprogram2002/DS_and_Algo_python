# The following stack implementation assumes that the end of the list will hold the top element
# of the stack. As the stack grows (as push operations occur), new items will be added on the
# end of the list. pop operations will manipulate that same end

class Stack:
    def __init__(self, new_list=None):
        self.items = new_list if new_list is not None else []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def print_stack(self):
        print(self.items)


# It is important to note that we could have chosen to implement the stack using a list where
# the top is at the beginning instead of at the end. The implementation is shown below.

class StackV2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# This ability to change the physical implementation of an abstract data type while maintaining
# the logical characteristics is an example of abstraction at work. However, even though the
# stack will work either way, if we consider the performance of the two implementations, there
# is definitely a difference

# The performance of the second implementation suffers in that
# the insert(0) and pop(0) operations will both require 𝑂(𝑛) for a stack of size 𝑛. Clearly, even
# though the implementations are logically equivalent, they would have very different timings
# when performing benchmark testing.


# Exercise 1: Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.

def rev_string(my_str):
    str_stack = Stack()
    for char in my_str:
        str_stack.push(char)
    return ''.join([str_stack.pop() for k in range(len(my_str))])


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')

    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

    print(rev_string("dog"))
    print(rev_string("superduper"))
    print(rev_string(rev_string("anagram")))
