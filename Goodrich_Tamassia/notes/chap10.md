# Maps, Hash Tables, and Skip Lists

Python’s dict class is arguably the most significant data structure in the language. It represents an abstraction known
as a **dictionary** in which unique keys are mapped to associated values. Because of the relationship they express
between keys and values, dictionaries are commonly known as **associative arrays** or **maps**

We note that the keys (the country names) are assumed to be unique, but the values (the currency units) are not
necessarily unique.

## The Map ADT

we introduce the **map ADT**, and define its behaviors to be consistent with those of Python’s built-in dict class. We
begin by listing what we consider the most significant five behaviors of a map M as follows:

* `M[k]:` Return the value v associated with key k in map M,if one exists; otherwise raise a KeyError.
* `M[k] = v:` Associate value v with key k in map M, replacing the existing value if the map already contains an item
  with key equal to k
* `del M[k]:` Remove from map M the item with key equal to k;if M has no such item, then raise a KeyError.
* `len(M):` Return the number of items in map M.
* `iter(M):` The default iteration for a map generates a sequence of keys in the map.

We have highlighted the above five behaviors because they demonstrate the core functionality of a map—namely, the
ability to query, add, modify, or delete a keyvalue pair, and the ability to report all such pairs. For additional
convenience, map M should also support the following behaviors:

* `k in M:` Return True if the map contains an item with key k.
* `M.get(k, d=None):` Return M[k] if key k exists in the map; otherwise return default value d. This provides a form to
  query M[k] without risk of a KeyError.
* `M.setdefault(k, d):` If key k exists in the map, simply return M[k];if key k does not exist, set M[k] = d and return
  that value.
* `M.pop(k, d=None):` Remove the item associated with key k from the map and return its associated value v.If key k is
  not in the map, return default value d (or raise KeyError if parameter d is None).
* `M.popitem():` Remove an arbitrary key-value pair from the map, and return a (k,v) tuple representing the removed
  pair. If map is empty, raise a KeyError.
* `M.clear():` Remove all key-value pairs from the map.
* `M.keys():` Return a set-like view of all keys ofM.
* `M.values():` Return a set-like view of all values ofM.
* `M.items():` Return a set-like view of (k,v) tuples for all entries ofM.
* `M.update(M2):` Assign M[k] = v for every (k,v) pair in map M2.
* `M==M2:` Return True if maps M and M2 have identical key-value associations.
* `M!= M2:` Return True if maps M and M2 do not have identical keyvalue associations.

### Application: Counting Word Frequencies

consider the problem of counting the number of occurrences of words in a document. A map is an ideal data structure to
use here, for we can use words as keys and word counts as values. We break apart the original document using a
combination of file and string methods that results in a loop over a lowercased version of all whitespace separated
pieces of the document. We omit all nonalphabetic characters so that parentheses, apostrophes, and other such
punctuation are not considered part of a word.

### Python’s MutableMapping Abstract Base Class

The collections module provides two abstract base classes that are relevant to our current discussion: the `Mapping` and
`MutableMapping` classes. The Mapping class includes all nonmutating methods supported by Python’s dict class, while the
MutableMapping class extends that to include the mutating methods

The significance of these abstract base classes is that they provide a framework to assist in creating a user-defined
map class. In particular, the MutableMapping class provides concrete implementations for all behaviors other than the
first five outlined in a before section.

As we implement the map abstraction with various data structures, as long as we provide the five core behaviors, we can
inherit all other derived behaviors by simply declaring MutableMapping as a parent class.

### Our MapBase Class

We will be providing many different implementations of the map ADT, in the remainder of this chapter and next, using a
variety of data structures demonstrating a trade-off of advantages and disadvantages. The MutableMapping abstract base
class, from Python’s collections module and discussed in the preceding pages, is a valuable tool when implementing a
map. However, in the interest of greater code reuse, we define our own MapBase class, which is itself a subclass of the
MutableMapping class. Our MapBase class provides additional support for the composition design pattern

