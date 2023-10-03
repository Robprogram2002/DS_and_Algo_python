# Priority Queues

In practice, there are many applications in which a queue-like structure is used to manage objects that must be
processed in some way, but for which the first-in, first-out policy does not suffice. Consider, for example, an
air-traffic control center that has to decide which flight to clear for landing from among many approaching the airport.
This choice may be influenced by factors such as each plane’s distance from the runway, time spent waiting in a holding
pattern, or amount of remaining fuel. It is unlikely that the landing decisions are based purely on a FIFO policy.

There are other situations in which a “first come, first serve” policy might seem reasonable, yet for which other
priorities come into play Because of the possibility of cancellations, the airline maintains a queue of standby
passengers hoping to get a seat. Although the priority of a standby passenger is influenced by the check-in time of that
passenger, other considerations include the fare paid and frequent-flyer status. So it may be that an available seat is
given to a passenger who has arrived later than another, if such a passenger is assigned a better priority by the
airline agent.

*A **priority queue** is a collection of prioritized elements that allows arbitrary element insertion, and allows the
removal of the element that has first priority*. When an element is added to a priority queue, the user designates its
priority by providing an associated **key**. The element with the minimum key will be the next to be removed from the
queue (thus, an element with key 1 will be given priority over an element with key 2).

any Python object may be used as a key, as long as the object type supports a consistent meaning for the test a < b.
With such generality, applications may develop their own notion of priority for each element.

## The Priority Queue ADT

Formally, we model an element and its priority as a key-value pair. We define the priority queue ADT to support the
following methods for a priority queue P:

* P.add(k, v): Insert an item with key k and value v into priority queue P.
* P.min(): Return a tuple, (k,v), representing the key and value of an item in priority queue P with minimum key
  (but do not remove the item); an error occurs if the priority queue is empty.
* P.remove min(): Remove an item with minimum key from priority queue P, and return a tuple, (k,v), representing the key
  and value of the removed item; an error occurs if the priority queue is empty.
* P.is empty(): Return True if priority queue P does not contain any items.
* len(P): Return the number of items in priority queue P.

A priority queue may have multiple entries with equivalent keys, in which case methods min and remove min may report an
arbitrary choice of item having minimum key. Values may be any type of object. In our initial model for a priority
queue, we assume that an element’s key remains fixed once it has been added to a priority queue.

## Implementing a Priority Queue

For priority queues, we will use composition to store items internally as pairs consisting of a key k and a value v. To
implement this concept for all priority queue implementations, we provide a **PriorityQueueBase** class.

### Implementation with an Unsorted List

we store entries within an unsorted list. These items are stored within a PositionalList, identified as the data member
of our class. We assume that the positional list is implemented with a doubly-linked list, so that all operations of
that ADT execute in O(1) time.

Each time a key-value pair is added to the priority queue, via the add method, we create a new Item composite for the
given key and value, and add that item to the end of the list. Such an implementation takes O(1) time. The remaining
challenge is that when `min` or `remove_min` is called, we must locate the item with minimum key. Because the items are
not sorted, we must inspect all entries to find one with a minimum key.

For convenience, we define a nonpublic `find_min` utility that returns the position of an item with minimum key.
Knowledge of the position allows the remove min method to invoke the delete method on the positional list. The min
method simply uses the position to retrieve the item when preparing a key-value tuple to return. Due to the loop for
finding the minimum key, both min and remove min methods run in O(n) time, where n is the number of entries in the
priority queue.

#### Comparison of the two list based implementations

We see an interesting tradeoff when we use a list to implement the priority queue ADT. An unsorted list supports fast
insertions but slow queries and deletions, whereas a sorted list allows fast queries and deletions, but slow insertions.

### Implementation with a Sorted List

