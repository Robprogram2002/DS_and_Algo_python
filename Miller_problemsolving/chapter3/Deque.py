# Our implementation will assume that the rear of th deque is at position 0 in the list

class Deque:
    def __init__(self, new_list=None):
        if new_list is None:
            self.items = []
        else:
            self.items = new_list

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)

# You are also likely to observe that in this implementation adding and removing items from the front
# is 𝑂(1) whereas adding and removing from the rear is 𝑂(𝑛). This is to be expected given the
# common operations that appear for adding and removing items. Again, the important thing is
# to be certain that we know where the front and rear are assigned in the implementation
