## Array-Based Sequences

The primary memory of a computer is composed of bits of information, and those bits are typically grouped into larger
units that depend upon the precise system architecture. Such a typical unit is a **byte**, which is equivalent to 8 bits

A computer system will have a huge number of bytes of memory, and to keep track of what information is stored in what
byte, the computer uses an abstraction known as a **memory address**. In effect, each byte of memory is associated with
a unique number that serves as its address (more formally, the binary representation of the number serves as the
address).

Memory addresses are typically coordinated with the physical layout of the memory system, and so we often portray the
numbers in sequential fashion. Despite the sequential nature of the numbering system, computer hardware is designed, in
theory, so that any byte of the main memory can be efficiently accessed based upon its memory address. In this sense, we
say that a computer’s main memory performs as **random access memory (RAM)**. That is, it is just as easy to retrieve
`byte#8675309` as it is to retrieve `byte#309`.

Using the notation for asymptotic analysis, we say that *any individual byte of memory can be stored or retrieved in
`O(1)` time.*

In general, a programming language keeps track of the association between an identifier and the memory address in which
the associated value is stored.

A group of related variables can be stored one after another in a contiguous portion of the computer’s memory. We will
denote such a representation as an **array**. As a tangible example, a text string is stored as an ordered sequence of
individual characters. In Python, each character is represented using the Unicode character set, and on most computing
systems, Python internally represents each Unicode character with 16 bits (i.e., 2 bytes).

We will refer to each location within an array as a cell, and will use an integer index to describe its location within
the array, with cells numbered starting with 0, 1, 2, and so on.

*Each cell of an array must use the same number of bytes*. This requirement is what allows an arbitrary cell of the
array to be accessed in constant time based on its index. In particular, if one knows the memory address at which an
array starts the number of bytes per element (e.g., 2 for a Unicode character), and a desired index within the array,
the appropriate memory address can be computed using the calculation, `start + cellsize*index`. By this formula, the
cell at index 0 begins precisely at the start of the array, the cell at index 1 begins precisely cellsize bytes beyond
the start of the array, and so on.

Consider an array like

        [ 'Rene' , 'Joseph' , 'Janet' , 'Jonas' , 'Helen' , 'Virginia' , ... ]

To represent such a list with an array, Python must adhere to the requirement that each cell of the array use the same
number of bytes. Yet the elements are strings, and strings naturally have different lengths.

Instead, Python represents a list or tuple instance using an internal storage mechanism of an array of **object
references**. At the lowest level, what is stored is a consecutive sequence of memory addresses at which the elements of
the sequence reside.

Although the relative size of the individual elements may vary, the number of bits used to store the memory address of
each element is fixed (e.g., 64-bits per address). In this way, Python can support constant-time access to a list or
tuple element based on its index.

The fact that lists and tuples are **referential structures** is significant to the semantics of these classes. A single
list instance may include multiple references to the same object as elements of the list, and it is possible for a
single object to be an element of two or more lists, as those lists simply store references back to that object. As an
example, when you compute a slice of a list, the result is a new list instance, but that new list has references to the
same elements that are in the original list,

When the elements of the list are immutable objects, the fact that the two lists share elements is not that significant,
as neither of the lists can cause a change to the shared object (we only can change the reference to a different
object )

The same semantics is demonstrated when making a new list as a **copy** of an existing one, with a syntax such as
`backup = list(primes)`. This produces a new list that is a **shallow copy** in that it references the same elements as
in the first list.

As a more striking example, it is a common practice in Python to initialize an array of integers using a syntax such as
`counters = [0] 8`. This syntax produces a list of length eight, with all eight elements being the value zero.
Technically, all eight cells of the list reference the *same object*.

At first glance, the extreme level of aliasing in this configuration may seem alarming. However, we rely on the fact
that the referenced integer is immutable. Even a command such as `counters[2] += 1` does not technically change the
value of the existing integer instance. This computes a new integer, with value `0+1`, and sets cell 2 to reference the
newly computed value

As a final manifestation of the referential nature of lists, we note that the extend command is used to add all elements
from one list to the end of another list. The extended list does not receive copies of those elements, it receives
references to those elements

#### Compact Arrays in Python

we emphasized that strings are represented using an array of characters (not an array of references). We will refer to
this more direct representation as a **compact array** because the array is storing the bits that represent the primary
data (characters, in the case of strings).

Compact arrays have several advantages over referential structures in terms of computing performance. Most
significantly, the overall memory usage will be much lower for a compact structure because there is no overhead devoted
to the explicit storage of the sequence of memory references (in addition to the primary data). That is, a referential
structure will typically use 64-bits for the memory address stored in the array, on top of whatever number of bits are
used to represent the object that is considered the element.

