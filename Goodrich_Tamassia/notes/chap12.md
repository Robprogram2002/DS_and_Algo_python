# Sorting and Selection

Given a collection, the goal is to rearrange the elements so that they are ordered from smallest to largest (or to
produce a new copy of the sequence with such an order). As we did when studying priority queues, we assume that such a
consistent order exists.

Sorting is among the most important, and well studied, of computing problems. Many advanced algorithms for a variety of
problems rely on sorting as a subroutine.

Python has built-in support for sorting data, in the form of the `sort` method of the list class that rearranges the
contents of a list, and the built-in `sorted` function that produces a new list containing the elements of an arbitrary
collection in sorted order. Those built-in functions use advanced algorithms (some of which we will describe in this
chapter), and they are highly optimized. A programmer should typically rely on calls to the built-in sorting functions,

when calling the built-in function, it is good to know what to expect in terms of efficiency and how that may depend
upon the initial order of elements or the type of objects that are being sorted. More generally, the ideas and
approaches that have led to advances in the development of sorting algorithm carry over to algorithm development in many
other areas of computing.

## Merge-Sort

### Divide-and-Conquer

The first two algorithms we describe use recursion in an algorithmic design pattern called **divide-and-conquer** that
consists of the following three steps:

1. **Divide:** If the input size is smaller than a certain threshold (say, one or two elements), solve the problem
   directly using a straightforward method and return the solution so obtained. Otherwise, divide the input data into
   two or more disjoint subsets.
2. **Conquer:** Recursively solve the subproblems associated with the subsets.
3. **Combine:** Take the solutions to the subproblems and merge them into a solution to the original problem.

We will first describe the merge-sort algorithm at a high level. To sort a sequence S with n elements using the three
divide-and-conquer steps, the merge-sort algorithm proceeds as follows:

1. Divide: If S has zero or one element, return S immediately; it is already sorted. Other-wise (S has at least two
   elements), remove all the elements from S and put them into two sequences, S1 and S2, each containing about half of
   the elements of S;that is, S1 contains the first |n/2| elements of S, and S2 contains the remaining |n/2| elements.
2. Conquer: Recursively sort sequences S1 and S2.
3. Combine: Put back the elements into S by merging the sorted sequences S1 and S2 into a sorted sequence.

We can visualize an execution of the merge-sort algorithm by means of a binary tree T, called the **merge-sort tree**.
Each node of T represents a recursive invocation (or call) of the merge-sort algorithm. We associate with each node v of
T the sequence S that is processed by the invocation associated with v. The children of node v are associated with the
recursive calls that process the subsequences S1 and S2 of S. The external nodes of T are associated with individual
elements of S, corresponding to instances of the algorithm that make no recursive calls.

This algorithm visualization in terms of the merge-sort tree helps us analyze the running time of the merge-sort
algorithm. In particular, since the size of the input sequence roughly halves at each recursive call of merge-sort, the
height of the merge-sort tree is about logn (recall that the base of log is 2 if omitted).

### Array-Based Implementation of Merge-Sort

The merge function is responsible for the subtask of merging two previously sorted sequences, S1 and S2, with the output
copied into S. We copy one element during each pass of the while loop, conditionally determining whether the next
element should be taken from S1 or S2. If we reach the end of one of the sequences, we must copy the next element from
the other.

### The Running Time of Merge-Sort

We begin by analyzing the running time of the merge algorithm. Let n1 and n2 be the number of elements of S1 and S2,
respectively. It is clear that the operations performed inside each pass of the while loop take O(1) time. The key
observation is that during each iteration of the loop, one element is copied from either S1 or S2 into S (and that
element is considered no further). Therefore, the number of iterations of the loop is n1 +n2. Thus, the running time of
algorithm merge is O(n1 +n2).

Having analyzed the running time of the merge algorithm used to combine subproblems, let us analyze the running time of
the entire merge-sort algorithm, assuming it is given an input sequence of n elements.In the case of our merge sort
function, we account for the time to divide the sequence into two subsequences, and the call to merge to combine the two
sorted sequences, but we exclude the two recursive calls to merge sort.