We use a positional list, yet maintaining entries sorted by nondecreasing keys. This ensures that the first element of
the list is an entry with the smallest key. The implementation of min and remove min are rather straightforward given
knowledge that the first element of a list has a minimum key. We rely on the first method of the positional list to find
the position of the first item, and the delete method to remove the entry from the list. Assuming that the list is
implemented with a doubly linked list, operations min and remove min take O(1) time.

This benefit comes at a cost, however, for method add now requires that we scan the list to find the appropriate
position to insert the new item. Our implementation starts at the end of the list, walking backward until the new key is
smaller than an existing item; in the worst case, it progresses until reaching the front of the list. Therefore, the add
method takes O(n) worst-case time, where n is the number of entries in the priority queue at the time the method is
executed

## Heaps

we provide a more efficient realization of a priority queue using a data structure called a **binary heap**. This data
structure allows us to perform both insertions and removals in logarithmic time, which is a significant improvement over
the list-based implementations. The fundamental way the heap achieves this improvement is to use the structure of a
binary tree to find a compromise between elements being entirely unsorted and perfectly sorted.

*A **heap** is a binary tree T that stores a collection of items at its positions and that satisfies two additional
properties: a relational property defined in terms of the way keys are stored in T and a structural property defined in
terms of the shape of T itself*

**Heap-Order Property :** In a heap T, for every position p other than the root, the key stored at p is greater than or
equal to the key stored at p’s parent.

As a consequence of the heap-order property, the keys encountered on a path from the root to a leaf of T are in
nondecreasing order. Also, a minimum key is always stored at the root of T. This makes it easy to locate such an item
when min or remove min is called, as it is informally said to be “at the top of the heap” (hence, the name “heap” for
the data structure).

For the sake of efficiency, as will become clear later, we want the heap T to have as small a height as possible. We
enforce this requirement by insisting that the heap T satisfy an additional structural property—it must be what we term
**complete**.

**Complete Binary Tree Property :** A heap T with height h is a complete binary tree if levels 0,1,2,... ,h−1 of T have
the maximum number of nodes possible and the remaining nodes at level h reside in the leftmost possible positions at
that level.

In formalizing what we mean by the leftmost possible positions we said that a complete binary tree with n elements is
one that has positions with level numbering 0 through n−1.

Insisting that T be complete also has an important consequence.

**Proposition :** Aheap T storing n entries has height h = |_ log n _|.

### Implementing a Priority Queue with a Heap

The last proposition implies that if we can perform update operations on a heap in time proportional to its height, then
those operations will run in logarithmic time. Let us therefore turn to the problem of how to efficiently perform
various priority queue methods using a heap.

The len and is empty methods can be implemented based on examination of the tree, and the min operation is equally
trivial because the heap property assures that the element at the root of the tree has a minimum key. The interesting
algorithms are those for implementing the add and remove min methods.

#### Adding an Item to the Heap

We store the pair (k,v) as an item at a new node of the tree. To maintain the complete binary tree property, that new
node should be placed at a position p just beyond the rightmost node at the bottom level of the tree, or as the leftmost
position of a new level, if the bottom level is already full (or if the heap is empty).

After this action, the tree T is complete, but it may violate the heap-order property. Hence, unless position p is the
root of T we compare the key at position p to that of p’s parent, which we denote as q. If key `k_p ≥ k_q`, the
heap-order property is satisfied and the algorithm terminates. If instead `k_p < k_q`, then we need to restore the
heap-order property, which can be locally achieved by swapping the entries stored at positions p and q.

This swap causes the new item to move up one level. Again, the heap-order property may be violated, so we repeat the
process, going up in T until no violation of the heap-order property occurs. A swap either resolves the violation of the
heap-order property or propagates it one level up in the heap. In the worst case, **up-heap bubbling** causes the new
entry to move all the way up to the root of heap T. Thus, in the worst case, the number of swaps performed in the
execution ofmethod add is equal to the height of T. By Proposition, that bound is |_ log n _|.

#### Removing the Item with Minimum Key