our MapBase class extending the existing MutableMapping abstract base class so that we inherit the many useful concrete
methods that class provides. We then define a nonpublic nested _Item class, whose instances are able to store both a key
and value

### Simple Unsorted Map Implementation

This implementation relies on storing key-value pairs in arbitrary order within a Python list.

This list-based map implementation is simple, but it is not particularly efficient. Each of the fundamental methods,
`__getitem__`,`__setitem__`,and `__delitem__` , relies on a for loop to scan the underlying list of items in search of a
matching key. Therefore, each of these methods runs in O(n) time on a map with n items.

## Hash Tables

### Collision-Handling Schemes

The main idea of a hash table is to take a bucket array, A, and a hash function, h,and use them to implement a map by
storing each item (k,v) in the “bucket” `A[h(k)]`. This simple idea is challenged, however, when we have two distinct
keys, k1 and k2, such that `h(k1)= h(k2)`. The existence of such collisions prevents us from simply inserting a new
item `(k,v)` directly into the bucket `A[h(k)]`. It also complicates our procedure for performing insertion, search, and
deletion operations.

#### Separate Chaining

A simple and efficient way for dealing with collisions is to have each bucket A[ j] store its own secondary container,
holding items (k,v) such that h(k)= j. A natural choice for the secondary container is a small map instance implemented
using a list. This **collision resolution rule** is known as **separate chaining**.

In the worst case, operations on an individual bucket take time proportional to the size of the bucket. Assuming we use
a good hash function to index the n items of our map in a bucket array of capacity N, the expected size of a bucket is
n/N. Therefore, if given a good hash function, the core map operations run in `O([n/N])`. The ratio `λ = n/N`, called
the **load factor** of the hash table, should be bounded by a small constant, preferably below 1. As long as λ is O(1),
the core operations on the hash table run in O(1) expected time.

#### Open Addressing

The separate chaining rule has one slight disadvantage: It requires the use of an auxiliary data structure—a list—to
hold items with colliding keys. If space is at a premium (for example, if we are writing a program for a small handheld
device), then we can use the alternative approach of always storing each item directly in a table slot. This approach
saves space because no auxiliary structures are employed, but it requires a bit more complexity to deal with collisions.
There are several variants of this approach, collectively referred to as **open addressing schemes**.

Open addressing requires that the load factor is always at most 1 and that items are stored directly in the cells of the
bucket array itself.

##### Linear Probing and Its Variants

### Python Hash Table Implementation

In this section, we develop two implementations of a hash table, one using separate chaining and the other using open
addressing with linear probing. we extend the MapBase class to define a new HashMapBase class providing much of the
common functionality to our two hash table implementations. The main design elements of the HashMapBase class are:

* The bucket array is represented as a Python list, named self. table, with all entries initialized to None.
* We maintain an instance variable self. n that represents the number of distinct items that are currently stored in the
  hash table.
* If the load factor of the table increases beyond 0.5, we double the size of the table and rehash all items into the
  new table.
* We define a hash function utility method that relies on Python’s built-in hash function to produce hash codes for
  keys, and a randomized MultiplyAdd-and-Divide (MAD) formula for the compression function.

What is not implemented in the base class is any notion of how a “bucket” should be represented. With separate chaining,
each bucket will be an independent structure. With open addressing, however, there is no tangible container for each
bucket; the “buckets” are effectively interleaved due to the probing sequences.

In our design, the HashMapBase class presumes the following to be abstract methods, which must be implemented by each
concrete subclass:

* _bucket_getitem(j, k) This method should search bucket j for an item having key k, returning the associated value, if
  found, or else raising a KeyError.
* _bucket_setitem(j, k, v) This method should modify bucket j so that key k becomes associated with value v. If the key
  already exists, the new value overwrites the existing value. Otherwise, a new item is inserted and this method is
  responsible for incrementing self. n.
