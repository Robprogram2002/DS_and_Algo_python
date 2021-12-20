# The implementation shown below assumes that the rear is at position 0 in the list. This allows us to
# use the insert function on lists to add new elements to the rear of the queue. The pop operation
# can be used to remove the front element (the last element of the list). Recall that this also
# means that enqueue will be 𝑂(𝑛) and dequeue will be 𝑂(1)

class Queue:
    def __init__(self, new_list=None):
        if new_list == [] or new_list is None:
            self.items = []
        else:
            self.items = new_list

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, new_item):
        self.items.insert(0, new_item)

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[len(self.items) - 1]


q = Queue()
print(q.is_empty())
print(q.enqueue(4))
print(q.enqueue('dog'))
print(q.enqueue(True))
print(q.size())
print(q.is_empty())
q.enqueue(8.4)
print(q.dequeue())
print(q.dequeue())
print(q.size())



# TODO: Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

# TODO:  it is possible to implement a queue such that both enqueue and dequeue have 𝑂(1) performance on average.
# In this case it means that most of the time enqueue and dequeue
# will be 𝑂(1) except in one particular circumstance where dequeue will be 𝑂(𝑛).

# TODO: Consider a real life situation. Formulate a question and then design a simulation that can help to answer it.
# Possible situations include:
#     • Cars lined up at a car wash
#     • Customers at a grocery store check-out
#     • Airplanes taking off and landing on a runway
#     • A bank teller