As another case study, suppose we wish to store a sequence of one million, 64-bit integers. In theory, we might hope to
use only 64 million bits. However, we estimate that a Python list *will use four to five times as much memory*. Each
element of the list will result in a 64-bit memory address being stored in the primary array, and an int instance being
stored elsewhere in memory.

Another important advantage to a compact structure for high-performance computing is that the primary data are stored
consecutively in memory. Note well that this is not the case for a referential structure. That is, even though a list
maintains careful ordering of the sequence of memory addresses, where those elements reside in memory is not determined
by the list. Because of the workings of the cache and memory hierarchies of computers, it is often advantageous to have
data stored in memory near other data that might be used in the same computations

Python provides several means for creating compact arrays of various types. Primary support for compact arrays is in a
module named `array`. That module defines a class, also named array, providing compact storage for arrays of primitive
data types.

the constructor for the `array` class requires a **type code** as a first parameter, which is a character that
designates the type of data that will be stored in the array.

        primes = array( i , [2, 3, 5, 7, 11, 13, 17, 19])

The array module does not provide support for making compact arrays of user-defined data types.

### Dynamic Arrays and Amortization

When creating a low-level array in a computer system, the precise size of that array must be explicitly declared in
order for the system to properly allocate a consecutive piece of memory for its storage.

Because the system might dedicate neighboring memory locations to store other data, the capacity of an array cannot
trivially be increased by expanding into subsequent cells. In the context of representing a Python `tuple` or `str`
instance, this constraint is no problem. Instances of those classes are immutable, so the correct size for an underlying
array can be fixed when the object is instantiated.

Although a list has a particular length when constructed, the class allows us to add elements to the list, with no
apparent limit on the overall capacity of the list. To provide this abstraction, Python relies on an algorithmic sleight
of hand known as a **dynamic array**

The first key to providing the semantics of a dynamic array is that a list instance maintains an underlying array that
often has greater capacity than the current length of the list. If a user continues to append elements to a list, any
reserved capacity will eventually be exhausted. In that case, the class requests a new, larger array from the system,
and initializes the new array so that its prefix matches that of the existing smaller array. At that point in time, the
old array is no longer needed, so it is reclaimed by the system.

#### Implementing a dynamic array

Although the Python list class provides a highly optimized implementation of dynamic arrays, it is instructive to see
how such a class might be implemented.

If an element is appended to a list at a time when the underlying array is full, we perform the following steps:

1. Allocate a new array B with larger capacity.
2. Set `B[i] = A[i], for i = 0,...,n−1,` where n denotes current number of items.
3. Set `A = B`, that is, we henceforth use B as the array supporting the list.
4. Insert the new element in the new array.

The remaining issue to consider is how large of a new array to create. A commonly used rule is for the new array to have
twice the capacity of the existing array that has been filled.

#### Performance analysis

The strategy of replacing an array with a new, larger array might at first seem slow, because a single append operation
may require Ω(n) time to perform, where n is the current number of elements in the array. However, notice that by
doubling the capacity during an array replacement, our new array allows us to add n new elements before the array must
be replaced again. In this way, there are many simple append operations for each expensive one. This fact allows us to
show that performing a series of operations on an initially empty dynamic array is efficient in terms of its total
running time.

Using an algorithmic design pattern called **amortization**, we can show that performing a sequence of such append
operations on a dynamic array is actually quite efficient.

> **Proposition:** Let S be a sequence implemented by means of a dynamic array with initial capacity one, using the
> strategy of doubling the array size when full. The total time to perform a series of n append operations in S,
> starting from S being empty, is O(n).

the O(1) amortized bound per operation can be proven for any geometrically increasing progression of array sizes (not
only for doubling). When choosing the geometric base, there exists a tradeoff between run-time efficiency and memory
usage. With a base of 2 (i.e., doubling the array), if the last insertion causes a resize event, the array essentially
ends up twice as large as it needs to be. If we instead increase the array by only 25% of its current size (i.e., a
geometric base of 1.25), we do not risk wasting as much memory in the end, but there will be more intermediate resize
events along the way.

**Memory Usage and Shrinking an Array.**

Another consequence of the rule of a geometric increase in capacity when appending to a dynamic array is that the final
array size is guaranteed to be proportional to the overall number of elements. That is, the data structure uses O(n)
memory. This is a very desirable property for a data structure.

If a container, such as a Python list, provides operations that cause the removal of one or more elements, greater care
must be taken to ensure that a dynamic array guarantees O(n) memory usage. The risk is that repeated insertions may
cause the underlying array to grow arbitrarily large, and that there will no longer be a proportional relationship
between the actual number of elements and the array capacity after many elements are removed.

