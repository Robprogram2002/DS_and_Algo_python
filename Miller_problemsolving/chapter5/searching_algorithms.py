# TODO: Sequential Search

def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))


# TODO: Ordered Sequential Search

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))


# TODO: Binary Search

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        print("----step----")
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if a_list[midpoint] > item:
                # then item may be at the left half of the list
                last = midpoint - 1
            else:
                # then item may be at the right half of the list
                first = midpoint + 1
    return found


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(test_list, 3))
print(binary_search(test_list, 19))


def recursive_binary_search(a_list, item):
    print('------recursive step-----')
    if len(a_list) == 0:
        return False
    else:
        midpoint = (len(a_list) - 1) // 2
        if a_list[midpoint] == item:
            return True
        elif a_list[midpoint] > item:
            # left half
            return recursive_binary_search(a_list[:midpoint], item)
        else:
            # right half
            return recursive_binary_search(a_list[midpoint + 1:], item)


# print(recursive_binary_search(test_list, 19))
# print(recursive_binary_search(test_list, 3))


# In the recursive solution shown above, the recursive call, binary_search(a_list[:midpoint],item).
# uses the slice operator to create the left half of the list that is then passed to the next invocation
# (similarly for the right half as well).
# However, we know that the slice operator in Python is actually
# 𝑂(𝑘). This means that the binary search using slice will not perform in strict logarithmic time.
# Luckily this can be remedied by passing the list along with the starting and ending indices

def recursive_binary_search_v2(a_list, item, start, end):
    print('------recursive step v2 {} : {}-----'.format(start, end))
    if end == start:
        return False
    else:
        midpoint = (end + start) // 2
        if a_list[midpoint] == item:
            return True
        elif a_list[midpoint] > item:
            # left half
            return recursive_binary_search_v2(a_list, item, start, midpoint - 1)
        else:
            # right half
            return recursive_binary_search_v2(a_list, item, midpoint + 1, end)


print(recursive_binary_search_v2(test_list, 3, 0, len(test_list) - 1))
print(recursive_binary_search_v2(test_list, 19, 0, len(test_list) - 1))


# TODO: HASH FUNCTION

# The code below shows a function called hash that takes a string
# and a table size and returns the hash value in the range from 0 to table_size−1.

def hash_function(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum + ord(a_string[pos])
    return sum % table_size


# It is interesting to note that when using this hash function, anagrams will always be given
# the same hash value. To remedy this, we could use the position of the character as a weight.

def hash_weighted_function(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum += ord(a_string[pos]) * (pos + 1)
    return sum % table_size

# You may be able to think of a number of additional ways to compute hash values for items
# in a collection. The important thing to remember is that the hash function has to be efficient
# so that it does not become the dominant part of the storage and search process. If the hash
# function is too complex, then it becomes more work to compute the slot name than it would be
# to simply do a basic sequential or binary search as described earlier. This would quickly defeat
# the purpose of hashing

