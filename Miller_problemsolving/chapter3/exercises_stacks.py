# 1 Simple Balance Parentheses

# Balanced parentheses means that each opening symbol has a corresponding closing symbol and the pairs
# of parentheses are properly nested. Consider the following correctly balanced strings of
# parentheses

# (()((())())) Correct
# ((((((())  Incorrect

# The ability to differentiate between parentheses that are correctly balanced and those that are
# unbalanced is an important part of recognizing many programming language structures.

# The challenge then is to write an algorithm that will read a string of parentheses from left to
# right and decide whether the symbols are balanced. To solve this problem we need to make
# an important observation. As you process symbols from left to right, the most recent opening
# parenthesis must match the next closing symbol

#  Also, the first opening symbol processed may have to wait until the very last symbol for its match. Closing
#  symbols match opening symbols in the reverse order of their appearance; they match from the inside out. This
# is a clue that stacks can be used to solve the problem.

# Starting with an empty stack, process the
# parenthesis strings from left to right. If a symbol is an opening parenthesis, push it on the
# stack as a signal that a corresponding closing symbol needs to appear later. If, on the other
# hand, a symbol is a closing parenthesis, pop the stack. As long as it is possible to pop the
# stack to match every closing symbol, the parentheses remain balanced. If at any time there is
# no opening symbol on the stack to match a closing symbol, the string is not balanced
# At the end of the string, when all symbols have been processed, the stack should be empty.

from Miller_problemsolving.chapter3.Stacks import Stack


# using a for loop
def parent_checker(text):
    parent_stack = Stack()
    pass_check = True
    for char in text:
        if char == '(':
            parent_stack.push(char)
        elif char == ')':
            if parent_stack.is_empty():
                pass_check = False
                break
            else:
                parent_stack.pop()
        else:
            continue

    if not parent_stack.is_empty():
        pass_check = False

    return pass_check


print('first check:', parent_checker('(231(fak)(43((xmc))(zckm))89u)'))
print('second check:', parent_checker('((((((())'))
print('third check:', parent_checker('((()))))(())'))


# using a while loop
def parent_checker_v2(text):
    parent_stack = Stack()
    pass_check = True
    index = 0
    while index < len(text) and pass_check is True:
        if text[index] == '(':
            parent_stack.push(1)
        elif text[index] == ')':
            if parent_stack.is_empty():
                pass_check = False
            else:
                parent_stack.pop()
        index += 1

    if not parent_stack.is_empty():
        pass_check = False

    return pass_check


print('first check:', parent_checker_v2('(231(fak)(43((xmc))(zckm))89u)'))
print('second check:', parent_checker_v2('((((((())'))
print('third check:', parent_checker_v2('((()))))(())'))

# 2. Balanced Symbols (A General Case)

#  problem shown above is a specific case of a more general situation
# that arises in many programming languages. The general problem of balancing and nesting
# different kinds of opening and closing symbols occurs frequently
# It is possible to mix symbols as long as each maintains its own open and close relationship. Strings of symbols
# such as
# { { ( [ ] [ ] ) } ( ) }
# are properly balanced in that not only does each opening symbol have a corresponding closing
# symbol, but the types of symbols match as well

# Recall that each opening symbol is simply pushed on the stack to
# wait for the matching closing symbol to appear later in the sequence. When a closing symbol
# does appear, the only difference is that we must check to be sure that it correctly matches the
# type of the opening symbol on top of the stack. If the two symbols do not match, the string is
# not balanced. Once again, if the entire string is processed and nothing is left on the stack, the
# string is correctly balanced.


par_types = {
    '(': 0,
    ')': 0,
    '[': 1,
    ']': 1,
    '{': 2,
    '}': 2,
    '<': 3,
    '>': 3,
}