* _bucket_delitem(j, k) This method should remove the item from bucket j having key k, or raise a KeyError if no such
  item exists. (self. n is decremented after this method.)
* __iter__ This is the standard map method to iterate through all keys of the map. Our base class does not delegate this
  on a per-bucket basis because “buckets” in open addressing are not inherently disjoint.

## Sorted Maps

The traditional map ADT allows a user to look up the value associated with a given key, but the search for that key is a
form known as an **exact search**. In fact, the fast performance of hash-based implementations of the map ADT relies on
the intentionally scattering of keys that may seem very “near” to each other in the original domain, so that they are
more uniformly distributed in a hash table.

In this section, we introduce an extension known as the **sorted map** ADT that includes all behaviors of the standard
map, plus the following:

* M.find_min(): Return the (key,value) pair with minimum key (or None, if map is empty).
* M.find_max(): Return the (key,value) pair with maximum key (or None, if map is empty).
* M.find_lt(k): Return the (key,value) pair with the greatest key that is strictly less than k (or None,if no such item
  exists).
* M.find_le(k): Return the (key,value) pair with the greatest key that is less than or equal to k (or None, if no such
  item exists).
* M.find_gt(k): Return the (key,value) pair with the least key that is strictly greater than k (or None,if no such item
  exists).
* M.find_ge(k): Return the (key,value) pair with the least key that is greater than or equal to k (or None,if no such
  item exists).
* M.find_range(start, stop): Iterate all (key,value) pairs with start <=key < stop. If start is None, iteration begins
  with minimum key; if stop is None, iteration concludes with maximum key.
* iter(M): Iterate all keys of the map according to their natural order, from smallest to largest.
* reversed(M): Iterate all keys of the map in reverse order; in Python, this is implemented with the reversed method.

### Sorted Search Tables

In this section, we begin by exploring a simple implementation of a sorted map. We store the map’s items in an
array-based sequence A so that they are in increasing order of their keys, assuming the keys have a naturally defined
order. We refer to this implementation of a map as a **sorted search table**.

the sorted search table has a space requirement that is O(n), assuming we grow and shrink the array to keep its size
proportional to the number of items in the map. The primary advantage of this representation, and our reason for
insisting that A be array-based, is that it allows us to use the binary search algorithm for a variety of efficient
operations.

we can adapt the binary search algorithm to provide far more useful information when performing forms of inexact search
in support of the sorted map ADT.

The important realization is that while performing a binary search, we can determine the index at or near where a target
might be found. During a successful search, the standard implementation determines the precise index at which the target
is found. During an unsuccessful search, although the target is not found, the algorithm will effectively determine a
pair of indices designating elements of the collection that are just less than or just greater than the missing target.

The most notable feature of our design is the inclusion of a `_find_index` utility function. This method using the
binary search algorithm, but by convention returns the *index* of the leftmost item in the search interval having key
greater than or equal to k. Therefore, if the key is present, it will return the index of the item having that key. (
Recall that keys are unique in a map.) When the key is missing, the function returns the index of the item in the search
interval that is just beyond where the key would have been located. As a technicality, the method returns index high+1
to indicate that no items of the interval had a key greater than k.

We rely on this utility method when implementing the traditional map operations and the new sorted map operations

#### Analysis

We conclude by analyzing the performance of our SortedTableMap implementation.

It should be clear that the len , find min,and find max methods run in O(1) time, and that iterating the keys of the
table in either direction can be performed in O(n) time. The analysis for the various forms of search all depend on the
fact that a binary search on a table with n entries runs in O(logn) time.

We therefore claim an O(logn) worst-case running time for methods `__getitem__, find_lt, find_gt, find_le, and find_ge`.
Each of these makes a single call to find index, followed by a constant number of additional steps to determine the
appropriate answer based on the index.

The analysis of find range is a bit more interesting. It begins with a binary search to find the first item within the
range (if any). After that, it executes a loop that takes O(1) time per iteration to report subsequent values until
reaching the end of the range. If there are s items reported in the range, the total running time is O(s+logn).

In contrast to the efficient search operations, update operations for a sorted table may take considerable time.
Although binary search can help identify the index at which an update occurs, both insertions and deletions require, in
the worst case, that linearly many existing elements be shifted in order to maintain the sorted order of the table.
Specifically, the potential call to `_table.insert` from within `__setitem__` and `_table.pop` from within `__delitem__`
lead to O(n) worst-case time.

### Two Applications of Sorted Maps

In this section, we explore applications in which there is particular advantage to using a sorted map rather than a
traditional (unsorted) map. To apply a sorted map, keys must come from a domain that is totally ordered. Furthermore, to
take advantage of the inexact or range searches afforded by a sorted map, there should be some reason why nearby keys
have relevance to a search.

#### Maxima Sets

## Skip Lists

An interesting data structure for realizing the sorted map ADT is the **skip list**. Unfortunately, update operations on
a sorted array have O(n) worst-case running time because of the need to shift elements. we demonstrated that linked
lists support very efficient update operations, as long as the position within the list is identified. Unfortunately, we
cannot perform fast searches on a standard linked lists.

Skip lists provide a clever compromise to efficiently support search and update operations. A skip list S for a map M
consists of a series of lists `{S_0, S_1, ... , S_h}`. Each list `S_i` store a subset of the items of M sorted by
increasing keys, plus items with two sentinel keys denoted `- inf` and `+ inf`, where `- inf` is smaller than every
possible key that can be inserted in M and `+ inf` is larger than every possible key that can be inserted in M. In
addition, the lists in S satisfy the following:

* List S0 contains every item of the map M (plus sentinels −∞ and +∞).
* For i = 1, ..., h-1, list Si contains (in addition to −∞ and +∞) a randomly generated subset of the items in list
  Si−1.
* List Sh contains only −∞ and +∞.

Also, we refer to h as the **height** of skip list S.

As we shall see in the details of the insertion method, the items in Si+1 are chosen at random from the items in Si by
picking each item from Si to also be in Si+1 with probability 1/2. That is, in essence, we “flip a coin” for each item
in Si and place that item in Si+1 if the coin comes up “heads.” Thus, we expect S1 to have about n/2 items, S2 to have
about n/4 items, and, in general, Si to have about n/2^i items. In other words, we expect the height h of S to be about
logn.

Some functions, called **pseudorandom number generators**, generate random-like numbers, starting with an initial **
seed**. Other methods use hardware devices to extract “true” random numbers from nature. In any case, we will assume
that our computer has access to numbers that are sufficiently random for our analysis.

The main advantage of using **randomization** in data structure and algorithm design is that the structures and
functions that result are usually simple and efficient. The skip list has the same logarithmic time bounds for searching
as is achieved by the binary search algorithm, yet it extends that performance to update methods when inserting or
deleting items. Nevertheless, the bounds are **expected** for the skip list, while binary search has a **worst-case**
bound with a sorted table.

A skip list makes random choices in arranging its structure in such a way that search and update times are O(logn)
**on average**,where n is the number of items in the map. Interestingly, the notion of average time complexity used here
does not depend on the probability distribution of the keys in the input. Instead, it depends on the use of a
random-number generator in the implementation of the insertions to help decide where to place the new item.

The running time is averaged over all possible outcomes of the random numbers used when inserting entries. Using the
position abstraction used for lists and trees, we view a skip list as a two-dimensional collection of positions arranged
horizontally into **levels** and vertically into **towers**.

Each level is a list Si and each tower contains positions storing the same item across consecutive lists. The positions
in a skip list can be traversed using the following operations:

* next(p): Return the position following p on the same level.
* prev(p): Return the position preceding p on the same level.
* below(p): Return the position below p in the same tower.
* above(p): Return the position above p in the same tower.

We conventionally assume that the above operations return None if the position requested does not exist. Without going
into the details, we note that we can easily implement a skip list by means of a linked structure such that the
individual traversal methods each take O(1) time, given a skip-list position p. Such a linked structure is essentially a
collection of h doubly linked lists aligned at towers, which are also doubly linked lists.

### Search and Update Operations in a Skip List

In fact, all the skip-list search and update algorithms are based on an elegant `SkipSearch` method that takes a key k
and finds the position p of the item in list S0 that has the largest key less than or equal to k (which is possibly −∞).

Suppose we are given a search key k. We begin the SkipSearch method by setting a position variable p to the topmost,
left position in the skip list S, called the **start position** of S. We then perform the following steps, where key(p)
denotes the key of the item at position p:

1. If S.below(p) is None, then the search terminates—we are **at the bottom** and have located the item in S with the
   largest key less than or equal to the search key k. Otherwise, we **drop down** to the next lower level in the
   present tower by setting p = S.below(p).
2. Starting at position p, we move p forward until it is at the rightmost position on the present level such
   that `key(p) ≤ k`. We call this the **scan forward** step. Note that such a position always exists, since each level
   contains the keys +∞ and −∞. It may be that p remains where it started after we perform such a forward scan for this
   level.
3. Return to step 1.

Given this method, the map operation `M[k]` is performed by computing `p = SkipSearch(k)` and testing whether
`key(p)= k`. If these two keys are equal, we return the associated value; otherwise, we raise a KeyError.

    Algorithm SkipSearch(k): 
        Input: A search key k 
        Output: Position p in the bottom list S0 with the largest key such that key(p)≤k
        
        p = start                   {begin at start position}
        while below(p) != None do 
            p = below(p)                    {drop down}
            while k >= key(next(p)) do
                p = next(p)                 {scan forward}
        return p.

As it turns out, the expected running time of algorithm SkipSearch on a skip list with n entries is O(logn). Navigation
starting at the position identified by SkipSearch(k) can be easily used to provide the additional forms of searches in
the sorted map ADT.

### Insertion in a Skip List

The execution of the map operation `M[k] = v` begins with a call to SkipSearch(k). This gives us the position p of the
bottom-level item with the largest key less than or equal to k (note that p may hold the special item with key −∞). If
`key(p)= k`,the associated value is overwritten with v. Otherwise, we need to create a new tower for item (k,v).

We insert (k,v) immediately after position p within S0. After inserting the new item at the bottom level, we use
randomization to decide the height of the tower for the new item. We “flip” a coin, and if the flip comes up tails, then
we stop here. Else (the flip comes up heads), we backtrack to the previous (next higher) level and insert (k,v) in this
level at the appropriate position. We again flip a coin; if it comes up heads, we go to the next higher level and
repeat. Thus, we continue to insert the new item (k,v) in lists until we finally get a flip that comes up tails.

We link together all the references to the new item (k,v) created in this process to create its tower. A coin flip can
be simulated with Python’s built-in pseudo-random number generator from the random module by calling randrange(2), which
returns 0 or 1, each with probability 1/2.

    Algorithm SkipInsert(k,v): 
        Input: Key k and value v 
        Output: Topmost position of the item inserted in the skip list 
        
        p = SkipSearch(k) 
        q = None                                {q will represent top node in new item’s tower}
        i = −1 
        repeat 
            i = i+1 
            if i ≥ h then 
                h = h+1                         {add a new level to the skip list}
                t = next(s) 
                s = insertAfterAbove(None, s, (−∞,None))  {grow leftmost tower} 
                insertAfterAbove(s, t,(+∞,None))   {grow rightmost tower}
            while above(p) is None do 
                p = prev(p)             {scan backward}
            p = above(p)                {jump up to higher level}
            q = insertAfterAbove(p,q, (k,v))                {increase height of new item’s tower}
        until coinFlip() == tails 
        n = n+1 
        return q