> **Proposition :** Algorithm merge-sort sorts a sequence S of size n in O(nlogn) time, assuming two elements of S can be
> compared in O(1) time.

### Alternative Implementations of Merge-Sort

The merge-sort algorithm can easily be adapted to use any form of a basic queue as its container type. we provide such
an implementation, based on use of the LinkedQueue class. The O(nlogn) bound for merge-sort applies to this
implementation as well, since each basic operation runs in O(1) time when implemented with a linked list.

### A Bottom-Up (Nonrecursive) Merge-Sort

There is a nonrecursive version of array-based merge-sort, which runs in O(nlogn) time. It is a bit faster than
recursive merge-sort in practice, as it avoids the extra overheads of recursive calls and temporary memory at each
level. The main idea is to perform merge-sort bottom-up, performing the merges level by level going up the merge-sort
tree.

Given an input array of elements, we begin by merging every successive pair of elements into sorted runs of length two.
We merge these runs into runs of length four, merge these new runs into runs of length eight, and so on, until the array
is sorted. To keep the space usage reasonable, we deploy a second array that stores the merged runs (swapping input and
output arrays after each iteration).

A similar bottom-up approach can be used for sorting linked lists.

## Quick-Sort

Like merge-sort, this algorithm is also based on the divide-and-conquer paradigm, but it uses this technique in a
somewhat opposite manner, as all the hard work is done **before** the recursive calls.

The main idea is to apply the divide-and-conquer technique, whereby we divide S into subsequences, recur to sort each
subsequence, and then combine the sorted subsequences by a simple concatenation. In particular, the quick-sort algorithm
consists of the following three steps.

1. Divide: If S has at least two elements (nothing needs to be done if S has zero or one element), select a specific
   element x from S, which is called the **pivot**. As is common practice, choose the pivot x to be the last element in
   S. Remove all the elements from S and put them into three sequences:
    * L, storing the elements in S less than x
    * E, storing the elements in S equal to x
    * G, storing the elements in S greater than x Of course, if the elements of S are distinct, then E holds just one
      element— the pivot itself.
2. Conquer: Recursively sort sequences L and G.
3. Combine: Put back the elements into S in order by first inserting the elements of L, then those of E, and finally
   those of G.

the execution of quick-sort can be visualized by means of a binary recursion tree, called the **quick-sort tree**.

Unlike merge-sort, however, the height of the quick-sort tree associated with an execution of quick-sort is linear in
the worst case. This happens, for example, if the sequence consists of n distinct elements and is already sorted.
Indeed, in this case, the standard choice of the last element as pivot yields a subsequence L of size n−1, while
subsequence E has size 1 and subsequence G has size 0. At each invocation of quick-sort on subsequence L, the size
decreases by 1. Hence, the height of the quick-sort tree is n−1.

We can analyze the running time of quick-sort with the same technique used for merge-sort. Namely, we can identify the
time spent at each node of the quick-sort tree T and sum up the running times for all the nodes.

we see that the divide step and the final concatenation of quick-sort can be implemented in linear time. Thus, the time
spent at a node v of T is proportional to the input size s(v) of v, defined as the size of the sequence handled by the
invocation of quick-sort associated with node v.Since subsequence E has at least one element (the pivot), the sum of the
input sizes of the children of v is at most s(v)−1.

We can therefore bound the overall running time of an execution of quick-sort as O(n · h) where h is the overall height
of the quick-sort tree T for that execution. Unfortunately, in the worst case, the height of a quick-sort tree is Θ(n).
Thus, quick-sort runs in O(n^2) worst-case time. Paradoxically, if we choose the pivot as the last element of the
sequence, this worst-case behavior occurs for problem instances when sorting should be easy—if the sequence is already
sorted.

The best case for quick-sort on a sequence of distinct elements occurs when subsequences L and G have roughly the same
size. In that case, as we saw with merge-sort, the tree has height O(logn) and therefore quick-sort runs in O(nlogn)
time. More so, we can observe an O(nlogn) running time even if the split between L and G is not as perfect. For example,
if every divide step caused one subsequence to have one-fourth of those elements and the other to have three-fourths of
the elements, the height of the tree would remain O(logn) and thus the overall performance O(nlogn).

