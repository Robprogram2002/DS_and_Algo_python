import os


# factorial
def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# A recursive algorithm for computing the sum of the 1st  n numbers in a sequence

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

def conv_str_to_num(string: str, n=0):
    if n == len(string) - 1:
        return int(string[n])
    else:
        return int(string[n]) * (10 ** (len(string) - 1 - n)) + conv_str_to_num(string, n + 1)


def conv_str_to_num2(string: str, n):
    if n == 1:
        return int(string[-1])
    else:
        return int(string[len(string) - n]) * (10 ** (n - 1)) + conv_str_to_num2(string, n - 1)


print('convert string to number 13531 : ', conv_str_to_num('13531'))
print('convert string to number 239412 : ', conv_str_to_num('239412'))
print(type(conv_str_to_num('239412')))

print('convert string to number2 13531 : ', conv_str_to_num2('13531', len('13531')))
print('convert string to number2 239412 : ', conv_str_to_num2('239412', len('239412')))
print(type(conv_str_to_num('239412')))


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
print(max_min_recursive([0, 0, 0, 0, 1, 0, 0, ], 7))


# Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.

def int_log2(n: int, i=0):
    value = n + 0
    count = 0
    while value > 2:
        value = value / 2
        count += 1
    return count


def int_log2_recursive(n):
    if n < 2:
        return 0
    return 1 + int_log2_recursive(n / 2)


print(int_log2(100), int_log2(40))
print(int_log2_recursive(100), int_log2_recursive(40))


# Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at
# most O(n^2) in the worst case without using sorting

def is_uniqueness(s: [], start):
    if start < len(s) - 1:
        for j in range(start + 1, len(s)):
            if s[start] == s[j]:
                return False
        return is_uniqueness(s, start + 1)
    return True


print('is unique: ', is_uniqueness([2, 5, -8, 3, -123, 43, 1, 2, 0], 0))


# Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction

def recursive_prod(n: int, m: int):
    if m == 0:
        return 0
    else:
        return n + recursive_prod(n, m - 1)


print(recursive_prod(4, 3))
print(recursive_prod(7, 5))
print(recursive_prod(11, 11))


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

def recursive_palind_check(string: str, start, end):
    if start >= end - 1:
        return True

    if string[start] == string[end - 1]:
        return recursive_palind_check(string, start + 1, end - 1)
    else:
        return False


print(recursive_palind_check('racecar', 0, len('racecar')))
print(recursive_palind_check('gohangasalamiimalasagnahog', 0, len('gohangasalamiimalasagnahog')))
print(recursive_palind_check('dog&god', 0, len('dog&god')))
print(recursive_palind_check('dog&good', 0, len('dog&good')))
print(recursive_palind_check('superduper', 0, len('superduper')))


# Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.

def compare(string: str):
    if string in 'aeiou':
        return 1
    elif string in 'bcdfghjklmnpqrstvwxyz':
        return -1
    else:
        return 0


def counter(string: str, n: int):
    if n == 1:
        return compare(string[n - 1])
    else:
        return compare(string[n - 1]) + counter(string, n - 1)


def vowels_vs_consonants(string: str, n: int):
    count = counter(string, n)
    print(count)
    if count > 0:
        return 'vowels win!!'
    elif count < 0:
        return 'consonants win!!'
    else:
        return 'no one win !!'


print(vowels_vs_consonants('there is a beautiful cat here', len('there is a beautiful cat here')))
print(vowels_vs_consonants('i am  a good person too', len('i am  a good person too')))


# Write a short recursive Python function that rearranges a sequence of integer values so that all  the even values
# appear before all the odd values

def rearrange_even_odd(data: [], start, end):
    if start < end - 1:
        if data[start] % 2 != 0:
            if data[end - 10] % 2 == 0:
                data[start], data[end - 1] = data[end - 1], data[start]
                rearrange_even_odd(data, start + 1, end - 1)
            else:
                rearrange_even_odd(data, start, end - 1)
        else:
            rearrange_even_odd(data, start + 1, end)
    else:
        print(start)  # mid/break index


array = [3, 56, 1, 2, 568, 3, 23, 66, 8, 12, 46, 82, 12, 5]
rearrange_even_odd(array, 0, len(array))
print(array)


# Given an unsorted sequence, S, of integers and an integer k, describe a
# recursive algorithm for rearranging the elements in S so that all elements
# less than or equal to k come before any elements larger than k.

def rearrange_k(data: [], k, start, end):
    if start < end - 1:
        if data[start] > k:
            if data[end - 1] <= k:
                data[start], data[end - 1] = data[end - 1], data[start]
                rearrange_k(data, k, start + 1, end - 1)
            else:
                rearrange_k(data, k, start, end - 1)
        else:
            rearrange_k(data, k, start + 1, end)
    else:
        print(start)  # mid/break index


rearrange_k(array, 50, 0, len(array))
print(array)


# Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order.
# Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair
# exists

def find_sum_elements(data: [], k, start, end):
    if start < end - 1 and data[start] < k:
        search = k - data[start]
        if data[end - 1] == search:
            return start, end - 1
        elif data[end - 1] > search:
            return find_sum_elements(data, k, start, end - 1)
        else:
            return find_sum_elements(data, k, start + 1, len(data))

    return None


array = [2, 3, 4, 5, 6, 7, 8]
print(find_sum_elements(array, 15, 0, len(array)))


# Implement a recursive function with signature find(path, filename) that
# reports all entries of the file system rooted at the given path having the
# given file name.

def is_file_in_dir(path: str, filename: str):
    found = False
    if os.path.isdir(path):
        for name in os.listdir(path):
            if name == filename:
                found = True
    return found


dir = 'C:\\Users\\rober\\PycharmProjects\\DS_and_Algorithms_Python\\Goodrich_Tamassia\\recursion'
print(is_file_in_dir(dir, 'disk_usage.py'))
print(is_file_in_dir(dir, 'random_name.py'))

# Write a program that can solve instances of the Tower of Hanoi problem


# Python’s os module provides a function with signature walk(path) that is a generator yielding the tuple (dirpath,
# dirnames, filenames) for each subdirectory of the directory identified by string path, such that string dirpath is
# the full path to the subdirectory, dirnames is a list of the names of the subdirectories within dirpath,and filenames
# is a list of the names of non-directory entries of dirpath. Give your own implementation of such a walk function.
