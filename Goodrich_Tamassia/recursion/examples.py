# A recursive algorithm for computing the sum of a sequence of numbers

def linear_sum(data: [], n: int):
    if len(data) == 0:
        return 0
    else:
        return linear_sum(data, n - 1) + data[n - 1]


# For an input of size n, the linear sum algorithm makes n+1 function
# calls. Hence, it will take O(n) time, because it spends a constant amount of time
# performing the nonrecursive part of each call. Moreover, we can also see that the
# memory space used by the algorithm (in addition to the sequence) is also O(n), as
# we use a constant amount of memory space for each of the n+1 activation records
# in the trace at the time we make the final recursive call (with n = 0)


# Next, let us consider the problem of reversing the n elements of a sequence.  We can solve this problem using
# linear recursion, by observing that the reversal of a sequence can be achieved by swapping the first and last elements
# and then recursively reversing the remaining elements

def reverse(data: [], start: int, last: int):
    if start < last - 1:
        data[start], data[last - 1] = data[last - 1], data[start]  # swap first and last
        reverse(data, start + 1, last - 1)  # recur on rest


# Note that there are two implicit base case scenarios: When start == stop, the
# implicit range is empty, and when start == stop−1, the implicit range has only
# one element. In either of these cases, there is no need for action, as a sequence
# with zero elements or one element is trivially equal to its reversal. When otherwise
# invoking recursion, we are guaranteed to make progress towards a base case, as
# the difference, stop−start, decreases by two with each call
# If n is even, we will eventually reach the start == stop case, and if n is odd, we will
# eventually reach the start == stop − 1 case.

# The above argument implies that the recursive algorithm  is guaranteed to terminate after a total of 1 + [n/2]
# recursive calls. Since each call involves a constant amount of work, the entire process runs in O(n) time.

# We consider the problem of raising a number x to an arbitrary nonnegative integer, n. That is, we wish
# to compute the power function, defined as power(x,n) = x^n. We will consider two different recursive formulations for
# the problem that lead to algorithms with very different performance.

def power1(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n - 1)


# A recursive call to this version of power(x,n) runs in O(n) time.

def power2(x, n):
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)  # rely on truncated division
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


# in each recursive call of function power(x,n) is at most half of the preceding
# exponent. As we saw with the analysis of binary search, the number of times that
# we can divide n in half before getting to one or less is O(logn). Therefore, our new
# formulation of the power function results in O(logn) recursive calls of constant time and space.


# Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.

def max_recursive(data: [], n):
    if n <= 1:
        return data[0]
    prev_max = max_recursive(data, n - 1)
    if prev_max > data[n - 1]:
        return prev_max
    else:
        return data[n - 1]


def min_recursive(data: [], n):
    if n <= 1:
        return data[0]
    prev_min = min_recursive(data, n - 1)
    if prev_min < data[n - 1]:
        return prev_min
    else:
        return data[n - 1]


print(max_recursive([-1, 4, -3, 20, 1, 0, 8, 5, 3], 9))
print(min_recursive([-1, 4, -3, 20, 1, 0, 8, 5, 3], 9))


# Describe a recursive function for computing the n^th Harmonic number

def harmonic(n: int):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic(n - 1)


print(harmonic(4))
print(1 + 1 / 2 + 1 / 3 + 1 / 4)


# Describe a recursive function for converting a string of digits into the integer it represents. For example, '13531'
# represents the integer 13,531

def conv_str_to_num(string: str, n):
    print('next')


print(conv_str_to_num('13531', len('13531')))


# Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any
# loop

def max_min_recursive(data: [], n):
    if n <= 1:
        return data[0], data[0]
    prev_pair = max_min_recursive(data, n - 1)
    if prev_pair[0] < data[n - 1]:
        if prev_pair[1] > data[n - 1]:
            return prev_pair
        else:
            return prev_pair[0], data[n - 1]
    else:
        return data[n - 1], prev_pair[1]


print(max_min_recursive([-1, 4, -3, 20, 1, 0, 8, 5, 3], 9))


# Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction

# Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).

# Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop .

def reverse_string(string: str):
    str_list = [char for char in string]
    reverse(str_list, 0, len(str_list))
    return ''.join(str_list)


print(reverse_string('pots&pans'))

#  Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse

# Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.

# Write a short recursive Python function that rearranges a sequence of integer values so that all  the even values
# appear before all the odd values

# Given an unsorted sequence, S, of integers and an integer k, describe a
# recursive algorithm for rearranging the elements in S so that all elements
# less than or equal to k come before any elements larger than k.

# Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order.
# Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair
# exists

# Implement a recursive function with signature find(path, filename) that
# reports all entries of the file system rooted at the given path having the
# given file name.

# Write a program that can solve instances of the Tower of Hanoi problem
