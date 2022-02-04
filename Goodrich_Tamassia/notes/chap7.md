## Linked Lists

Python’s list class is highly optimized, and often a great choice for storage. With that said, there are some notable
disadvantages:

1. The length of a dynamic array might be longer than the actual number of elements that it stores.
2. Amortized bounds for operations may be unacceptable in real-time systems.
3. Insertions and deletions at interior positions of an array are expensive.

In this chapter, we introduce a data structure known as a **linked list**, which provides an alternative to an
array-based sequence (such as a Python list). Both array-based sequences and linked lists keep elements in a certain
order, but using a very different style. An array provides the more centralized representation, with one large chunk of
memory capable of accommodating references to many elements. A linked list, in contrast, relies on a more distributed
representation in which a lightweight object, known as a **node**, is allocated for each element. Each node maintains a
reference to its element and one or more references to neighboring nodes in order to collectively represent the linear
order of the sequence.

We will demonstrate a trade-off of advantages and disadvantages when contrasting array-based sequences and linked lists.
Elements of a linked list cannot be efficiently accessed by a numeric index k, and we cannot tell just by examining a
node if it is the second, fifth, or twentieth node in the list. However, linked lists avoid the three disadvantages
noted above for array-based sequences.

### Singly Linked Lists

A singly linked list, in its simplest form, is a *collection of nodes* that collectively form a *linear sequence*. Each
node stores a reference to an object that is an element of the sequence, as well as a *reference* to the next node of
the list

The first and last node of a linked list are known as the **head** and **tail** of the list, respectively. By starting
at the head, and moving from one node to another by following each node’s next reference, we can reach the tail of the
list. We can identify the tail as the node having None as its next reference. This process is commonly known as **
traversing** the linked list. Because the next reference of a node can be viewed as a link or pointer to another node,
the process of traversing a list is also known as **link hopping** or **pointer hopping**.

Minimally, the linked list instance must keep a reference to the head of the list. Without an explicit reference to the
head, there would be no way to locate that node (or indirectly, any others). There is not an absolute need to store a
direct reference to the tail of the list, as it could otherwise be located by starting at the head and traversing the
rest of the list. However, storing an explicit reference to the tail node is a common convenience to avoid such a
traversal. In similar regard, it is common for the linked list instance to keep a count of the total number of nodes
that comprise the list (commonly described as the size of the list), to avoid the need to traverse the list to count the
nodes

An important property of a linked list is that it does not have a predetermined fixed size; it uses space proportionally
to its current number of elements

**Inserting an element at the Head.** The main idea is that we create a new node, set its element to the new element,
set its next link to refer to the current head, and then set the list’s head to point to the new node

If the list were initially empty (i.e., L.head is None), then a natural consequence is that the new node has its next
reference set to None.

**Inserting an Element at the Tail.** In this case, we create a new node, assign its next reference to None, set the
next reference of the tail to point to this new node, and then update the tail reference itself to this new node. (but
we must check if the list is not empty)

**Removing an Element.** Removing an element from the head of a singly linked list is essentially the reverse operation
of inserting a new element at the head.

Unfortunately, we cannot easily delete the last node of a singly linked list. Even if we maintain a tail reference
directly to the last node of the list, we must be able to access the node before the last node in order to remove the
last node. But we cannot reach the node before the tail by following next links from the tail. The only way to access
this node is to start from the head of the list and search all the way through the list. But such a sequence of
link-hopping operations could take a long time

##### Implementing a Stack with a Singly Linked List

In designing such an implementation, we need to decide whether to model the top of the stack at the head or at the tail
of the list. There is clearly a best choice here; we can efficiently insert and delete elements in constant time only at
the head. Since all stack operations affect the top, we orient the top of the stack at the head of our list.

To represent individual nodes of the list, we develop a lightweight Node class. This class will never be directly
exposed to the user of our stack class, so we will formally define it as a nonpublic, nested class of our eventual
LinkedStack class

##### Implementing a Queue with a Singly Linked List

Because we need to perform operations on both ends of the queue, we will explicitly maintain both a head reference and a
tail reference as instance variables for each queue. The natural orientation for a queue is to align the front of the
queue with the head of the list, and the back of the queue with the tail of the list, because we must be able to enqueue
elements at the back, and dequeue them from the front. (Recall we are unable to efficiently remove elements from the
tail of a singly linked list.)

In general, an operation at the head has no effect on the tail, but when dequeue is invoked on a queue with one element,
we are simultaneously removing the tail of the list. We therefore set self. tail to None for consistency.

There is a similar complication in our implementation of enqueue. The newest node always becomes the new tail. Yet a
distinction is made depending on whether that new node is the only node in the list. In that case, it also becomes the
new head; otherwise the new node must be linked immediately after the existing tail node.

