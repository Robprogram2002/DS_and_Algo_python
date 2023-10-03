import random
# 1 Simulation: Hot Potato

# In this game (see Figure 3.13) children line up in a circle and pass an item from
# neighbour to neighbour as fast as they can. At a certain point in the game, the action is stopped
# and the child who has the item (the potato) is removed from the circle  Play continues until
# only one child is left.

# To simulate the circle, we will use a queue. Assume that the child holding
# the potato will be at the front of the queue. Upon passing the potato, the simulation will simply
# dequeue and then immediately enqueue that child, putting her at the end of the line. She will
# then wait until all the others have been at the front before it will be her turn again. After num
# dequeue/enqueue operations, the child at the front will be removed permanently and another
# cycle will begin. This process will continue until only one name remains (the size of the queue
# is 1)

from Miller_problemsolving.chapter3.Queue import Queue


def potato_game(people):
    people_queue = Queue()
    for name in people:
        people_queue.enqueue(name)
    while people_queue.size() > 1:

        for i in range(0, random.randint(1, 30)):
            people_queue.enqueue(people_queue.dequeue())

        print("{} has been eliminated".format(people_queue.dequeue()))

    print("{} is the winner".format(people_queue.dequeue()))


potato_game(["Bill", "David", "Susan", "Jane", "Kent",
             "Brad"])

# Note that in this example the value of the counting constant is greater than the number of names
# in the list. This is not a problem since the queue acts like a circle and counting continues back at
# the beginning until the value is reached. Also, notice that the list is loaded into the queue such
# that the first name on the list will be at the front of the queue. Bill in this case is the first item
# in the list and therefore moves to the front of the queue
