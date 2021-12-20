from chapter3.LinkedList import Node

ordering = {
    0: "ascending",
    1: "descending"
}


class OrderedList:
    def __init__(self, order=0):
        self.head_ref = None
        self.order = ordering[order]

    def is_empty(self):
        return self.head_ref is None

    def size(self):
        current = self.head_ref
        count = 0
        while current is not None:
            current = current.get_next()
            count += 1
        return count

    def add(self, new_item):
        new_node = Node(new_item)
        # search for its place
        current = self.head_ref
        prev = None
        stop = False
        if self.order == "ascending":
            while current is not None and not stop:
                if current.get_data() > new_node.get_data():
                    stop = True
                else:
                    prev = current
                    current = current.get_next()
        else:
            while current is not None and not stop:
                if current.get_data() < new_node.get_data():
                    stop = True
                else:
                    prev = current
                    current = current.get_next()

        if prev is None:
            # the item must be placed at the beginning
            new_node.set_next(self.head_ref)
            self.head_ref = new_node
        else:
            # the item must go before current
            new_node.set_next(current)
            prev.set_next(new_node)

    def search(self, value):
        current = self.head_ref
        found = False
        if self.order == "ascending":
            while current is not None and not found:
                if current.get_data() == value:
                    found = True
                elif current.get_data() > value:
                    # the following nodes are greater than the search value
                    break
                else:
                    current = current.get_next()
        else:
            while current is not None and not found:
                if current.get_data() == value:
                    found = True
                elif current.get_data() < value:
                    # the following nodes are lower than the search value
                    break
                else:
                    current = current.get_next()
        return found

    def remove(self, item):
        current = self.head_ref
        prev = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.get_next()

        if found:
            if prev is None:
                # we are removing the first element
                self.head_ref = current.get_next()
            else:
                # we are removing a between element
                prev.set_next(current.get_next())
        else:
            raise RuntimeWarning("Item not found in the list")

    def index(self, value):
        current = self.head_ref
        found = False
        count = 0
        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
                count += 1

        if not found:
            count = -1

        return count

    def pop(self, position=None):
        current = self.head_ref
        prev = None
        if position == 0:
            # remove first item
            self.head_ref = self.head_ref.get_next()
            return
        elif position == self.size() - 1 or position is None:
            # remove the last item
            while current.get_next() is not None:
                prev = current
                current = current.get_next()

            # we want to remove current
            prev.set_next(current.get_next())
            return
        else:
            # remove an item in between
            found = False
            count = 0
            while current is not None and not found:
                if count == position:
                    found = True
                    # we want to remove current
                    prev.set_next(current.get_next())
                else:
                    prev = current
                    current = current.get_next()
                    count += 1

            if not found:
                raise RuntimeError("index out of the list elements range")

    def print_list(self):
        current_list = []
        current = self.head_ref
        while current is not None:
            current_list.append(current.get_data())
            current = current.get_next()
        print(current_list)


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.print_list()

print(mylist.size())

print(mylist.search(17))
print(mylist.search(-1))

print(mylist.index(17))
print(mylist.index(-4))

mylist.remove(26)
mylist.print_list()
mylist.remove(31)
mylist.print_list()
mylist.remove(54)
mylist.print_list()

mylist.add(-2)
mylist.print_list()

mylist.pop()
mylist.print_list()

mylist.pop((mylist.size() // 2))
mylist.print_list()

print("************************************************")

mylist = OrderedList(1)
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.print_list()

print(mylist.size())

print(mylist.search(17))
print(mylist.search(-1))

print(mylist.index(17))
print(mylist.index(-4))

mylist.remove(26)
mylist.print_list()
mylist.remove(31)
mylist.print_list()
mylist.remove(54)
mylist.print_list()

mylist.add(-2)
mylist.print_list()

mylist.pop()
mylist.print_list()

mylist.pop((mylist.size() // 2))
mylist.print_list()