In terms of performance, the LinkedQueue is similar to the LinkedStack in that all operations run in worst-case constant
time, and the space usage is linear in the current number of elements.

### Circularly Linked Lists

the notion of a circular array was artificial, in that there was nothing about the representation of the array itself
that was circular in structure. It was our use of modular arithmetic when “advancing” an index from the last slot to the
first slot that provided such an abstraction.

In the case of linked lists, there is a more tangible notion of a circularly linked list, as we can have the tail of the
list use its next reference to point back to the head of the list. We call such a structure a **circularly linked list**
.

A circularly linked list provides a more general model than a standard linked list for data sets that are **cyclic**,
that is, which do not have any particular notion of a beginning and end

Even though a circularly linked list has no beginning or end, per se, we must maintain a reference to a particular node
in order to make use of the list. We use the identifier **current** to describe such a designated node. By
setting `current = current.next`, we can effectively advance through the nodes of the list.

To motivate the use of a circularly linked list, we consider a **round-robin scheduler**, which iterates through a
collection of elements in a circular fashion and “services” each element by performing a given action on it. Such a
scheduler is used, for example, to fairly allocate a resource that must be shared by a collection of clients.

A round-robin scheduler could be implemented with the general queue ADT, by repeatedly performing the following steps on
queue Q

        1. e = Q.dequeue()
        2. Service element e
        3. Q.enqueue(e)

But there is unnecessary effort in the combination of a dequeue operation followed soon after by an enqueue of the same
element.

If using a circularly linked list, the effective transfer of an item from the “head” of the list to the “tail” of the
list can be accomplished by advancing a reference that marks the boundary of the queue. We will next provide an
implementation of a `CircularQueue` class that supports the entire queue ADT, together with an additional method,
`rotate( )`, that moves the first element of the queue to the back. (A similar method is supported by the `deque` class
of Python’s collections module)

With this operation, a round-robin schedule can more efficiently be implemented by repeatedly performing the following
steps:

       1. Service element Q.front()
       2. Q.rotate()

** Implementing a Queue with a Circularly Linked List.** we rely on the intuition in which the queue has a head and a
tail, but with the next reference of the tail linked to the head. Given such a model, there is no need for us to
explicitly store references to both the head and the tail; as long as we keep a reference to the tail, we can always
find the head by following the tail’s next reference

The only two instance variables are tail, which is a reference to the tail node (or None when empty), and size, which is
the current number of elements in the queue. When an operation involves the front of the queue, we
recognize `self._tail._next` as the head of the queue. When enqueue is called, a new node is placed just after the tail
but before the current head, and then the new node becomes the head (`tail._next`).

### Doubly Linked Lists

we are unable to efficiently delete a node at the tail of the list. More generally, we cannot efficiently delete an
arbitrary node from an interior position of the list if only given a reference to that node, because we cannot determine
the node that immediately precedes the node to be deleted (yet, that node needs to have its next reference updated).

To provide greater symmetry, we define a linked list in which each node keeps an explicit reference to the node before
it and a reference to the node after it. Such a structure is known as a **doubly linked list**. These lists allow a
greater variety of O(1)-time update operations. We continue to use the term “next” for the reference to the node that
follows another, and we introduce the term “prev” for the reference to the node that precedes it

##### Header and Trailer Sentinels

In order to avoid some special cases when operating near the boundaries of a doubly linked list, it helps to add *
special nodes* at both ends of the list: a **header** node at the beginning of the list, and a **trailer** node at the
end of the list. These “dummy” nodes are known as **sentinels** (or **guards**), and they do not store elements of the
primary sequence.

When using sentinel nodes, an empty list is initialized so that the next field of the header points to the trailer, and
the prev field of the trailer points to the header; the remaining fields of the sentinels are irrelevant (presumably
None, in Python).

For a nonempty list, the header’s `next` will refer to a node containing the first real element of a sequence, just as
the trailer’s `prev` references the node containing the last element of a sequence.

Although we could implement a doubly linked list without sentinel nodes; the slight extra space devoted to the sentinels
greatly simplifies the logic of our operations. Most notably, the header and trailer nodes never change—only the nodes
between them change. Furthermore, we can treat all insertions in a unified manner, because a new node will always be
placed between a pair of existing nodes. In similar fashion, every element that is to be deleted is guaranteed to be
stored in a node that has neighbors on each side (this avoids check for cases when the list is empty).

**Basic Implementation of a Doubly Linked List**

##### Implementing a Deque with a Doubly Linked List

With an implementation based upon a doubly linked list, we can achieve all deque operation in worst-case O(1) time.

With the use of sentinels, the key to our implementation is to remember that the header does not store the first element
of the deque—it is the node just after the header that stores the first element (assuming the deque is nonempty).
Similarly, the node just before the trailer stores the last element of the deque.

