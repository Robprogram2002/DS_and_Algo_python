import random

from Stack import ArrayStack
from Queue import ArrayQueue, CircularQueue


# Implement a function with signature transfer(S, T) that transfers all elements from
# stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T

def transfer(S: ArrayStack, T: ArrayStack):
    while not S.is_empty():
        T.push(S.pop())


stack_1 = ArrayStack()
stack_1.push(2)
stack_1.push(4)
stack_1.push(6)
stack_1.push(8)
stack_2 = ArrayStack()

print(stack_1)
print(stack_2)
transfer(stack_1, stack_2)
print(stack_2)
print(stack_1)


# Give a recursive method for removing all the elements from a stack.

def remove_all(S: ArrayStack):
    if not S.is_empty():
        S.pop()
        remove_all(S)


remove_all(stack_2)
print(stack_2)


# Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order

def reverse(data: []):
    temp = ArrayStack()
    for i in range(len(data)):
        temp.push(data[i])
    for k in range(len(data)):
        data[k] = temp.pop()


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(my_list)
print(my_list)


# Describe a nonrecursive algorithm for enumerating all permutations of the
# numbers {1,2,...,n} using an explicit stack


# Show how to use a stack S and a queue Q to generate all possible subsets
# of an n-element set T nonrecursively


# Suppose you have a stack S containing n elements and a queue Q that is
# initially empty. Describe how you can use Q to scan S to see if it contains a
# certain element x, with the additional constraint that your algorithm must
# return the elements back to S in their original order. You may only use S,
# Q, and a constant number of other variables.

def find_in_stack(S: ArrayStack, Q: ArrayQueue, e):
    print('next')


# Implement a hot potato game using a queue

def potato_game(people):
    people_queue = ArrayQueue()
    # people_queue = CircularQueue()
    for name in people:
        people_queue.enqueue(name)
    while len(people_queue) > 1:

        for i in range(0, random.randint(1, 30)):
            people_queue.rotate()

        print("{} has been eliminated".format(people_queue.dequeue()))

    print("{} is the winner".format(people_queue.dequeue()))


potato_game(["Bill", "David", "Susan", "Jane", "Kent", "Brad"])
