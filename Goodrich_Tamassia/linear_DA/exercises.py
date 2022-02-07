from Stack import ArrayStack


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
transfer(stack_1, stack_2)
print(stack_2)
print(stack_1)


# Give a recursive method for removing all the elements from a stack.

def remove_all(S: ArrayStack):
    if S.is_empty():
        return
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

# C-6.19

# Describe a nonrecursive algorithm for enumerating all permutations of the
# numbers {1,2,...,n} using an explicit stack


# Show how to use a stack S and a queue Q to generate all possible subsets
# of an n-element set T nonrecursively


# Suppose you have a stack S containing n elements and a queue Q that is
# initially empty. Describe how you can use Q to scan S to see if it contains a
# certain element x, with the additional constraint that your algorithm must
# return the elements back to S in their original order. You may only use S,
# Q, and a constant number of other variables.


#  Modify the ArrayQueue implementation so that the queue’s capacity is
# limited to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If enqueue is called when the queue
# is at full capacity, throw a Full exception (defined similarly to Empty).


# In certain applications of the queue ADT, it is common to repeatedly
# dequeue an element, process it in some way, and then immediately enqueue
# the same element. Modify the ArrayQueue implementation to include a rotate( )
# method that has semantics identical to the combination, Q.enqueue(Q.dequeue( )).
# However, your implementation should
# be more efficient than making two separate calls (for example, because
# there is no need to modify size).


# Give a complete ArrayDeque implementation of the double-ended queue
# ADT


# Give an array-based implementation of a double-ended queue supporting
# all of the public behaviors shown in Table 6.4 for the collections.deque
# class, including use of the maxlen optional parameter. When a length limited
# deque is full, provide semantics similar to the collections.deque
# class, whereby a call to insert an element on one end of a deque causes an
# element to be lost from the opposite side
