## SORTING AND SEARCHING

### Searching
Searching is the algorithmic process of finding a particular item in a collection of items. A search typically answers
either True or False as to whether the item is present. On occasion it may be modified to return where the item
is found. For our purposes here, we will simply concern ourselves with the question of membership.

It turns out that there are many different ways to search for the item. What we are interested in here is how these
algorithms work and how they compare to one another.

#### The Sequential Search
When data items are stored in a collection such as a list, we say that they have a linear or
sequential relationship. Each data item is stored in a position relative to the others

Since these index values are ordered, it is possible for us to visit them in sequence. This process gives rise to our
first searching technique, the sequential search

Starting at the first item in the list, we simply move
from item to item, following the underlying sequential ordering until we either find what we
are looking for or run out of items. If we run out of items, we have discovered that the item we
were searching for was not present.

###### Analysis of Sequential Search
To analyze searching algorithms, we need to decide on a basic unit of computation. Recall
that this is typically the common step that must be repeated in order to solve the problem. For
searching, it makes sense to count the number of comparisons performed. Each comparison
may or may not discover the item we are looking for.

In addition, we make another assumption here. The list of items is not ordered in any way. The items have been
placed randomly into the list. In other words, the probability that the item we are looking
for is in any particular position is exactly the same for each position of the list.

If the item is not in the list, the only way to know it is to compare it against every item present.
If there are 𝑛 items, then the sequential search requires 𝑛 comparisons to discover that the item
is not there

In the case where the item is in the list, the analysis is not so straightforward.
There are actually three different scenarios that can occur. In the best case we will find the item
in the first place we look, at the beginning of the list. We will need only one comparison. In the
worst case, we will not discover the item until the very last comparison, the nth comparison.
What about the average case? On average, we will find the item about halfway into the list; that is n/2.

Recall, however, that as 𝑛 gets large, the coefficients,
no matter what they are, become insignificant in our approximation, so the complexity of the
sequential search, is 𝑂(𝑛).

**Ordered Lists**
What would happen to the sequential search if the items were ordered in some way? Would we be able to gain
any efficiency in our search technique?

Assume that the list of items was constructed so that the items were in ascending order, from
low to high. If the item we are looking for is present in the list, the chance of it being in
any one of the 𝑛 positions is still the same as before. We will still have the same number of
comparisons to find the item. However, if the item is not present there is a slight advantage.
In this case, the algorithm does not have to continue looking through all of the
items to report that the item was not found. It can stop immediately

On average, we will know after looking through only n^2 items. However, this technique is still 𝑂(𝑛).
In summary, a sequential search is improved by ordering the list only in the case where we do not find the item.

### The Binary Search

It is possible to take greater advantage of the ordered list if we are clever with our comparisons.
Instead of searching the list in sequence, a **binary search** will start by examining the middle item.
If that item is the one we are searching for, we are done.
If it is not the correct item, we can use the ordered nature of
the list to eliminate half of the remaining items. If the item we are searching for is greater than
the middle item, we know that the entire lower half of the list as well as the middle item can be
eliminated from further consideration. The item, if it is in the list, must be in the upper half.

We can then repeat the process with the upper half. Start at the middle item and compare
it against what we are looking for. Again, we either find it or split the list in half, therefore
eliminating another large part of our possible search space

When we perform a binary search of a list, we first check the middle item.
If the item we are searching for is less than the middle item, we can simply perform a binary
search of the left half of the original list. Likewise, if the item is greater, we can perform a
binary search of the right half. Either way, this is a recursive call to the binary search function
passing a smaller list.

###### Analysis of Binary Search
To analyze the binary search algorithm, we need to recall that each comparison eliminates about
half of the remaining items from consideration. What is the maximum number of comparisons
this algorithm will require to check the entire list?
How many times can we split the list?

When we split the list enough times, we end up with a list that has just one item. Either that is
the item we are looking for or it is not. Either way, we are done. The number of comparisons
necessary to get to this point is 𝑖 where n/2^𝑖 = 1. Solving for 𝑖 gives us 𝑖 = log 𝑛. The maximum
number of comparisons is logarithmic with respect to the number of items in the list. Therefore,
the binary search is 𝑂(log 𝑛).

