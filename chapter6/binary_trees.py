class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child: BinaryTree = None
        self.right_child: BinaryTree = None

    def insert_left(self, value):
        new_node = BinaryTree(value)
        if self.left_child is None:
            self.left_child = new_node
        else:
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        new_node = BinaryTree(value)
        if self.right_child is None:
            self.right_child = new_node
        else:
            new_node.right_child = self.right_child
            self.right_child = new_node

    def traverse_preorder(self):
        print(self.key)
        # The internal method must check for the existence of the left and the right children before making the
        # recursive call
        if self.left_child is not None:
            self.left_child.traverse_preorder()
        if self.right_child is not None:
            self.right_child.traverse_preorder()

    def traverse_postorder(self):
        if self.left_child is not None:
            self.left_child.traverse_preorder()
        if self.right_child is not None:
            self.right_child.traverse_preorder()
        print(self.key)

    def traverse_inorder(self):
        if self.left_child is not None:
            self.left_child.traverse_preorder()
            print(self.key)

        if self.right_child is not None:
            self.right_child.traverse_preorder()

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


#  Notice that both the left and right children of the root are themselves
# distinct instances of the BinaryTree class. This allows us to treat any child of a binary tree as
# a binary tree itself.


r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())


# Since the entire binary heap can be represented by a single list, all the constructor will do is initialize the list
# and an attribute current_size to keep track of the current size of the heap

class BinaryHeap:

    def __init__(self):
        #  an empty binary heap has a single zero as the first element of heap_list and that this zero is not used,
        #  but is there so that simple integer division can be used in later methods.
        self.heap_list = [0]
        self.current_size = 0

    # percolates a new item as far up in the tree as it needs to go to
    # maintain the heap property.
    def percolates_up(self, i):
        # The parent of the current node can be computed by dividing the index of the current node by 2.
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        #  Once a new item is appended to the tree, percolates_up takes over and positions the new item properly.
        self.percolates_up(self.current_size)

    def percolates_down(self, i):
        while (i * 2) <= self.current_size:
            mc_index = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc_index]:
                # percolates
                self.heap_list[i], self.heap_list[mc_index] = self.heap_list[mc_index], self.heap_list[i]
            i = mc_index

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            # if there is not right node, then return the left
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                # if left node is lower than right node, return left
                return i * 2
            else:
                # return right
                i * 2 + 1

    def del_min(self):
        old_min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolates_down(1)
        return old_min

    def build_binary_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.percolates_down(i)
            i -= 1

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def find_min(self):
        return self.heap_list[1]
