import random


# Write a short Python function, that takes two integer values and returns True if n is a multiple of m and False 
# otherwise

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


print(is_multiple(8, 2))
print(is_multiple(21, 7))
print(is_multiple(21, 2))


#  Write a short Python function that takes a sequence of one or more numbers, and returns the smallest and largest
#  numbers, in the form of a tuple of length two

def minmax(data: []):
    min_val = data[0]
    max_val = data[0]
    for element in data:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element

    return min_val, max_val


print(minmax([2, 7, 3, 34, -12, 34, 0, -13]))


# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive
# integers smaller than n.

def sum_sqr_lowers(n: int):
    if n < 0:
        raise ValueError('integer must be greater than zero')
    return sum(k * k for k in range(0, n))


print(sum_sqr_lowers(10))
print(sum_sqr_lowers(4))


# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def sum_sqr_lower_odds(n: int):
    if n < 0:
        raise ValueError('integer must be greater than zero')
    return sum(k * k for k in range(0, n) if k % 2 != 0)


print(sum_sqr_lower_odds(10))
print(sum_sqr_lower_odds(4))

# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

for num in range(50, 90, 10):
    print(num, end='\t')
print('')

#  What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for num in range(8, -10, -2):
    print(num, end='\t')
print('')

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256]

print([2 ** k for k in range(0, 9)])


# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, 
# with parameterization similar to the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function

def choice(data: []):
    n = len(data)
    return data[random.randrange(0, n)]


print(choice(['Hi', 'hola', 'ciao', 'salut', 'Hello']))


# Write a  function that reverses a list of n elements, so that they are listed in the opposite order than they
# were before

def reverse_list(data: []):
    return [data[-i] for i in range(1, len(data)+1)]


print('reversed list: ', reverse_list([1, 2, 3, 4, 5, 6, 7, 8]))
print('reversed list: ', reverse_list(['a', 'b', 'c', 'd', 'e', 'f', 'g']))


#  Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def is_prod_odd(data: [int]):
    if len(data) < 2 :
        return False
    i = 0
    while i != len(data) - 1:
        for j in range(i+1, len(data)):
            if 2 % data[i]*data[j] != 0:
                print((i, j))
                return True
        i += 1
    return False


print(is_prod_odd([2, 65, 26, 23, 57]))

# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


def check_distinct(data: []):
    return True if len(data) < 1 else len(data) == len(set(data))


print(check_distinct([2, 3, 4, 5, 6, 7]))
print(check_distinct([2, 3, 4, 5, 6, 2]))
print(check_distinct([0]))


# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order occurs
# with equal probability. The random module includes a more basic function randint(a, b)
# that returns a uniformly random integer from a to b (including both endpoints). Using only
# the randint function, implement your own version of the shuffle function

def shuffle(data: []):
    for i in reversed(range(1, len(data))):
        j = random.randint(0, i)
        data[i], data[j] = data[j], data[i]

examp1 = [2, 4, 6, 8, 10]
shuffle(examp1)
print('shuffle example 1: ', examp1)

# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b.


def dot_product(a: [], b: []):
    if len(a) != len(b):
        raise ValueError('the list must be of the same length')

    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


print(dot_product([2, 4, 6, 8], [1, 3, 5, 7]))


# Write a short Python function that counts the number of vowels in a given character string.

def count_vowels(sentence: str):
    count = 0
    for char in sentence.lower():
        if char in 'aeiou':
            count += 1
    return count


print(count_vowels('good morning, how are you TODAY?'))


# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed.
def remove_punctuations(s: str):
    punt = set('\',.";:')
    return ''.join((k for k in s if k not in punt))


word = "Let's try, Mike."
print(word)
print(remove_punctuations(word))


# Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v.

def norm(v: [], p=2):
    if p <= 0:
        raise ValueError('the exponent must be an integer greater than zero')
    return sum(k ** p for k in v) ** (1 / p)


print(norm([4, 3]))


# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2

def how_many_twos(n: int):
    if n < 0:
        raise ValueError('the parameter must be a positive integer')
    count = 0
    while n >= 2:
        n = n/2
        count += 1
    return count


print(how_many_twos(13))

# Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.


# Write a Python program that simulates a handheld calculator. Your program should process input from the Python
# console representing buttons that are “pushed,” and then output the contents of the screen after each
# operation is performed.


# The birthday paradox says that the probability that two people in a room will have the same birthday is more than half,
# provided n, the number of people in the room, is more than 23. This property is not really a paradox, but many people
# find it surprising. Design a Python program that can test this paradox by a series of experiments on randomly generated
# birthdays, which test this paradox for n = 5,10,15,20,... ,100.


# Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word
# appears in the list