Even though a binary search is generally better than a sequential search, it is important to note
that for small values of 𝑛, the additional cost of sorting is probably not worth it. In fact, we
should always consider whether it is cost effective to take on the extra work of sorting to gain
searching benefits. If we can sort once and then search many times, the cost of the sort is
not so significant. However, for large lists, sorting even once can be so expensive that simply
performing a sequential search from the start may be the best choice.

### Hashing

In this section we will attempt to go one step further by building a data structure that can be searched in 𝑂(1) time.
This concept is referred to as hashing.
In order to do this, we will need to know even more about where the items might be when we
go to look for them in the collection. If every item is where it should be, then the search can
use a single comparison to discover the presence of an item

A **hash table** is a collection of items which are stored in such a way as to make it easy to find
them later.  Each position of the hash table, often called a slot, can hold an item and is named
by an integer value starting at 0

Initially, the hash table contains no items so every slot is empty. We
can implement a hash table by using a list with each element initialized to the special Python
value None.

The mapping between an item and the slot where that item belongs in the hash table is called
the **hash function**. The hash function will take any item in the collection and return an integer
in the range of slot names, between 0 and 𝑚 − 1 (m the size of the hash table)

Our first hash function, sometimes referred to as the **“remainder method,”** simply takes an item and divides it by
the table size, returning the remainder as its hash value (𝑕(item) = item%m).
Note that this remainder method (modulo arithmetic) will typically be present in some form in
all hash functions, since the result must be in the range of slot names.

Once the hash values have been computed, we can insert each item into the hash table at the
designated position. The **load factor**  is commonly denoted by i = number_items / size and represent how of the hash
table is occupied.

Now when we want to search for an item, we simply use the hash function to compute the slot
name for the item and then check the hash table to see if it is present. This searching operation
is 𝑂(1), since a constant amount of time is required to compute the hash value and then index
the hash table at that location. If everything is where it should be, we have found a constant
time search algorithm.

this technique is going to work only if each item maps to a
unique location in the hash table. According to the hash function, two or more items would need to
be in the same slot. This is referred to as a collision (it may also be called a “clash”). Clearly,
collisions create a problem for the hashing technique

###### Hash Functions

Given a collection of items, a hash function that maps each item into a unique slot is referred to
as a perfect hash function. If we know the items and the collection will never change, then it is
possible to construct a perfect hash function. Unfortunately, given an arbitrary collection of items, there is
no systematic way to construct a perfect hash function. Luckily, we do not need the hash function to be perfect to
still gain performance efficiency.

Our goal is to create a hash function that minimizes the number of collisions, is easy to compute,
and evenly distributes the items in the hash table. There are a number of common ways to
extend the simple remainder method. We will consider a few of them here.

> The **folding method** for constructing hash functions begins by dividing the item into equal size pieces
>(the last piece may not be of equal size). These pieces are then added together
to give the resulting hash value. For example, if our item was the phone number 436-555-
4601, we would take the digits and divide them into groups of 2 (43, 65, 55, 46, 01). After the
addition, 43 + 65 + 55 + 46 + 01, we get 210. If we assume our hash table has 11 slots, then
we need to perform the extra step of dividing by 11 and keeping the remainder. In this case
210%11 is 1, so the phone number 436-555-4601 hashes to slot 1.


> Another numerical technique for constructing a hash function is called the **mid-square method**. We first square the
>item, and then extract some portion of the resulting digits. For example, if the item were 44, we would first
>compute 44^2 = 1,936. By extracting the middle two digits, 93, and performing the remainder step, we get 5 (93%11).

We can also create hash functions for character-based items such as strings. The word “cat”
can be thought of as a sequence of ordinal values. We can then take these three ordinal values, add them up, and use
the remainder method to get a hash value