We will see in the next section that introducing randomization in the choice of a pivot will makes quick-sort
essentially behave in this way on average, with an expected running time that is O(nlogn).

### Randomized Quick-Sort

One common method for analyzing quick-sort is to assume that the pivot will always divide the sequence in a reasonably
balanced manner. We feel such an assumption would presuppose knowledge about the input distribution that is typically
not available, however. In general, we desire some way of getting close to the best-case running time for quick-sort.
The way to get close to the best-case running time, of course, is for the pivot to divide the input sequence S almost
equally. If this outcome were to occur, then it would result in a running time that is asymptotically the same as the
best-case running time. That is, having pivots close to the “middle” of the set of elements leads to an O(nlogn) running
time for quick-sort.

let us introduce randomization into the algorithm and pick as the pivot a random element of the input sequence. That is,
instead of picking the pivot as the first or last element of S, we pick an element of S at random as the pivot, keeping
the rest of the algorithm unchanged. This variation of quick-sort is called **randomized quick-sort**. The following
proposition shows that the expected running time of randomized quick-sort on a sequence with n elements is O(nlogn).
This expectation is taken over all the possible random choices the algorithm makes, and is independent of any
assumptions about the distribution of the possible input sequences the algorithm is likely to be given.

> **Proposition :** The expected running time of randomized quick-sort on a sequence S of size n is O(nlogn).

### Additional Optimizations for Quick-Sort

An algorithm is in-place if it uses only a small amount of memory in addition to that needed for the original input.
Quick-sort of an array-based sequence can be adapted to be in-place, and such an optimization is used in most deployed
implementations.

Performing the quick-sort algorithm in-place requires a bit of ingenuity, however, for we must use the input sequence
itself to store the subsequences for all the recursive calls.

Our implementation assumes that the input sequence, S, is given as a Python list of elements. In-place quick-sort
modifies the input sequence using element swapping and does not explicitly create subsequences. Instead, a subsequence
of the input sequence is implicitly represented by a range of positions specified by a leftmost index a and a rightmost
index b.

The divide step is performed by scanning the array simultaneously using local variables left, which advances forward,
and right, which advances backward, swapping pairs of elements that are in reverse order. When these two indices pass
each other, the division step is complete and the algorithm completes by recurring on these two sublists. There is no
explicit “combine” step, because the concatenation of the two sublists is implicit to the in-place use of the original
list.

It is worth noting that if a sequence has duplicate values, we are not explicitly creating three sublists L, E,and G, as
in our original quick-sort description. We instead allow elements equal to the pivot (other than the pivot itself) to be
dispersed across the two sublists.

Although the implementation we describe in this section for dividing the sequence into two pieces is in-place, we note
that the complete quick-sort algorithm needs space for a stack proportional to the depth of the recursion tree, which in
this case can be as large as n−1. Admittedly, the expected stack depth is O(logn), which is small compared to n.
Nevertheless, a simple trick lets us guarantee the stack size is O(logn). The main idea is to design a nonrecursive
version of in-place quick-sort using an explicit stack to iteratively process subproblems (each of which can be
represented with a pair of indices marking subarray boundaries).

Each iteration involves popping the top subproblem, splitting it in two (if it is big enough), and pushing the two new
subproblems. The trick is that when pushing the new subproblems, we should first push the larger subproblem and then the
smaller one. In this way, the sizes of the subproblems will at least double as we go down the stack; hence, the stack
can have depth at most O(logn).

**Pivot Selection**

Our implementation in this section blindly picks the last element as the pivot at each level of the quick-sort
recursion. This leaves it susceptible to the Θ(n2)-time worst case.

this can be improved upon by using a randomly chosen pivot for each partition step. In practice, another common
technique for choosing a pivot is to use the median of tree values, taken respectively from the front, middle, and tail
of the array. This **median-of-three** heuristic will more often choose a good pivot and computing a median of three may
require lower overhead than selecting a pivot with a random number generator. For larger data sets, the median of more
than three potential pivots might be computed.

### Hybrid Approaches