We use the inherited `insert_between` method to insert at either end of the deque. To insert an element at the front of
the deque, we place it immediately between the header and the node just after the header. An insertion at the end of
deque is placed immediately before the trailer node. Note that these operations succeed, even when the deque is empty;
in such a situation, the new node is placed between the two sentinels.

When deleting an element from a nonempty deque, we rely upon the inherited delete_node method, knowing that the
designated node is assured to have neighbors on each side.

### The Positional List ADT

We wish to have a more general abstraction.

What if a waiting customer decides to hang up before reaching the front of the customer service queue? Or what if
someone who is waiting in line to buy tickets allows a friend to “cut” into line at that position? We would like to
design an abstract data type that provides a user a way to refer to elements *anywhere in a sequence*, and to perform
*arbitrary insertions and deletions*.

When working with array-based sequences, integer indices provide an excellent means for describing the location of an
element, or the location at which an insertion or deletion should take place.

For linked lists, we prefer an abstraction in which there is some other means for describing a position.

One of the great benefits of a linked list structure is that it is possible to perform O(1)-time insertions and
deletions at arbitrary positions of the list, as long as we are given a reference to a relevant node of the list. It is
therefore very tempting to develop an ADT in which a node reference serves as the mechanism for describing a position.
In fact, our `_DoublyLinkedBase` class has methods `insert_between` and `delete_node` that accept node references as
parameters.

However, such direct use of nodes would violate the object-oriented design principles of abstraction and encapsulation.

For these reasons, instead of relying directly on nodes, we introduce an independent **position abstraction** to denote
the location of an element within a list, and then a complete **positional list ADT** that can encapsulate a doubly
linked list  (or even an array-based sequence)

A position acts as a marker or token within the broader positional list. A position p is unaffected by changes elsewhere
in a list; the only way in which a position becomes invalid is if an explicit command is issued to delete it. A position
instance is a simple object, supporting only the following method:

    p.element( ): Return the element stored at position p

In the context of the positional list ADT, positions serve as parameters to some methods and as return values from other
methods. In describing the behaviors of a positional list, we being by presenting the accessor methods supported by a
list L:

- **L.first( ):** Return the position of the first element of L, or None if L is empty.
- **L.last( ):** Return the position of the last element of L, or None if L is empty.
- **L.before(p):** Return the position of L immediately before position p, or None if p is the first position.
- **L.after(p):** Return the position of L immediately after position p, or None if p is the last position.
- **L.is_empty( ):** Return True if list L does not contain any elements.
- **len(L):** Return the number of elements in the list.
- **iter(L):** Return a forward iterator for the elements of the list.

The positional list ADT also includes the following update methods:

- **L.add_first(e):** Insert a new element e at the front of L, returning the position of the new element.
- **L.add_last(e):** Insert a new element e at the back of L, returning the position of the new element.
- **L.add_before(p, e):** Insert a new element e just before position p in L, returning the position of the new element.
- **L.add_after(p, e):** Insert a new element e just after position p in L, returning the position of the new element.
- **L.replace(p, e):** Replace the element at position p with element e, returning the element formerly at position p.
- **L.delete(p):** Remove and return the element at position p in L, invalidating the position.

For those methods of the ADT that accept a position p as a parameter, an error occurs if p is not a valid position for
list L.

Note well that the first( ) and last( ) methods of the positional list ADT return the *associated positions*, not the
elements. The advantage of receiving a position as a return value is that we can use that position to navigate the list.
For example, the following code fragment prints all elements of a positional list named data.

    cursor = data.first( )
    while cursor is not None:
        print(cursor.element( ))        # print the element stored at the position
        cursor = data.after(cursor)     # advance to the next position (if any)

This code relies on the stated convention that the None object is returned when after is called upon the last position.
That return value is clearly distinguishable from any legitimate position. The positional list ADT similarly indicates
that the None value is returned when the before method is invoked at the front of the list, or when first or last
methods are called upon an empty list. Therefore, the above code fragment works correctly even if the data list is empty

Because the ADT includes support for Python’s iter function, users may rely on the traditional for-loop syntax for such
a forward traversal of a list named data.

    for e in data:
        print(e)

#### Doubly Linked List Implementation

we present a complete implementation of a PositionalList class using a doubly linked list that satisfies the following
important proposition.

**Proposition:** Each method of the positional list ADT runs in worst-case `O(1)` time when implemented with a doubly
linked list.

`Position` instances will be used to represent the locations of elements within the list. Our various `PositionalList`
methods may end up creating redundant `Position` instances that reference the same underlying node (for example, when
first and last are the same). For that reason, our `Position` class defines the `__eq__` and `__ne__` special methods so
that a test such as `p == q` evaluates to True when two positions refer to the same node.

