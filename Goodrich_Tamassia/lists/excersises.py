from random import randrange


# Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive, with exactly one repeated. Describe a
# fast algorithm for finding the integer in A that is repeated

def find_duplicated(data: []):
    return sum(data) - sum(k for k in range(1, len(data)))

    # data.sort()
    # for i in range(len(data)-1):
    #     if data[i] == data[i + 1]:
    #         return data[i]
    # return None


print(find_duplicated([7, 2, 1, 4, 3, 5, 6, 4]))


# The shuffle method, supported by the random module, takes a Python
# list and rearranges it so that every possible ordering is equally likely.
# Implement your own version of such a function. You may rely on the
# randrange(n) function of the random module, which returns a random
# number between 0 and n−1 inclusive

def shuffle(data: []):
    n = len(data)
    for i in range(n - 1, 0, -1):
        rand_index = randrange(0, n)
        data[rand_index], data[i] = data[i], data[rand_index]
    return data


print(shuffle([3, 10, -2, -33, -12, 5, 100, 1.42, -23.1]))

# Let B be an array of size n ≥ 6 containing integers from 1 to n−5, inclusive, with exactly five repeated.
# Describe a good algorithm for finding the five integers in B that are repeated

# A useful operation in databases is the natural join. If we view a database
# as a list of ordered pairs of objects, then the natural join of databases A
# and B is the list of all ordered triples (x,y,z) such that the pair (x,y) is in
# A and the pair (y,z) is in B. Describe and analyze an efficient algorithm
# for computing the natural join of a list A of n pairs and a list B of m pairs.

data_A = [(1, 2), (2, 8), (-3, 0), (4, -2), (0, 1), (43, -12)]
data_B = [(2, 10), (10, 1), (0, 0), (-12, 4), (-2, 4), (72, 227)]


def element_wise_join(list_a: [], list_b: []):
    new_list = []
    for k in range(len(list_a)):
        if list_a[k][1] == list_b[k][0]:
            new_list.append((list_a[k][0], list_a[k][1], list_b[k][1]))

    return new_list


print(element_wise_join(data_A, data_B))


def natural_join_bad(list_a: [], list_b: []):
    new_list = []
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i][1] == list_b[j][0]:
                new_list.append((list_a[i][0], list_a[i][1], list_b[j][1]))
    return new_list


print(natural_join_bad(data_A, data_B))


# Write a Python function that takes two three-dimensional numeric data
# sets and adds them componentwise.

def add_nth_list_2dim(data_a: [], data_b: []):
    result = [k for k in data_a]
    for k in range(len(data_a)):
        for j in range(len(data_a[0])):
            result[k][j] += data_b[k][j]
    return result


data_A = [[1, 2, 5, 1], [2, 8, 3, 2], [-3, 0, -2, -3], [4, -2, 15, 4], [0, 1, -2, 0]]
data_B = [[2, 10, 1, 2], [10, 1, 4.6, 10], [0, 0, -10, 0], [-12, 4, 2, -12], [-2, 4, 0, -2]]

print(add_nth_list_2dim(data_A, data_B))

data_A = [[[1, 2, 5, 1], [2, 8, 3, 2], [-3, 0, -2, -3]], [[4, -2, 15, 4], [0, 1, -2, 0], [10, 22, 0, 2]]]
data_B = [[[2, 10, 1, 2], [10, 1, 4.6, 10], [0, 0, -10, 0]], [[-12, 4, 2, -12], [-2, 4, 0, -2], [10, 22, 0, 2]]]


def add_nth_list_3dim(data_a: [], data_b: []):
    result = [k for k in data_a]
    for k in range(len(data_a)):
        for j in range(len(data_a[0])):
            for i in range(len(data_a[0][0])):
                result[k][j][i] += data_b[k][j][i]
    return result


print(add_nth_list_3dim(data_A, data_B))

# Suppose that x and y are references to nodes of circularly linked lists, although not necessarily the same list.
# Describe a fast algorithm for telling if x and y belong to the same list.

# Give a fast algorithm for concatenating two doubly linked lists L and M, with header and trailer sentinel nodes,
# into a single list L'

# Implement a function, with calling syntax max(L), that returns the maximum element from a PositionalList instance
# L containing comparable elements.

# Redo the previously problem with max as a method of the PositionalList class, so that calling syntax L.max() is
# supported.

# Update the PositionalList class to support an additional method find(e), which returns the position of the
# (first occurrence of) element e in the list (or None if not found).

# Repeat the previous process using recursion. Your method should not contain any loops

# Provide support for a __reversed__ method of the PositionalList class that is similar to the given __iter__
# , but that iterates the elements in reversed order.

# Implement a clear() method for the FavoritesList class that returns the list to empty.

# Implement a reset counts() method for the FavoritesList class that resets all elements’ access counts to zero
# (while leaving the order of the list unchanged).

# Give a complete implementation of the stack ADT using a singly linked list that includes a header sentinel.

# Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and appends
# them to the end of the original queue. The operation should run in O(1) time and should result in Q2 being an empty
# queue

# Describe a fast recursive algorithm for reversing a singly linked list.

# Design a circular positional list ADT that abstracts a circularly linked list in the same way that the positional
# list ADT abstracts a doubly linked list, with a notion of a designated “cursor” position within the list.

# Modify the DoublyLinkedBase class to include a reverse method that reverses the order of the list, yet without 
# creating or destroying any nodes.

# Modify the PositionalList class to support a method swap(p, q) that causes the underlying nodes referenced by
# positions p and q to be exchanged for each other

# Implement a function that accepts a PositionalList L of n integers sorted in nondecreasing order, and another valueV,
# and determines in O(n) time if there are two elements ofL that sum precisely toV. The function should return a pair of
# positions of such elements, if found, or None otherwise.

# Write a Scoreboard class that maintains the top 10 scores for a game application using a singly linked list,

# Describe a method for performing a card shuffle of a list of 2n elements, by converting it into two lists. A card
# shuffle  is a permutation where a list L is cut into two lists, L1 and L2,where L1 is the first half of L and L2 is
# the second half of L, and then these two lists are merged into one by taking the first element in L1, then the first
# element in L2, followed by the second element in L1, the second element in L2, and so on.

# An array A is sparse if most of its entries are empty (i.e., None). A list L can be used to implement such an array
# efficiently. In particular, for each nonempty cell A[i], we can store an entry (i,e) in L,where e is the element
# stored at A[i]. This approach allows us to represent A using O(m) storage, where m is the number of nonempty entries
# in A. Provide such a SparseArray class
