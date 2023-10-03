from Miller_problemsolving.chapter3.Deque import Deque


# 1. Palindrome Checker

# A palindrome is a string that reads the same forward and backward, for
# example, radar, toot, and madam. We would like to construct an algorithm to input a string of
# characters and check whether it is a palindrome.

# We will process the string from left to right and add each character to the rear of the deque. At this
# point, the deque will be acting very much like an ordinary queue. However, we can now make
# use of the dual functionality of the deque. The front of the deque will hold the first character of
# the string and the rear of the deque will hold the last character

# Since we can remove both of them directly, we can compare them and continue only if they
# match. If we can keep matching first and the last items, we will eventually either run out of
# characters or be left with a deque of size 1 depending on whether the length of the original
# string was even or odd. In either case, the string must be a palindrome.

def palindrome_checker(word):
    deque = Deque()
    for char in word:
        deque.add_rear(char)

    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False

    return True


print(palindrome_checker('radar'))
print(palindrome_checker('toot'))
print(palindrome_checker('madam'))

print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker('sandwich'))
print(palindrome_checker('pencil'))
print(palindrome_checker('dog&god'))