We know that an entry with the smallest key is stored at the root r of T (even if there is more than one entry with
smallest key). We ensure that the shape of the heap respects the complete binary tree property by deleting the leaf at
the last position p of T, defined as the rightmost position at the bottommost level of the tree. To preserve the item
from the last position p, we copy it to the root r (in place of the item with minimum key that is being removed by the
operation).

even though T is now complete, it likely violates the heap-order property. If T has only one node (the root), then the
heap-order property is trivially satisfied and the algorithm terminates. Otherwise, we distinguish two cases, where p
initially denotes the root of T:

* If p has no right child, let c be the left child of p.
* Otherwise (p has both children), let c be a child of p with minimal key.

If key kp ≤ kc, the heap-order property is satisfied and the algorithm terminates. If instead kp >kc, then we need to
restore the heap-order property. This can be locally achieved by swapping the entries stored at p and c. Since we
intentionally consider the smaller key of the two children. Not only is the key of c smaller than that of p,it is at
least as small as the key at c’s sibling. This ensures that the heap-order property is locally restored when that
smaller key is promoted above the key that had been at p and that at c’s sibling.

Now , there may be a violation of this property at c; hence, we may have to continue swapping down T until no violation
of the heap-order property occurs. A swap either resolves the violation of the heap-order property or propagates it one
level down in the heap. In the worst case, an entry moves all the way down to the bottom level. Thus, the number of
swaps performed in the execution of method `remove_min` is, in the worst case, equal to the height of heap T, that is,
it is |_ log n _|.

### Array-Based Representation of a Complete Binary Tree

With this implementation, the elements of T have contiguous indices in the range `[0,n−1]` and the last position of T is
always at index n−1, where n is the number of positions of T.

Implementing a priority queue using an array-based heap representation allows us to avoid some complexities of a
node-based tree structure. In particular, the add and remove min operations of a priority queue both depend on locating
the last index of a heap of size n. With the array-based representation, the last position is at index n−1 of the array.
Locating the last position of a complete binary tree implemented with a linked structure requires more effort.

We use an array-based representation, maintaining a Python list of item composites.

### Analysis of a Heap-Based Priority Queue

assuming that two keys can be compared in O(1) time and that the heap T is implemented with an array-based or
linked-based tree representation, each of the priority queue ADT methods can be performed in O(1) or in O(logn) time,
where n is the number of entries at the time the method is executed.

* The min operation runs in O(1) because the root of the tree contains such an element.

* Locating the last position of a heap, as required for `add` and `remove_min`, can be performed in O(1) time for an
  array-based representation, or O(logn) time for a linked-tree representation

* In the worst case, up-heap and down-heap bubbling perform a number of swaps equal to the height of T.

The heap-based implementation achieves fast running times for both insertion and removal, unlike the implementations
that were based on using an unsorted or sorted list.

### Bottom-Up Heap Construction

### Python’s heapq Module

Python’s standard distribution includes a heapq module that provides support for heap-based priority queues. That module
does not provide any priority queue class; instead it provides functions that allow a standard Python list to be managed
as a heap. We note that heapq does not separately manage associated values; elements serve as their own key

The heapq module supports the following functions, all of which presume that existing list L satisfies the heap-order
property prior to the call:

## Sorting with a Priority Queue

As our first application of priority queues, we demonstrate how they can be used to sort a collection C of comparable
elements. That is, we can produce a sequence of elements ofC in increasing order (or at least in nondecreasing order if
there are duplicates). The algorithm is quite simple—we insert all elements into an initially empty priority queue, and
then we repeatedly call remove min to retrieve the elements in nondecreasing order.

### Selection-Sort and Insertion-Sort

Our pq sort function works correctly given any valid implementation of the priority queue class. However, the running
time of the sorting algorithm depends on the running times of the operations add and remove min for the given priority
queue class. We next discuss a choice of priority queue implementations that in effect cause the pq sort computation to
behave as one of several classic sorting algorithms.