def balanced_checker(text):
    parent_stack = Stack()
    index = 0
    while index < len(text):
        if text[index] in '{[(<¡':
            parent_stack.push(par_types[text[index]])
        elif text[index] in '}])>!':
            if parent_stack.is_empty():
                return False
            elif parent_stack.peek() != par_types[text[index]]:
                return False
            else:
                parent_stack.pop()
        index += 1

    return parent_stack.is_empty()


print('balanced checker 1:', balanced_checker('{b{23([ada][ajkd])}(131)anc}'))
print("balanced checker 2:", balanced_checker('[{()]'))
print("balanced checker 3:", balanced_checker('[{{([)]'))


def matches(char1, char2):
    opens = "([{"
    closes = ")]}"
    return opens.index(char1) == closes.index(char2)


def balanced_checker_v2(text):
    parent_stack = Stack()
    index = 0
    # is better to use a foor each loob in this case since we don't need the index only the char values
    while index < len(text):
        if text[index] in '{[(<¡':
            parent_stack.push(text[index])
        elif text[index] in '}])>!':
            if parent_stack.is_empty():
                return False
            elif not matches(parent_stack.pop(), text[index]):
                return False
        index += 1

    return parent_stack.is_empty()


print('balanced checker V2 1:', balanced_checker_v2('{b{23([ada][ajkd])}(131)anc}'))
print("balanced checker V2 2:", balanced_checker_v2('[{()]'))
print("balanced checker V2 3:", balanced_checker_v2('[{{([)]'))


# These two examples show that stacks are very important data structures for the processing
# of language constructs in computer science. Almost any notation you can think of has some
# type of nested symbol that must be matched in a balanced order.


# 3. Converting Decimal Numbers to Binary Numbers

#  Binary representation is important in computer science since all
# values stored within a computer exist as a string of binary digits, a string of 0s and 1s. Without
# the ability to convert back and forth between common representations and binary numbers, we
# would need to interact with computers in very awkward ways

# But how can we easily convert integer values into binary numbers? The answer is an algorithm
# called “Divide by 2” that uses a stack to keep track of the digits for the binary result.

# The Divide by 2 algorithm assumes that we start with an integer greater than 0. A simple
# iteration then continually divides the decimal number by 2 and keeps track of the remainder.
# We think about building our binary number as a sequence of digits; the first remainder we compute
# will actually be the last digit in the sequence

def decimal_to_binary(number: int):
    stack = Stack()
    count = 0
    while number > 0:
        stack.push(number % 2)
        number = number // 2
        count += 1

    return ''.join(str(stack.pop()) for k in range(count))


print(decimal_to_binary(233))
print(decimal_to_binary(42))


# In computer science it is common to use a number of different encodings. The most
# common of these are binary, octal (base 8), and hexadecimal (base 16).
# The “Divide by 2” idea is simply replaced with a more
# general “Divide by base.”

def decimal_to_base(number: int, base: int = 2):
    digits = "0123456789ABCDEF"
    stack = Stack()
    count = 0
    while number > 0:
        stack.push(number % base)
        number = number // base
        count += 1

    return ''.join(digits[stack.pop()] for k in range(count))


print(decimal_to_base(233, 8))
print(decimal_to_base(233, 9))
print(decimal_to_base(233, 16))
print(decimal_to_base(333, 16))

# Base 2 through base 10 numbers need a maximum of 10 digits, so the typical digit characters 0, 1, 2, 3, 4, 5, 6, 7,
# 8, and 9 work fine. The problem comes when we go beyond base 10. We can no longer
# simply use the remainders, as they are themselves represented as two-digit decimal numbers.
# Instead we need to create a set of digits that can be used to represent those remainders beyond 9.

# A solution to this problem is to extend the digit set to include some alphabet characters. For
# example, hexadecimal uses the ten decimal digits along with the first six alphabet characters
# for the 16 digits. To implement this, a digit string is created that stores the digits in their
# corresponding positions.

# When a remainder is removed from the stack, it can be used to index into the
# digit string and the correct resulting digit can be appended to the answer.
