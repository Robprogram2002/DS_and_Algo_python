import re


# Calculating the Sum of a List of Numbers
def list_sum(num_list, start: int, end: int):
    # This check is crucial and is our escape clause from the function. The sum of
    # a list of length 1 is trivial; it is just the number in the list
    if start == end - 1:
        return num_list[start]
    else:
        return num_list[start] + list_sum(num_list, start + 1, end)

    # You should think of this series of calls as a series of simplifications. Each time we make a recursive
    # call we are solving a smaller problem, until we reach the point where the problem cannot get
    # any smaller.

    # When we reach the point where the problem is as simple as it can get, we begin to piece together
    # the solutions of each of the small problems until the initial problem is solved


print(list_sum([1, 3, 5, 7, 9, -2], start=0, end=6))


# Converting an Integer to a String in Any Base

# Suppose you want to convert an integer to a string in some base between binary and hexadecimal. For example, convert
# the integer 10 to its string representation in decimal as “10,” or
# to its string representation in binary as “1010.”
# Suppose we have a sequence

# of characters corresponding to the first 10 digits, like conv_string = “0123456789”. It is
# easy to convert a number less than 10 to its string equivalent by looking it up in the sequence.
# For example, if the number is 9, then the string is conv_string[9] or “9.” If we can arrange to
# break up the number 769 into three single-digit numbers, 7, 6, and 9, then converting it to a
# string is simple. Then A number less than 10 sounds like a good base case.

# The next step is to figure out how to change state and make progress toward the base case.
# Let’s look at what happens if we divide a number by the base we are trying to convert to.

# Using integer division to divide 769 by 10, we get 76 with a remainder of 9. This gives us two
# good results. First, the remainder is a number less than our base that can be converted to a
# string immediately by lookup. Second, we get a number that is smaller than our original and
# moves us toward the base case of having a single number less than our base. Now our job is to
# convert 76 to its string representation. Again we will use integer division plus remainder to get
# results of 7 and 6 respectively. Finally, we have reduced the problem to converting 7, which we
# can do easily since it satisfies the base case condition of 𝑛 <base, where base= 10

# implementation

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


print(to_str(1245, 10))
print(to_str(233, 8))
print(to_str(233, 9))
print(to_str(233, 16))
print(to_str(333, 16))
print(to_str(10, 2))


# When we detect the base case, we stop recursing and simply return the string from the
# convertString sequence. In line 6 we satisfy both the second and third laws – by making the
# recursive call and by reducing the problem size – using division.

# Suppose that instead of concatenating the result of the recursive call to toStr with the string
# from convertString, we modified our algorithm to push the strings onto a stack prior to making
# the recursive call.


# The previous example gives us some insight into how Python implements a recursive function
# call. When a function is called in Python, a stack frame is allocated to handle the local variables of the function.
# When the function returns, the return value is left on top of the stack for
# the calling function to access.


# TODO : Write a function that takes a string as a parameter and returns a new string that is the reverse
#  of the old string.

def reverse_str(text):
    if len(text) == 1:
        return text
    else:
        return reverse_str(text[1:]) + text[0]


def _reverse_list(data: [], start, end):
    if start < end:
        data[start], data[end] = data[end], data[start]
        _reverse_list(data, start + 1, end - 1)


def reverse_str_v2(text: str):
    letters = list(text)
    _reverse_list(letters, start=0, end=len(letters) - 1)
    return ''.join(letters)


print(reverse_str("transformer"))
print(reverse_str_v2("transformer"))


# TODO: Write a function that takes a string as a parameter and returns true if the string is a palindrome
#  and False otherwise

def is_palindrome(text):
    new_text = re.sub(r'[,;.\'\"\’]', '', text.lower().replace(" ", ""))
    reverse = reverse_str(new_text)

    if new_text == reverse:
        return True
    else:
        return False


# using only recursion
def is_palindrome2(text: str, start: int, end: int):
    if start < end:
        if text[start].isalpha():
            if text[end - 1].isalpha():
                if text[start] == text[end - 1]:
                    return is_palindrome2(text, start + 1, end - 1)
                else:
                    return False
            else:
                return is_palindrome2(text, start, end - 1)
        else:
            return is_palindrome2(text, start + 1, end)
    return True


text1 = "Reviled did I live, said I, as evil I did deliver"
text2 = "is a false palindrome"
text3 = "Go hang a salami; I’m a lasagna hog"

print(is_palindrome(text1))
print(is_palindrome(text2))
print(is_palindrome(text3))

print('-----------')
print(is_palindrome2(text1.lower(), 0, len(text1)))
print(is_palindrome2(text2.lower(), 0, len(text2)))
print(is_palindrome2(text3.lower(), 0, len(text3)))


# TODO: Write a recursive function to compute the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(5))
print(factorial(10))


# TODO: Write a recursive function to reverse a list.

def reverse_list(data: []):
    _reverse_list(data, 0, len(data) - 1)
    return data


print(reverse_list([1, 2, 3, 4, 5, 6]))
print(reverse_list(["A", "B", "C", "D", "E", ]))


# TODO: Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive
#  function compare to that of an iterative version?


def fibonacci_recursion(n):  # n = term position
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)


def print_fibonacci_seq(n):  # n = number of terms
    seq = []
    for i in range(0, n):
        seq.append(fibonacci_recursion(i))
    print(seq)


print_fibonacci_seq(20)

# TODO: Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks
