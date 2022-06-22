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