If we implement P with an unsorted list, then Phase 1 of pq sort takes O(n) time, for we can add each element in O(1)
time. In Phase 2, the running time of each remove min operation is proportional to the size of P. Thus, the bottleneck
computation is the repeated “selection” of the minimum element in Phase 2. For this reason, this algorithm is better
known as **selection-sort**.

In Phase 2 we repeatedly remove an entry with smallest key from the priority queue P. The size of P starts at n and
incrementally decreases with each remove min until it becomes 0. Thus, Phase 2 takes time O(n2), as does the entire
selection-sort algorithm.

If we implement the priority queue P using a sorted list, then we improve the running time of Phase 2 to O(n), for each
remove min operation on P now takes O(1) time. Unfortunately, Phase 1 becomes the bottleneck for the running time,
since, in the worst case, each add operation takes time proportional to the current size of P. This sorting algorithm is
better known as **insertion-sort**.

This implies a worst-case O(n2) time for Phase 1, and thus, the entire insertion-sort algorithm. However, unlike
selection-sort, insertion sort has a best-case running time of O(n).

### Heap-Sort

During Phase 1, the ith add operation takes O(log i) time, since the heap has i entries after the operation is
performed. Therefore this phase takes O(nlogn) time. (It could be improved to O(n) with the bottom-up heap construction)

During the second phase of pq sort,the jth remove min operation runs in O(log(n− j +1)), since the heap has n− j +1
entries at the time the operation is performed. Summing over all j, this phase takes O(nlogn) time, so the entire
priority-queue sorting algorithm runs in O(nlogn) time when we use a heap to implement the priority queue. This sorting
algorithm is better known as **heap-sort**,

**Proposition:** The heap-sort algorithm sorts a collection C of n elements in O(nlogn) time, assuming two elements ofC
can be compared in O(1) time.

## Adaptable Priority Queues

there are situations in which additional methods would be useful, as shown by the scenarios below involving the standby
airline passenger application.

* A standby passenger with a pessimistic attitude may become tired of waiting and decide to leave ahead of the boarding
  time, requesting to be removed from the waiting list. Thus, we would like to remove from the priority queue the entry
  associated with this passenger. Operation remove min does not suffice since the passenger leaving does not necessarily
  have first priority. Instead, we want a new operation, remove, that removes an arbitrary entry.

* Another standby passenger finds her gold frequent-flyer card and shows it to the agent. Thus, her priority has to be
  modified accordingly. To achieve this change of priority, we would like to have a new operation update allowing us to
  replace the key of an existing entry with a new key.

### Locators

In order to implement methods update and remove efficiently, we need a mechanism for finding a user’s element within a
priority queue that avoids performing a linear search through the entire collection. To support our goal, when a new
element is added to the priority queue, we return a special object known as a locator to the caller. We then require the
user to provide an appropriate locator as a parameter when invoking the update or remove method, as follows, for a
priority queue P:

* **P.update(loc, k, v):** Replace key and value for the item identified by locator loc.
* **P.remove(loc):** Remove the item identified by locator loc from the priority queue and return its (key,value) pair.

a locator for a priority queue does not represent a tangible placement of an element within the structure. In our
priority queue, an element may be relocated within our data structure during an operation that does not seem directly
relevant to that element. A locator for an item will remain valid, as long as that item remains somewhere in the queue

### Implementing an Adaptable Priority Queue

To implement a Locator class, we will extend the existing Item composite to add a field designating the current index of
the element within the array-based representation of our heap.The list is a sequence of references to locator instances,
each of which stores a key, value, and the current index of the item within the list. The user will be given a reference
to the Locator instance for each inserted element, as portrayed by the token identifier

When we perform priority queue operations on our heap, and items are relocated within our structure, we reposition the
locator instances within the list and we update the third field of each locator to reflect its new index within the
list.

It is important to emphasize that the locator instances have not changed identity. The user’s token reference, continues
to reference the same instance; we have simply changed the third field of that instance, and we have changed where that
instance is referenced within the list sequence.