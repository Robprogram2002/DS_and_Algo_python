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