Although quick-sort has very good performance on large data sets, it has rather high overhead on relatively small data
sets. In practice, a simple algorithm like insertion-sort will execute faster when sorting such a short sequence.

It is therefore common, in optimized sorting implementations, to use a hybrid approach, with a divide-and-conquer
algorithm used until the size of a subsequence falls below some threshold (perhaps 50 elements); insertion-sort can be
directly invoked upon portions with length below the threshold.

## Studying Sorting through an Algorithmic Lens

A natural first question to ask is whether we can sort any faster than O(nlogn) time. Interestingly, if the
computational primitive used by a sorting algorithm is the comparison of two elements, this is in fact the best we can
do—comparison-based sorting has an Ω(nlogn) worst-case lower bound on its running time.

> **Proposition :** The running timeofanycomparison-based algorithm for sorting an n-element sequence isΩ(nlogn) in the
> worst case.

## Linear-Time Sorting: Bucket-Sort and Radix-Sort

A natural question to ask, then, is whether there are other kinds of sorting algorithms that can be designed to run
asymptotically faster than O(nlogn) time. Interestingly, such algorithms exist, but they require special assumptions
about the input sequence to be sorted. Even so, such scenarios often arise in practice, such as when sorting integers
from a known range or sorting character strings, so discussing them is worthwhile. In this section, we consider the
problem of sorting a sequence of entries, each a key-value pair, where the keys have a restricted type.

### Bucket-Sort

Consider a sequence S of n entries whose keys are integers in the range [0,N−1], for some integer N ≥ 2, and suppose
that S should be sorted according to the keys of the entries. In this case, it is possible to sort S in O(n+N) time. It
might seem surprising, but this implies, for example, that if N is O(n), then we can sort S in O(n) time. Of course, the
crucial point is that, because of the restrictive assumption about the format of the elements, we can avoid using
comparisons.

The main idea is to use an algorithm called **bucket-sort**, which is not based on comparisons, but on using keys as
indices into a bucket array B that has cells indexed from 0 to N−1. An entry with key k is placed in the “bucket” B[k]
,which itself is a sequence (of entries with key k). After inserting each entry of the input sequence S into its bucket,
we can put the entries back into S in sorted order by enumerating the contents of the buckets B[0],B[1],... ,B[N−1] in
order.

      Algorithm bucketSort(S): 
         Input: Sequence S of entries with integer keys in the range [0,N−1] 
         Output: Sequence S sorted in nondecreasing order of the keys 
         
         let B be an array of N sequences, each of which is initially empty 
         
         for each entry e in S do 
            k = the key of e 
            remove e from S and insert it at the end of bucket (sequence) B[k]
         for i = 0 to N−1 do 
            for each entry e in sequence B[i] do 
               remove e from B[i] and insert it at the end of S

It is easy to see that bucket-sort runs in O(n +N) time and uses O(n+N) space. Hence, bucket-sort is efficient when the
range N of values for the keys is small compared to the sequence size n, say N = O(n) or N = O(nlogn). Still, its
performance deteriorates as N grows compared to n.

An important property of the bucket-sort algorithm is that it works correctly even if there are many different elements
with the same key. Indeed, we described it in a way that anticipates such occurrences.

#### Stable Sorting

We say that a sorting algorithm is **stable** if, for any two entries (ki,vi) and (kj,v j) of S such that ki = kj and (
ki,vi) precedes (kj,v j) in S before sorting (that is, i < j), entry (ki,vi) also precedes entry (kj,v j) after sorting.
Stability is important for a sorting algorithm because applications may want to preserve the initial order of elements
with the same key.

Our informal description of bucket-sort guarantees stability as long as we ensure that all sequences act as queues, with
elements processed and removed from the front of a sequence and inserted at the back. That is, when initially placing
elements of S into buckets, we should process S from front to back, and add each element to the end of its bucket.
Subsequently, when transferring elements from the buckets back to S, we should process each B[i] from front to back,
with those elements added to the end of S.

### Radix-Sort