You may be able to think of a number of additional ways to compute hash values for items
in a collection. The important thing to remember is that the hash function has to be efficient
so that it does not become the dominant part of the storage and search process. If the hash
function is too complex, then it becomes more work to compute the slot name than it would be
to simply do a basic sequential or binary search as described earlier. This would quickly defeat
the purpose of hashing

**Collision Resolution :**  When two items hash to the same slot, we must
have a systematic method for placing the second item in the hash table. This process is called
collision resolution.

One method for resolving collisions looks into the hash table and tries to find another open slot
to hold the item that caused the collision. A simple way to do this is to start at the original
hash value position and then move in a sequential manner through the slots until we encounter
the first slot that is empty. Note that we may need to go back to the first slot (circularly) to
cover the entire hash table. This collision resolution process is referred to as **open addressing**
in that it tries to find the next open slot or address in the hash table. By systematically visiting
each slot one at a time, we are performing an open addressing technique called **linear probing**.

The general name for this process of looking for another slot after a collision is **rehashing**. With
simple linear probing, the rehash function is

    new_hash_value = rehash(old_hash_value)

where

    rehash(pos) = (pos + 1)%size_of_table.

The “plus 3” rehash can be defined as

    rehash(pos) = (pos + 3)%size_of_table

In general,

    rehash(pos) = (pos + skip)%sizeoftable.

It is important to note that the size of the “skip” must be such that all the slots in the table will
eventually be visited. Otherwise, part of the table will be unused. To ensure this, it is often
suggested that the table size be a prime number

An alternative method for handling the collision problem is to allow each slot to hold a reference
to a collection (or chain) of items. **Chaining** allows many items to exist at the same location
in the hash table. When collisions happen, the item is still placed in the proper slot of the hash
table. As more and more items hash to the same location, the difficulty of searching for the
item in the collection increases

When we want to search for an item, we use the hash function to generate the slot where
it should reside. Since each slot holds a collection, we use a searching technique to decide
whether the item is present. The advantage is that on the average there are likely to be many
fewer items in each slot, so the search is perhaps more efficient.

#### Implementing the Map Abstract Data Type

Recall that a dictionary is an associative data type where you can store key-data pairs. The key is used to look up
the associated data value. We often refer to this idea as a map.

> The structure is an unordered collection of associations between a key and a data value. The keys in a map are all
>unique so that there is a one-to-one relationship between a key and a value. The operations are given below.

• Map() Create a new, empty map. It returns an empty map collection.

• put(key,val) Add a new key-value pair to the map. If the key is already in the map
then replace the old value with the new value.

• get(key) Given a key, return the value stored in the map or None otherwise.

• del Delete the key-value pair from the map using a statement of the form del map[key].

• len() Return the number of key-value pairs stored in the map.

• in Return True for a statement of the form key in map, if the given key is in the map,
False otherwise.

##### Analysis of Hashing
We stated earlier that in the best case hashing would provide a 𝑂(1), constant time search
technique. However, due to collisions, the number of comparisons is typically not so simple.

The most important piece of information we need to analyze the use of a hash table is the load
factor, 𝜆. Conceptually, if 𝜆 is small, then there is a lower chance of collisions, meaning that
items are more likely to be in the slots where they belong. If 𝜆 is large, meaning that the table is
filling up, then there are more and more collisions. This means that collision resolution is more
difficult, requiring more comparisons to find an empty slot. With chaining, increased collisions
means an increased number of items on each chain.

If we are using chaining, the average number of comparisons is 1 + 𝜆/2 for the successful case, and simply 𝜆
comparisons if the search is unsuccessful

### Sorting
>Sorting is the process of placing elements from a collection in some kind of order.

Sorting a large number of items
can take a substantial amount of computing resources. Like searching, the efficiency of a
sorting algorithm is related to the number of items being processed. For small collections, a
complex sorting method may be more trouble than it is worth. The overhead may be too high.

On the other hand, for larger collections, we want to take advantage of as many improvements
as possible.

Before getting into specific algorithms, we should think about the operations that can be used
to analyze a sorting process. First, it will be necessary to compare two values to see which is
smaller (or larger). In order to sort a collection, it will be necessary to have some systematic
way to compare values to see if they are out of order. *The total number of comparisons will be
the most common way to measure a sort procedure*. Second, when values are not in the correct
position with respect to one another, it may be necessary to exchange them. This exchange is
a costly operation and *the total number of exchanges* will also be important for evaluating the
overall efficiency of the algorithm

#### Bubble Sort

> The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of
>order. Each pass through the list places the next largest value in
its proper place. In essence, each item “bubbles” up to the location where it belongs.

If there are 𝑛 items in the list, then there are 𝑛 − 1 pairs of items that
need to be compared on the first pass. It is important to note that once the largest value in the
list is part of a pair, it will continually be moved along until the pass is complete.

At the start of the second pass, the largest value is now in place. There are 𝑛 − 1 items left to
sort, meaning that there will be 𝑛 − 2 pairs. Since each pass places the next largest value in
place, the total number of passes necessary will be 𝑛 − 1. After completing the 𝑛 − 1 passes,
the smallest item must be in the correct position with no further processing required.

###### Time Analysis

To analyze the bubble sort, we should note that regardless of how the items are arranged in
the initial list, 𝑛 − 1 passes will be made to sort a list of size n. The total number of comparisons is the sum of
the first 𝑛 − 1 integers. Recall that the sum of the first 𝑛 integers is 1/2n^2 + 1/2n. The sum of the first 𝑛 − 1
integers is 1/2n^2 + 1/2n - n , which is 1/2n^2 - 1/2n . This is still 𝑂(𝑛^2) comparisons. In the best case,
if the list is already ordered, no exchanges will be made. However, in the worst case, every
comparison will cause an exchange. On average, we exchange half of the time.

> A bubble sort is often considered the most inefficient sorting method since it must exchange
items before the final location is known. These “wasted” exchange operations are very costly.

However, because the bubble sort makes passes through the entire unsorted portion of the list, it has the capability
to do something most sorting algorithms cannot. In particular, *if during
a pass there are no exchanges, then we know that the list must be sorted*. A bubble sort can
be modified to stop early if it finds that the list has become sorted. This means that *for lists
that require just a few passes, a bubble sort may have an advantage in that it will recognize the
sorted list and stop*.

#### Selection Sort

The selection sort improves on the bubble sort by making only one exchange for every pass
through the list. In order to do this, *a selection sort looks for the largest value as it makes a
pass and, after completing the pass, places it in the proper location*. As with a bubble sort, after
the first pass, the largest item is in the correct place. After the second pass, the next largest is
in place. This process continues and *requires 𝑛 − 1 passes to sort 𝑛 items*, since the final item
must be in place after the (𝑛 − 1)st pass.

You may see that the selection sort makes the same number of comparisons as the bubble sort
and is therefore also 𝑂(𝑛^2). However, due to the reduction in the number of exchanges, the
selection sort typically executes faster in benchmark studies (the constant value in Big O of selection sort is lower).
In fact, for our list, the bubble sort makes 20 exchanges, while the selection sort makes only 8.

#### The Insertion Sort

#### Shell Sort

#### The Merge Sort

We now turn our attention to using a *divide and conquer strategy* as a way to improve the
performance of sorting algorithms.  Merge sort is a *recursive algorithm that continually splits a list in half*. If
the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item,
we *split the list and recursively invoke a merge sort on both halves*. Once the two halves are sorted, the
fundamental operation, called a **merge**, is performed.

> Merging is the process of taking two
smaller sorted lists and combining them together into a single, sorted, new list

In order to analyze the merge_sort function, we need to consider the two distinct processes
that make up its implementation. First, the list is split into halves. We already computed (in a
binary search) that we can divide a list in half log 𝑛 times where 𝑛 is the length of the list. The
second process is the merge. Each item in the list will eventually be processed and placed on
the sorted list. So *the merge operation which results in a list of size 𝑛 requires 𝑛 operations*. The
result of this analysis is that *log 𝑛 splits, each of which costs 𝑛 for a total of 𝑛 log 𝑛 operations*.