Each time a method of the `PositionalList` class accepts a position as a parameter, we want to verify that the position
is valid, and if so, to determine the underlying node associated with the position. This functionality is implemented by
a non-public method named `_validate`. Internally, a position maintains a reference to the associated node of the linked
list, and also a reference to the list instance that contains the specified node. With the container reference, we can
robustly detect when a caller sends a position instance that does not belong to the indicated list. We are also able to
detect a position instance that belongs to the list, but that refers to a node that is no longer part of that list.
Recall that the `delete_node` of the base class sets the previous and next references of a deleted node to None; we can
recognize that condition to detect a deprecated node

### Case Study: Maintaining Access Frequencies

we consider maintaining a collection of elements while keeping track of the number of times each element is accessed.
Keeping such access counts allows us to know which elements are among the most popular.

We model this with a new favorites list ADT that supports the len and is empty methods as well as the following:

- **access(e):** Access the element e, incrementing its access count, and adding it to the favorites list if it is not
  already present.
- **remove(e):** Remove element e from the favorites list, if present.
- **top(k):** Return an iteration of the k most accessed elements

Our first approach for managing a list of favorites is to store elements in a linked list, keeping them in nonincreasing
order of access counts. We access or remove an element by searching the list from the most frequently accessed to the
least frequently accessed. Reporting the top k most accessed elements is easy, as they are the first k entries of the
list.

To maintain the invariant that elements are stored in nonincreasing order of access counts, we must consider how a
single access operation may affect the order. The accessed element’s count increases by one, and so it may become larger
than one or more of its preceding neighbors in the list, thereby violating the invariant.

We can perform a backward traversal of the list, starting at the position of the element whose access count has
increased, until we locate a valid position after which the element can be relocated

We wish to implement a favorites list by making use of a PositionalList for storage. We use a general object-oriented
design pattern, the **composition pattern**, in which we define a single object that is composed of two or more other
objects. Specifically, we define a nonpublic nested class, `_Item`, that stores the element and its access count as a
single instance. We then maintain our favorites list as a `PositionalList` of *item* instances, so that the access count
for a user’s element is embedded alongside it in our representation.

#### Using a List with the Move-to-Front Heuristic

### Link-Based vs. Array-Based Sequences

The dichotomy between these approaches presents a common design decision when choosing an appropriate implementation of
a data structure. There is not a one-size-fits-all solution, as each offers distinct advantages and disadvantage

**Advantages of Array-Based Sequence.**

- *Arrays provide O(1)-time access to an element based on an integer index.* In contrast, locating the kth element in a
  linked list requires O(k) time to traverse the list from the beginning, or possibly O(n− k) time, if traversing
  backward from the end of a doubly linked list.
- *Operations with equivalent asymptotic bounds typically run a constant factor more efficiently with an array-based
  structure versus a linked structure.* As an example, consider the typical enqueue operation for a queue. Ignoring the
  issue of resizing an array, this operation for the ArrayQueue class involves an arithmetic calculation of the new
  index, an increment of an integer, and storing a reference to the element in the array. In contrast, the process for a
  LinkedQueue requires the instantiation of a node, appropriate linking of nodes, and an increment of an integer. While
  this operation completes in O(1) time in either model, the actual number of CPU operations will be more in the linked
  version, especially given the instantiation of the new node.
- *Array-based representations typically use proportionally less memory than linked structures*. This advantage may seem
  counterintuitive, especially given that the length of a dynamic array may be longer than the number of elements that
  it stores. Both array-based lists and linked lists are referential structures, so the primary memory for storing the
  actual objects that are elements is the same for either structure. What differs is the auxiliary amounts of memory
  that are used by the two structures. For an array-based container of n elements, a typical worst case may be that a
  recently resized dynamic array has allocated memory for 2n object references. With linked lists, memory must be
  devoted not only to store a reference to each contained object, but also explicit references that link the nodes. So a
  singly linked list of length n already requires 2n references (an element reference and next reference for each node).
  With a doubly linked list, there are 3n references.

**Advantages of Link-Based Sequences.**

- *Link-based structures provide worst-case time bounds for their operations*. This is in contrast to the amortized
  bounds associated with the expansion or contraction of a dynamic array

When many individual operations are part of a larger computation, and we only care about the total time of that
computation, an amortized bound is as good as a worst-case bound precisely because it gives a guarantee on the sum of
the time spent on the individual operations. However, if data structure operations are used in a real-time system that
is designed to provide more immediate responses, a long delay caused by a single (amortized) operation may have an
adverse effect.

- *Link-based structures support O(1)-time insertions and deletions at arbitrary positions.* This is perhaps the most
  significant advantage of the linked list. This is in stark contrast to an array-based sequence which more general
  insertions and deletions are expensive.