One of the reasons that stable sorting is so important is that it allows the bucket-sort approach to be applied to more
general contexts than to sort integers. Suppose, for example, that we want to sort entries with keys that are pairs (k,
l),where k and l are integers in the range [0,N−1], for some integer N≥ 2. In a context such as this, it is common to
define an order on these keys using the **lexicographic** (dictionary) convention, where (k1, l1) < (k2, l2) if k1 <k2
or if k1 = k2 and l1 < l2. This is a pairwise version of the lexicographic comparison function, which can be applied to
equal-length character strings, or to tuples of length d.

> The **radix-sort** algorithm sorts a sequence S of entries with keys that are pairs, by applying a stable bucket-sort on
> the sequence twice; first using one component of the pair as the key when ordering and then using the second component.

By first stably sorting by the second component and then again by the first component, we guarantee that if two entries
are equal in the second sort (by the first component), then their relative order in the starting sequence (which is
sorted by the second component) is preserved. Thus, the resulting sequence is guaranteed to be sorted lexicographically
every time

> **Proposition :** Let S be a sequence ofn key-value pairs, each of which has a key (k1,k2,... ,kd),where ki is an
> integer in the range [0,N−1] for some integer N≥ 2. We can sort S lexicographically in timeO(d(n+N)) using radix-sort.

Radix sort can be applied to any key that can be viewed as a composite of smaller pieces that are to be sorted
lexicographically.

## Comparing Sorting Algorithms

We have studied several methods, such as insertion-sort, and selection-sort, that have O(n2)-time behavior in the
average and worst case. We have also studied several methods with O(nlogn)-time behavior, including heap-sort,
merge-sort, and quick-sort. Finally, the bucket-sort and radix-sort methods run in linear time for certain types of
keys.

there is no clear “best” sorting algorithm from the remaining candidates. There are trade-offs involving efficiency,
memory usage, and stability. The sorting algorithm best suited for a particular application depends on the properties of
that application.

**Insertion-Sort :** If implemented well, the running time of insertion-sort is O(n+m),where m is the number of
inversions (that is, the number of pairs of elements out of order). Thus, insertion-sort is an excellent algorithm for
sorting small sequences (say, less than 50 elements), because insertion-sort is simple to program, and small sequences
necessarily have few inversions. Also, insertion-sort is quite effective for sorting sequences that are already “almost”
sorted. By “almost,” we mean that the number of inversions is small. But outside these cases is a poor choice

**Heap-Sort :** runs in O(nlogn) time in the worst case, which is optimal for comparison-based sorting methods.
Heap-sort can easily be made to execute in-place, and is a natural choice on small- and medium-sized sequences, when
input data can fit into main memory. However, heap-sort tends to be outperformed by both quick-sort and merge-sort on
larger sequences. A standard heap-sort does not provide a stable sort, because of the swapping of elements

**Quick-Sort :** we expect its performance to be O(nlogn)-time, and experimental studies have shown that it outperforms
both heap-sort and merge-sort on many tests. Quick-sort does not naturally provide a stable sort, due to the swapping of
elements during the partitioning step. For decades quick-sort was the default choice for a general-purpose, in-memory
sorting algorithm

**Merge-Sort :** runs in O(nlogn) time in the worst case. It is quite difficult to make merge-sort run in-place for
arrays, and without that optimization the extra overhead of allocate a temporary array, and copying between the arrays
is less attractive than in-place implementations of heap-sort and quick-sort for sequences that can fit entirely in a
computer’s main memory.

Since 2003, the standard sort method of Python’s list class has been a hybrid approach named **Tim-sort** (designed by
Tim Peters), which is essentially a bottom-up merge-sort that takes advantage of some initial runs in the data while
using insertion-sort to build additional runs. Tim-sort has also become the default algorithm for sorting arrays in
Java7.

**Bucket-Sort and Radix-Sort :** if an application involves sorting entries with small integer keys, character strings,
or d-tuples of keys from a discrete range, then bucket-sort or radix-sort is an excellent choice, for it runs in O(d(
n+N)) time, where [0,N−1] is the range of integer keys (and d = 1 for bucket sort). Thus, if d(n+N) is significantly
“below” the nlogn function, then this sorting method should run faster than even quick-sort, heap-sort, or merge-sort.