### Removal in a Skip List

to perform the map operation del `M[k]` we begin by executing method SkipSearch(k). If the position p stores an entry
with key different from k, we raise a KeyError. Otherwise, we remove p and all the positions above p, which are easily
accessed by using above operations to climb up the tower of this entry in S starting at position p. While removing
levels of the tower, we reestablish links between the horizontal neighbors of each removed position.

As we show in the next subsection, deletion operation in a skip list with n entries has O(logn) expected running time.

there are some minor improvements to the skip-list data structure we would like to discuss. First, we do not actually
need to store references to values at the levels of the skip list above the bottom level, because all that is needed at
these levels are references to keys. In fact, we can more efficiently represent a tower as a single object, storing the
key-value pair, and maintaining j previous references and j next references if the tower reaches level Sj.

Second, for the horizontal axes, it is possible to keep the list singly linked, storing only the next references. We can
perform insertions and removals in strictly a top-down, scan-forward fashion.

Neither of these optimizations improve the asymptotic performance of skip lists by more than a constant factor, but
these improvements can, nevertheless, be meaningful in practice. In fact, experimental evidence suggests that optimized
skip lists are faster in practice than AVL trees and other balanced search trees.

### Maintaining the Topmost Level

A skip list S must maintain a reference to the start position (the topmost, left position in S) as an instance variable,
and must have a policy for any insertion that wishes to continue inserting a new entry past the top level of S.There are
two possible courses of action we can take, both of which have their merits.

One possibility is to restrict the top level, h, to be kept at some fixed value that is a function of n, the number of
entries currently in the map (from the analysis we will see that `h=max{10,2 |log n|}` is a reasonable choice, and
picking `h=3|logn|` is even safer). Implementing this choice means that we must modify the insertion algorithm to stop
inserting a new position once we reach the topmost level (unless `|logn| < |log(n+1)|`, in which case we can now go at
least one more level, since the bound on the height is increasing).

The other possibility is to let an insertion continue inserting a new position as long as heads keeps getting returned
from the random number generator. As we show in the analysis of skip lists, the probability that an insertion will go to
a level that is more than O(logn) is very low, so this design choice should also work.

Table summarizes the performance of a sorted map realized by a skip list.

    Operation                       |                            Running Time 
    len(M)                                                          O(1) 
    k in M                                                      O(logn) expected
    M[k] = v                                                    O(logn) expected 
    del M[k]                                                    O(logn) expected
    M.find_min(), M.find_max()                                      O(1) 
    M.find_lt(k), M.find_gt(k)                                  O(logn) expected
    M.find le(k), M.find ge(k)  
    M.find range(start, stop)                          O(s+logn) expected, with s items reported 
    iter(M), reversed(M)                                            O(n)

## Sets, Multisets, and Multimaps

We conclude this chapter by examining several additional abstractions that are closely related to the map ADT, and that
can be implemented using data structures similar to those for a map.

* A **set** is an unordered collection of elements, without duplicates, that typically supports efficient membership
  tests. In essence, elements of a set are like keys of a map, but without any auxiliary values.
* A **multiset** (also known as a **bag**) is a set-like container that allows duplicates.
* A **multimap** is similar to a traditional map, in that it associates values with keys; however, in a multimap the
  same key can be mapped to multiple values. For example, the index of this book maps a given term to one or more
  locations at which the term occurs elsewhere in the book.

### The Set ADT

Python provides support for representing the mathematical notion of a set through the built-in classes frozenset and
set. Both of those classes are implemented using hash tables in Python. Python’s collections module defines abstract
base classes that essentially mirror these built-in classes.

> the abstract base class collections.Set matches the concrete frozenset class, while the abstract base class
> collections.MutableSet is akin to the concrete set class.

In our own discussion, we equate the “set ADT” with the behavior of the builtin set class (and thus, the
collections.MutableSet base class). We begin by listing what we consider to be the five most fundamental behaviors for a
set S:

