# The special Python reference value None will play an important role in the Node class and
# later in the linked list itself. A reference to None will denote the fact that there is no next
# node. Note in the constructor that a node is initially created with next set to None. Since this
# is sometimes referred to as “grounding the node,” we will use the standard ground symbol to
# denote a reference that is referring to None.

class Node:
    def __init__(self, data, next_ref=None):
        self.item = data
        self.next = next_ref

    def get_data(self):
        return self.item

    def set_data(self, new_data):
        self.item = new_data

    def set_next(self, new_location):
        self.next = new_location

    def get_next(self):
        return self.next


temp = Node(93)
print(temp.get_data())


# the unordered list will be built from a collection of nodes, each linked
# to the next by explicit references. As long as we know where to find the first node (containing
# the first item), each item after that can be found by successively following the next links. With
# this in mind, the UnorderedList class must maintain a reference to the first node.

# The head of the list refers to the first node which contains the first item
# of the list. In turn, that node holds a reference to the next node (the next item) and so on. It
# is very important to note that the list class itself does not contain any node objects. Instead it
# contains a single reference to only the first node in the linked structure

class LinkedList:

    def __init__(self):
        # None will again be used to state that the head of the list does not refer to anything.
        self.head_ref = None
        self.tail_ref = None

    # checks to see if the head of the list is a reference to None
    # (This shows the advantage to using the reference None to denote the “end” of the linked structure)
    def is_empty(self):
        return self.head_ref is None

    # how do we get items into our list? We need to implement the add method. However, before
    # we can do that, we need to address the important question of where in the linked list to place
    # the new item. Since this list is unordered, the specific location of the new item with respect to
    # the other items already in the list is not important. The new item can go anywhere. With that
    # in mind, it makes sense to place the new item in the easiest location possible.

    # Recall that the linked list structure provides us with only one entry point, the head of the list.
    # All of the other nodes can only be reached by accessing the first node and then following next
    # links. This means that the easiest place to add the new node is right at the head, or beginning,
    # of the list. In other words, we will make the new item the first item of the list and the existing
    # items will need to be linked to this new first item so that they follow.

    def add(self, new_item):
        new_node = Node(new_item, self.head_ref)
        self.head_ref = new_node

        if self.is_empty():
            self.tail_ref = new_node
            # The order of the two steps described above is very important.

    # The next methods that we will implement-size, search, and remove-are all based on a technique
    # known as linked list traversal. Traversal refers to the process of systematically visiting each
    # node. To do this we use an external reference that starts at the first node in the list. As we visit
    # each node, we move the reference to the next node by “traversing” the next reference.

    # To implement the size method, we need to traverse the linked list and keep a count of the
    # number of nodes that occurred
    def size(self):
        # At the start of the process we have not seen any nodes so the count is set to 0.
        current = self.head_ref
        count = 0
        # As long as the current reference has not seen the
        # end of the list (None), we move current along to the next node via the assignment statement
        while current is not None:
            current = current.get_next()
            count += 1
        #  Finally, count gets returned after the iteration stops.
        return count

    # As we visit each node in the linked list we will ask whether the data stored there
    # matches the item we are looking for. In this case, however, we may not have to traverse all the
    # way to the end of the list. In fact, if we do get to the end of the list, that means that the item we
    # are looking for must not be present. Also, if we do find the item, there is no need to continue.
    def search(self, value):
        current = self.head_ref
        found = False
        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    # First, we need to traverse the list looking for the
    # item we want to remove. Once we find the item , we must
    # remove it. But how do we remove it?
    # In order to remove the node containing the item, we need to modify the link in the previous
    # node so that it refers to the node that comes after current. Unfortunately, there is no way to go
    # backward in the linked list. Since current refers to the node ahead of the node where we would
    # like to make the change, it is too late to make the necessary modification.
    # The solution to this dilemma is to use two external references as we traverse down the linked
    # list
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
            elif current.get_next() is None:
                # we are removing the last element
                self.tail_ref = prev
                prev.set_next(None)
            else:
                # we are removing a between element
                prev.set_next(current.get_next())
        else:
            raise RuntimeWarning("Item not found in the list")

    # insert, index, and pop require that we name the positions of the list.
    # We will assume that position names are integers starting with 0

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

        return count if found else -1

    def append(self, item):
        new_node = Node(item)
        self.tail_ref.set_next(new_node)
        self.tail_ref = new_node

    def insert(self, position, item):
        if position == 0:
            return self.add(item)
        elif position == self.size() - 1:
            return self.append(item)

        new_node = Node(item)
        current = self.head_ref
        prev = None
        count = 0
        found = False

        while current is not None and not found:
            if count == position:
                new_node.set_next(current)
                prev.set_next(new_node)
                found = True
            else:
                prev = current
                current = current.get_next()
                count += 1

        if not found:
            raise RuntimeError("index out of the list elements range")

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
            self.tail_ref = prev
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


if __name__ == '__main__':
    mylist = LinkedList()
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

    mylist.append(-2)
    mylist.append("The end")
    mylist.print_list()

    mylist.insert(0, "the start")
    mylist.print_list()
    mylist.insert(mylist.size() - 1, "The end 2")
    mylist.print_list()
    mylist.insert(mylist.size() // 2, "The middle")
    mylist.print_list()

    mylist.pop()
    mylist.print_list()

    mylist.pop((mylist.size() // 2) + 1)
    mylist.print_list()

# TODO: str method
# Implement the __str__ method in the UnorderedList class. What would be a good string
# representation for a list?
# Implement __str__ method so that lists are displayed the Python way (with square brackets).

# TODO: Implement a slice method for the UnorderedList class.
# It should take two parameters,
# start and stop, and return a copy of the list starting at the start position and going up to
# but not including the stop position.

# TODO:
# Implement a stack using linked lists.
# Implement a queue using linked lists.
# Implement a deque using linked lists.

# TODO: implement a doubly linked list