## Python’s Built-In Sorting Functions

There are many situations in which we wish to sort a list of elements, but according to some order other than the
natural order defined by the < operator. For example, we might wish to sort a list of strings from shortest to longest (
rather than alphabetically). Both of Python’s built-in sort functions allow a caller to control the notion of order that
is used when sorting. This is accomplished by providing, as an optional keyword parameter, a reference to a secondary
function that computes a key for each element of the primary sequence; then the primary elements are sorted based on the
natural order of their keys.

A key function must be a one-parameter function that accepts an element as a parameter and returns a key. For example,
we could use the built-in len function when sorting strings by length, as a call len(s) for string s returns its length.
To sort our colors list based on length, we use the syntax `colors.sort(key=len)` to mutate the list
or `sorted(colors, key=len)` to generate a new ordered list, while leaving the original alone

These built-in functions also support a keyword parameter, reverse, that can be set to True to cause the sort order to
be from largest to smallest.

Python’s support for a key function when sorting is implemented using what is known as the **decorate-sort-undecorate
design pattern**. It proceeds in 3 steps:

1. Each element of the list is temporarily replaced with a “decorated” version that includes the result of the key
   function applied to the element.
2. The list is sorted based upon the natural order of the keys .
3. The decorated elements are replaced by the original elements.

Although there is already built-in support for Python, if we were to implement such a strategy ourselves, a natural way
to represent a “decorated” element is using the same composition strategy that we used for representing key-value pairs
within a priority queue. With such a composition, we could trivially adapt any sorting algorithm to use the
decorate-sort-undecorate pattern.

## Selection

There are a number of applications in which we are interested in identifying a single element in terms of its rank
relative to the sorted order of the entire set like the minimum, maximum and the median.

> In general, queries that ask for an element with a given rank are called **order statistics**.

we discuss the general order-statistic problem of selecting the kth smallest element from an unsorted collection of n
comparable elements. This is known as the **selection problem**.

Of course, we can solve this problem by sorting the collection and then indexing into the sorted sequence at index `k−1`
Using the best comparison-based sorting algorithms, this approach would take O(nlogn) time, which is obviously an
overkill for the cases where k = 1or k = n (or even k = 2, k = 3, k = n−1, or k = n−5), because we can easily solve the
selection problem for these values of k in O(n) time. Thus, a natural question to ask is whether we can achieve an O(n)
running time for all values of k.

### Prune-and-Search

We can indeed solve the selection problem in O(n) time for any value of k.Moreover, the technique we use to achieve this
result involves an interesting algorithmic design pattern. This design pattern is known as **prune-and-search** or
**decreaseand-conquer**.

In applying this design pattern, we solve a given problem that is defined on a collection of n objects by pruning away a
fraction of the n objects and recursively solving the smaller problem. When we have finally reduced the problem to one
defined on a constant-sized collection of objects, we then solve the problem using some brute-force method. Returning
back from all the recursive calls completes the construction. In some cases, we can avoid using recursion, in which case
we simply iterate the prune-and-search reduction step until we can apply a brute-force method and stop.

Incidentally, the binary search method is an example of the prune-and-search design pattern.

### Randomized Quick-Select

This algorithm runs in O(n) **expected** time, taken over all possible random choices made by the algorithm; this
expectation does not depend whatsoever on any randomness assumptions about the input distribution. We note though that
randomized quick-select runs in O(n2) time in the **worst case**,

Suppose we are given an unsorted sequence S of n comparable elements together with an integer k ∈ [1,n]. At a high
level, the quick-select algorithm for finding the kth smallest element in S is similar to the randomized quick-sort
algorithm.

We pick a “pivot” element from S at random and use this to subdivide S into three subsequences L, E,and G, storing the
elements of S less than, equal to, and greater than the pivot, respectively. In the prune step, we determine which of
these subsets contains the desired element, based on the value of k and the sizes of those subsets. We then recur on the
appropriate subset, noting that the desired element’s rank in the subset may differ from its rank in the full set.

> **Proposition :** The expected running time of randomized quick-select on a sequence S ofsize n isO(n), assuming two
> elements ofS can be compared inO(1) time.