> A merge sort is an **𝑂(𝑛 log 𝑛)** algorithm.

It is important to notice that the merge_sort function requires extra space to hold the two
halves as they are extracted with the slicing operations. This additional space can be a critical
factor if the list is large and can make this sort problematic when working on large data sets.

#### The Quick Sort

The quick sort uses divide and conquer to gain the same advantages as the merge sort, while
not using additional storage. As a trade-off, however, it is possible that the list may not be
divided in half. When this happens, we will see that performance is diminished

A quick sort first selects a value, which is called the **pivot value**. Although there are many
different ways to choose the pivot value, we will simply use the first item in the list. *The role
of the pivot value is to assist with splitting the list*. The *actual position where the pivot value
belongs in the final sorted list*, commonly called the **split point**, *will be used to divide the list
for subsequent calls to the quick sort*.

> The **partition** process  will find the split point and at the same
time move other items to the appropriate side of the list, either less than or greater than the
pivot value.

Partitioning begins by locating two position markers – let’s call them left_mark and
right_mark – at the beginning and end of the remaining items in the list. The goal of the partition
process is to move items that are on the wrong side
with respect to the pivot value while also converging on the split point

> We begin by incrementing left_mark until we locate a value that is greater than the pivot
value. We then decrement right_mark until we find a value that is less than the pivot value.

At this point we have discovered two items that are out of place with respect to the eventual
split point. Now we can exchange these two items and then repeat the process again.

> At the point where right_mark becomes less than left_mark, we stop. The position of
right_mark is now the split point. The pivot value can be exchanged with the contents of the
split point and the pivot value is now in place

In addition, all the items to the left
of the split point are less than the pivot value, and all the items to the right of the split point are
greater than the pivot value. The list can now be divided at the split point and the quick sort
can be invoked recursively on the two halves

To analyze the quick_sort function, note that for a list of length 𝑛, if the partition always
occurs in the middle of the list, there will again be log 𝑛 divisions. In order to find the split
point, each of the 𝑛 items needs to be checked against the pivot value. The result is 𝑛 log 𝑛. In
addition, *there is no need for additional memory* as in the merge sort process.

Unfortunately,* in the worst case, the split points may not be in the middle and can be very
skewed to the left or the right, leaving a very uneven division*. In this case, sorting a list of 𝑛
items divides into sorting a list of 0 items and a list of 𝑛 − 1 items. Then sorting a list of 𝑛 − 1
divides into a list of size 0 and a list of size 𝑛 − 2, and so on. The result is an 𝑂(𝑛^2) sort with
all of the overhead that recursion requires.

We mentioned earlier that there are different ways to choose the pivot value. In particular, we
can attempt to alleviate some of the potential for an uneven division by using a technique called
**median of three**. To choose the pivot value, we will consider the first, the middle, and the last
element in the list. In our example, those are 54, 77, and 20. Now pick the median value, in our
case 54, and use it for the pivot value (of course, that was the pivot value we used originally).
The idea is that in the case where the the first item in the list does not belong toward the middle
of the list, the median of three will choose a better “middle” value. This will be particularly
useful when the original list is somewhat sorted to begin with.

### Summary

• A sequential search is 𝑂(𝑛) for ordered and unordered lists.

• A binary search of an ordered list is 𝑂(log 𝑛) in the worst case.

• Hash tables can provide constant time searching.

• A bubble sort, a selection sort, and an insertion sort are 𝑂(𝑛^2) algorithms.

• A shell sort improves on the insertion sort by sorting incremental sublists. It falls between
𝑂(𝑛) and 𝑂(𝑛^2).

• A merge sort is 𝑂(𝑛 log 𝑛), but requires additional space for the merging process.

• A quick sort is 𝑂(𝑛 log 𝑛), but may degrade to 𝑂(𝑛^2) if the split points are not near the
middle of the list. It does not require additional space

