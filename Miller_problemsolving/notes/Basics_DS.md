## 3. BASIC DATA STRUCTURES

####### What Are Linear Structures?
Stacks, queues, deques, and lists are examples of data collections whose items are ordered depending on how they are
added or removed. Once an item is added, it stays in that position relative to the other elements that came before
and came after it. Collections such as these are often referred to as **linear data structures**.

Linear structures can be thought of as having two ends. What distinguishes
one linear structure from another is the way in which items are added and removed, in particular
the location where these additions and removals occur

### 3.1 Stacks

A **stack** (sometimes called a “push-down stack”) is an ordered collection of items where the
addition of new items and the removal of existing items always takes place at the same end.
This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”

Then items stored in the stack that are closer to the base
represent those that have been in the stack the longest. The most recently added item is the
one that is in position to be removed first. This ordering principle is sometimes called **LIFO,
last-in first-out**. It provides an ordering based on length of time in the collection. Newer items
are near the top, while older items are near the base

One of the most useful ideas related to stacks comes from the simple observation of items as
they are added and then removed. Assume you start out with a clean desktop. Now place books
one at a time on top of each other. You are constructing a stack. Consider what happens when
you begin removing books. The order that they are removed is exactly the reverse of the order
that they were placed. Stacks are fundamentally important, as they can be used to reverse the
order of items. *The order of insertion is the reverse of the order of removal*.

For example, every web browser has a Back button. As you navigate
from web page to web page, those pages are placed on a stack (actually it is the URLs that are
going on the stack). The current page that you are viewing is on the top and the first page you
looked at is at the base. If you click on the Back button, you begin to move in reverse order
through the pages.

##### The Stack Abstract Data Type
A stack is structured as an ordered collection of items where items are added to and
removed from the end called the “top.” Stacks are ordered LIFO. The stack operations are given
below

• **Stack()** creates a new stack that is empty. It needs no parameters and returns an empty
stack.

• **push(item)** adds a new item to the top of the stack. It needs the item and returns
nothing.

• **pop()** removes the top item from the stack. It needs no parameters and returns the item.
The stack is modified.

• **peek()** returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

• **is_empty()** tests to see whether the stack is empty. It needs no parameters and returns
a boolean value.

• **size()** returns the number of items on the stack. It needs no parameters and returns an
integer.

##### Implementing A Stack in Python
we will turn our attention to using Python to implement the stack. Recall that when we give an abstract data type a
physical implementation we refer to the implementation as a data structure.

### 3.2 Queues

A queue is an ordered collection of items where the addition of new items happens at one end,
called the “rear,” and the removal of existing items occurs at the other end, commonly called
the “front.” As an element enters the queue it starts at the rear and makes its way toward the
front, waiting until that time when it is the next element to be removed

The most recently added item in the queue must wait at the end of the collection. The item that
has been in the collection the longest is at the front. This ordering principle is sometimes called
**FIFO, first-in first-out**. It is also known as **“first-come first-served.”**

Well-behaved lines, or queues, are very
restrictive in that they have only one way in and only one way out. There is no jumping in the
middle and no leaving before you have waited the necessary amount of time to get to the front.

operating systems use a number of different queues to control
processes within a computer. The scheduling of what gets done next is typically based on
a queuing algorithm that tries to execute programs as quickly as possible and serve as many
users as it can. Also, as we type, sometimes keystrokes get ahead of the characters that appear
on the screen. This is due to the computer doing other work at that moment. The keystrokes
are being placed in a queue-like buffer so that they can eventually be displayed on the screen
in the proper order

##### The Queue Abstract Data Type
A queue is structured as an ordered collection of items which are added at one end,
called the “rear,” and removed from the other end, called the “front.” Queues maintain a FIFO
ordering property. The queue operations are given below

• Queue() creates a new queue that is empty. It needs no parameters and returns an empty
queue.

• enqueue(item) adds a new item to the rear of the queue. It needs the item and returns
nothing.

• dequeue() removes the front item from the queue. It needs no parameters and returns the
item. The queue is modified.

• is_empty() tests to see whether the queue is empty. It needs no parameters and returns a
boolean value.

• size() returns the number of items in the queue. It needs no parameters and returns an
integer.

##### Implementing A Queue in Python


### 3.3 Deques

A deque, also known as a double-ended queue, is an ordered collection of items similar to the
queue. It has two ends, a front and a rear, and the items remain positioned in the collection.
What makes a deque different is the unrestrictive nature of adding and removing items. New
items can be added at either the front or the rear. Likewise, existing items can be removed from
either end. In a sense, this hybrid linear structure provides all the capabilities of stacks and
queues in a single data structure

It is important to note that even though the deque can assume many of the characteristics of
stacks and queues, it does not require the LIFO and FIFO orderings that are enforced by those
data structures. It is up to you to make consistent use of the addition and removal operations

##### The Deques abstract data type
A deque is structured as an ordered collection of items where items are added and
removed from either end, either front or rear. The deque operations are given below.

• Deque() creates a new deque that is empty. It needs no parameters and returns an empty
deque.

• add_front(item) adds a new item to the front of the deque. It needs the item and returns
nothing

• add_rear(item) adds a new item to the rear of the deque. It needs the item and returns
nothing.

• remove_front() removes the front item from the deque. It needs no parameters and returns
the item. The deque is modified.

