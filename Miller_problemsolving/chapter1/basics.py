import math

# NUMERIC DATA TYPES
# mainly two primitive data types for numeric data: integers and floats
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
print(2 ** 10)  # 1024
print(6 / 3)  # 2.0
print(7 / 3)  # 2.33333333333
print(7 // 3)  # 2
print(7 % 3)  # 1
print(3 / 6)  # 0.5
print(3 // 6)  # 0
print(3 % 6)  # 3
print(2 ** 100)  # 1267650600228229401496703205376

# BOOLEAN DATA TYPE

print(False or True)
print(not (False or True))
print(True and True)

# combine logical and relational operators to form complex logical equations.

print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

# Build-in Collection Data Types : LISTS

my_list = [1, 3, True, 6.5]

# repetition operator: the result is a repetition of references to the data objects in the sequence.
init_list = [0] * 12

# Example:
origin_list = [1, 2, 3, 4]
A = origin_list * 3
print(A)
origin_list[2] = 45
print(A)

# The variable A holds a collection of three references to the original list called my_list. Note
# that a change to one element of my_list shows up in all three occurrences in A

# range produces a range object that represents a sequence of values. By using the
# list function, it is possible to see the value of the range object as a list

print(range(10))  # The range object represents a sequence of integers
print(list(range(10)))
print(range(10, 1, -1))
print(list(range(10, 1, -1)))

my_dict = {
    'casa': 'house',
    'perro': 'dog',
    'gato': 'cat'
}

print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())
print(list(my_dict.keys()))
print(list(my_dict.items()))
print(list(my_dict.values()))

# INPUT AND OUTPUT

# Python’s input function takes a single parameter that is a string. This string is often called
# the prompt because it contains some helpful text prompting the user to enter something.

user_name = input("Please enter your name ")
print("Your name in all capitals is", user_name.upper(), "and has length", len(user_name))

# If you want this string interpreted as another type, you must provide the type conversion explicitly

user_radius = input("Please enter the radius of the circle ")
radius = float(user_radius)
diameter = 2 * radius
print("circle diameter", diameter)

# STRING FORMATTING

# print takes zero or more parameters and displays them using a single blank as the default separator. It is possible to
# change the separator character by setting the sep argument

# In addition, each print ends with a newline character by default. This behavior
# can be changed by setting the end argument.

print("Hello", "World")
print("Hello", "World", sep="***")
print("Hello", "World", end="***")

# Template strings

price = 24
item = 'banana'

print("The %s costs %d cents" % (item, price))
print("The %+10s costs %5.2f cents" % (item, price))
print("The %+10s costs %10.2f cents" % (item, price))

item_dict = {"item": "banana", "cost": 24}
print("The %(item)s costs %(cost)7.1f cents" % item_dict)

# CONTROL STRUCTURES

for item in [1, 2, 3, 4, 5]:
    print(item)

# for loop assigns the variable item to be each successive value in the list [1, 3, 6, 2, 5]. The body of the
# iteration is then executed. This works for any collection that is a sequence (lists, tuples, and
# strings).

for item in range(5):
    print(item ** 2)

# The range function will return a range object
# representing the sequence 0, 1, 2, 3, 4 and each value will be assigned to the variable item.

word_list = ['cat', 'dog', 'rabbit']
letter_list = []

""""
iterates over a list of strings and for each string processes each character by appending it to a list. 
The result is a list of all the letters in all of the words
"""
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)

print(letter_list)

# if we would like to create a list of the first 10 perfect squares, we could use a for statement

sq_list = []
for x in range(1, 11):
    sq_list.append(x ** 2)
print(sq_list)

# Using a list comprehension, we can do this in one step as

sq_list2 = [x ** 2 for x in range(1, 11)]
print(sq_list2)

# The general syntax for a list comprehension also allows a selection criteria to be added so that only certain items
# get added.

sq_list_odds = [x * x for x in range(1, 11) if x % 2 != 0]
print(sq_list_odds)

# Any sequence that supports iteration can be used within a list
# comprehension to construct a new list.

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])

# EXCEPTIONS AND ERRORS

a_number = int(input("Please enter an integer "))

# We can handle this exception (if user enter a number lower than 0) by calling the print function from within a try
# block. A corresponding except block “catches” the exception and prints a message back to the user in the event that
# an exception occurs.

try:
    print(math.sqrt(a_number))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))

# instead of calling the square root function with a negative number, we could have
# checked the value first and then raised our own exception

# The code fragment below shows the result of creating a new RuntimeError exception. Note that the program would still
# terminate but now the exception that caused the termination is something explicitly created by the programmer.

b_number = int(input('Please enter an integer'))

if b_number < 0:
    raise RuntimeError("You can't use a negative integer number")
else:
    print(math.sqrt(a_number))