A robust implementation of such a data structure will shrink the underlying array, on occasion, while maintaining
the `O(1)` amortized bound on individual operations. However, care must be taken to ensure that the structure cannot
rapidly oscillate between growing and shrinking the underlying array, in which case the amortized bound would not be
achieved

### Efficiency of Python’s Sequence Types

Python’s list class uses a form of dynamic arrays for its storage. Yet, a careful examination of the intermediate array
capacities suggests that Python is not using a pure geometric progression, nor is it using an arithmetic progression.

We note that tuples are typically more memory efficient than lists because they are immutable; therefore, there is no
need for an underlying dynamic array with surplus capacity.

**Searching for Occurrences of a Value.** Each of the count, index, and contains methods proceed through iteration of
the sequence from left to right. Notably, the loop for computing the count must proceed through the entire sequence,
while the loops for checking containment of an element or determining the index of an element immediately exit once they
find the leftmost occurrence of the desired value, if one exists. So while count always examines the n elements of the
sequence, index and contains examine n elements in the worst case, but may be faster.

**Lexicographic Comparisons.** Comparisons between two sequences are defined lexicographically. In the worst case,
evaluating such a condition requires an iteration taking time proportional to the length of the shorter of the two
sequences (because when one sequence ends, the lexicographic result can be determined). However, in some cases the
result of the test can be evaluated more efficiently. For example, if evaluating `[7, 3, ...] < [7, 5, ...]`, it is
clear that the result is True without examining the remainders of those lists, because the second element of the left
operand is strictly less than the second element of the right operand

There are several syntaxes for constructing new lists. In almost all cases, the asymptotic efficiency of the behavior is
linear in the length of the list that is created. However, as with the case in the preceding discussion of extend vs
calling append many times, there are significant differences in the practical efficiency.

Experiments should show that the list comprehension syntax is significantly faster than building the list by repeatedly
appending. Similarly, it is a common Python idiom to initialize a list of constant values using the multiplication
operator, as in `[0]*n` to produce a list of length n with all values equal to zero. Not only is this succinct for the
programmer; it is more efficient than building such a list incrementally.

#### Python’s String Class

The analysis for many behaviors is quite intuitive. For example, methods that produce a new string (e.g., capitalize,
center, strip) require time that is linear in the length of the string that is produced. Many of the behaviors that test
Boolean conditions of a string (e.g., islower) take O(n)time, examining all n characters in the worst case, but short
circuiting as soon as the answer becomes evident (e.g., islower can immediately return False if the first character is
uppercased). The comparison operators (e.g., ==, <) fall into this category as well

**Pattern Matching.** (chapter 13)

**Pattern Matching.** Finally, we wish to comment on several approaches for composing large strings. It may be tempting
to compose a result through repeated concatenation, as follows.

    # WARNING: do not do this
    letters = # start with empty string
    for c in document:
        if c.isalpha( ):
            letters += c # concatenate alphabetic character

While the preceding code fragment accomplishes the goal, it may be terribly inefficient. Because strings are immutable,
the command, letters += c, would presumably compute the concatenation, letters + c, as a new string instance and then
reassign the identifier, letters, to that result. Constructing that new string would require time proportional to its
length. If the final result has n characters, the series of concatenations would take time proportional to the familiar
sum 1+ 2+ 3+···+n, and therefore O(n^2) time.

The optimization is as follows. The reason that a command, letters += c, causes a new string instance to be created is
that the original string must be left unchanged if another variable in a program refers to that string. On the other
hand, if Python knew that there were no other references to the string in question, it could implement += more
efficiently by directly mutating the string (as a dynamic array). As it happens, the Python interpreter already
maintains what are known as **reference counts** for each object; this count is used in part to determine if an object
can be garbage collected. But in this context, it provides a means to detect when no other references exist to a string,
thereby allowing the optimization.

A more standard Python idiom to guarantee linear time composition of a string is to use a temporary list to store
individual pieces, and then to rely on the join method of the str class to compose the final result.

    temp = [ ]                  # start with empty list
    for c in document:
        if c.isalpha( ):
            temp.append(c)      # append alphabetic character
    letters = .join(temp)       # compose overall result

This approach is guaranteed to run in O(n) time. First, we note that the series of up to n append calls will require a
total of O(n) time, as per the definition of the amortized cost of that operation. The final call to join also
guarantees that it takes time that is linear in the final length of the composed string.

we can further improve the practical execution time by using a list comprehension syntax to build up the temporary list,
rather than by repeated calls to append. That solution appears as,

    letters = .join([c for c in document if c.isalpha( )])

Better yet, we can entirely avoid the temporary list with a generator comprehension:

    letters = .join(c for c in document if c.isalpha( ))


### Using Array-Based Sequences