• remove_rear() removes the rear item from the deque. It needs no parameters and returns
the item. The deque is modified.

• is_empty() tests to see whether the deque is empty. It needs no parameters and returns a
boolean value.

• size() returns the number of items in the deque. It needs no parameters and returns an
integer.

##### Implementing a Deque in Python

### 3.4 Lists

not all programming languages include a list collection. In these cases, the notion of a list must be implemented by
the programmer.

A list is a collection of items where each item holds a relative position with respect to the
others. More specifically, we will refer to this type of list as an unordered list. We can consider
the list as having a first item, a second item, a third item, and so on. We can also refer to the
beginning of the list (the first item) or the end of the list (the last item).

### The Unordered List Abstract Data Type

The structure of an unordered list is a collection of items where each item
holds a relative position with respect to the others. Some possible unordered list operations are
given below.

• List() creates a new list that is empty. It needs no parameters and returns an empty list.

• add(item) adds a new item to the list. It needs the item and returns nothing. Assume the
item is not already in the list.

• remove(item) removes the item from the list. It needs the item and modifies the list.
Assume the item is present in the list.

• search(item) searches for the item in the list. It needs the item and returns a boolean
value.

• is_empty() tests to see whether the list is empty. It needs no parameters and returns a
boolean value.

• size() returns the number of items in the list. It needs no parameters and returns an
integer.

• append(item) adds a new item to the end of the list making it the last item in the collection. It needs the
item and returns nothing. Assume the item is not already in the list.

• index(item) returns the position of item in the list. It needs the item and returns the index.
Assume the item is in the list.

• insert(pos,item) adds a new item to the list at position pos. It needs the item and returns
nothing. Assume the item is not already in the list and there are enough existing items to
have position pos.

• pop() removes and returns the last item in the list. It needs nothing and returns an item.
Assume the list has at least one item.

• pop(pos) removes and returns the item at position pos. It needs the position and returns
the item. Assume the item is in the list

##### Implementing an Unordered List: Linked Lists
we will construct what is commonly known as a **linked list**. Recall that we need to be sure that we can maintain
the relative positioning of the items. However, there is no requirement that we maintain that positioning in
contiguous memory.

It is important to note that the location of the first item of the list must be explicitly specified.
Once we know where the first item is, the first item can tell us where the second is, and so on.
The external reference is often referred to as the head of the list. Similarly, the last item needs
to know that there is no next item.

**The Node class**
The basic building block for the linked list implementation is the node. Each node object must
hold at least two pieces of information. First, the node must contain the list item itself. We will
call this the data field of the node. In addition, each node must hold a reference to the next
node. To construct a node, you need to supply the initial data value for the node

The Node class also includes the usual methods to access and modify the data and the next reference.

#### The Ordered List Abstract Data Type

The structure of an ordered list is a collection of items where each item holds a relative position
that is based upon some underlying characteristic of the item. The ordering is typically either
ascending or descending and we assume that list items have a meaningful comparison operation that is
already defined. Many of the ordered list operations are the same as those of the
unordered list.

• OrderedList() creates a new ordered list that is empty. It needs no parameters and returns
an empty list.

• add(item) adds a new item to the list making sure that the order is preserved. It needs the
item and returns nothing. Assume the item is not already in the list.

• remove(item) removes the item from the list. It needs the item and modifies the list.
Assume the item is present in the list.

• search(item) searches for the item in the list. It needs the item and returns a boolean
value.

• is_empty() tests to see whether the list is empty. It needs no parameters and returns a
boolean value.

• size() returns the number of items in the list. It needs no parameters and returns an
integer.

• index(item) returns the position of item in the list. It needs the item and returns the index.
Assume the item is in the list.

• pop() removes and returns the last item in the list. It needs nothing and returns an item.
Assume the list has at least one item.

• pop(pos) removes and returns the item at position pos. It needs the position and returns
the item. Assume the item is in the list

##### Implementing an Ordered List

we must remember that the relative positions of the items are based on some underlying characteristic.
Again, the node and link structure is ideal for representing the relative positioning of the items.

we should note that the is_empty and size methods can be implemented the same as with unordered lists since
they deal only with the number of nodes in the list without regard to the actual item values. Likewise, the remove
method will work just fine since we still need to find the item and then link around the node to
remove it. The two remaining methods, search and add, will require some modification.

The search of an unordered linked list required that we traverse the nodes one at a time until
we either find the item we are looking for or run out of nodes (None). It turns out that the same
approach would actually work with the ordered list and in fact in the case where we find the
item it is exactly what we need. However, in the case where the item is not in the list, we can
take advantage of the ordering to stop the search as soon as possible.

Once the value in the node becomes greater than the item we are searching for, the search can stop and return False.
There is no way the item could exist further out in the linked list.

The most significant method modification will take place in add. Recall that for unordered lists,
the add method could simply place a new node at the head of the list. It was the easiest point
of access. Unfortunately, this will no longer work with ordered lists. It is now necessary that
we discover the specific place where a new item belongs in the existing ordered list

##### Analysis of Linked Lists
To analyze the complexity of the linked list operations, we need to consider whether they
require traversal

You may also have noticed that the performance of this implementation differs from the actual
performance given earlier for Python lists. This suggests that linked lists are not the way Python
lists are implemented. The actual implementation of a Python list is based on the notion of an
array