* S.add(e): Add element e to the set. This has no effect if the set already contains e.
* S.discard(e): Remove element e from the set, if present. This has no effect if the set does not contain e.
* e in S: Return True if the set contains element e. In Python, this is implemented with the special contains method.
* len(S): Return the number of elements in set S. In Python, this is implemented with the special method len .
* iter(S): Generate an iteration of all elements of the set.

Those remaining behaviors can be naturally grouped as follows. We begin by describing the following additional
operations for removing one or more elements from a set:

S.remove(e): Remove element e from the set. If the set does not contain e, raise a KeyError. S.pop(): Remove and return
an arbitrary element from the set. If the set is empty, raise a KeyError. S.clear(): Remove all elements from the set.

The next group of behaviors perform Boolean comparisons between two sets.

* S==T: Return True if sets S and T have identical contents.
* S!=T: Return True if sets S and T are not equivalent.
* S <=T: Return True if set S is a subset of set T.
* S < T: Return True if set S is a proper subset of set T.
* S >=T: Return True if set S is a superset of set T.
* S > T: Return True if set S is a proper superset of set T.
* S.isdisjoint(T): Return True if sets S and T have no common elements.

Finally, there exists a variety of behaviors that either update an existing set, or compute a new set instance, based on
classical set theory operations.

* S | T: Return a new set representing the union of sets S and T.
* S |=T: Update set S to be the union of S and set T.
* S & T: Return a new set representing the intersection of sets S and T.
* S &= T: Update set S to be the intersection of S and set T.
* SˆT: Return a new set representing the symmetric difference of sets S and T, that is, a set of elements that are in
  precisely one of S or T.
* Sˆ=T: Update set S to become the symmetric difference of itself and set T.
* S − T: Return a new set containing elements in S but not T.
* S −=T: Update set S to remove all common elements with set T.

#### Python’s MutableSet Abstract Base Class

To aid in the creation of user-defined set classes, Python’s collections module provides a MutableSet abstract base
class. The MutableSet base class provides concrete implementations for all methods described before, except for five
core behaviors (add, discard, __contains__ , __len__ ,and __iter__ ) that must be implemented by any concrete subclass.

> This design is an example of what is known as the **template method pattern**, as the concrete methods of the MutableSet
> class rely on the presumed abstract methods that will subsequently be provided by a subclass.

### Implementing Sets, Multisets, and Multimaps

Although sets and maps have very different public interfaces, they are really quite similar. A set is simply a map in
which keys do not have associated values. Any data structure used to implement a map can be modified to implement the
set ADT with similar performance guarantees. We could trivially adapt any map class by storing set elements as keys, and
using None as an irrelevant value, but such an implementation is unnecessarily wasteful. An efficient set implementation
should abandon the Item composite that we use in our MapBase class and instead store set elements directly in a data
structure.

**Multisets**

The same element may occur several times in a multiset. All of the data structures we have seen can be reimplemented to
allow for duplicates to appear as separate elements. However, another way to implement a multiset is by using a map in
which the map key is a (distinct) element of the multiset, and the associated value is a count of the number of
occurrences of that element within the multiset.

Python’s standard collections module includes a definition for a class named `Counter` that is in essence a multiset.
Formally, the Counter class is a subclass of dict, with the expectation that values are integers, and with additional
functionality like a `most_common(n)` method that returns a list of the n most common elements. The standard `__iter__`
reports each element only once (since those are formally the keys of the dictionary). There is another method named
`elements()` that iterates through the multiset with each element being repeated according to its count.

**Multimaps**

Although there is no multimap in Python’s standard libraries, a common implementation approach is to use a standard map
in which the value associated with a key is itself a container class storing any number of associated values. Our
implementation uses the standard dict class as the map, and a list of values as a composite value in the dictionary. We
have designed the class so that a different map implementation can easily be substituted by overriding the class-level
MapType attribute 