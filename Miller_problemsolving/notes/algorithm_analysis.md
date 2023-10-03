## ALGORITHM ANALYSIS

An interesting question often arises. When two programs solve the same problem but look different, is one program better
than the other?

We need to remember that there is an important difference between a program and the underlying algorithm that the
program is representing. an algorithm is a generic, step-by-step list of instructions for solving a problem. It is a
method for solving any instance of the problem such that given a particular input, the algorithm produces the desired
result. A program, on the other hand, is an algorithm that has been encoded into some programming language. There may be
many programs for the same algorithm, depending on the programmer and the programming language being used.

Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each
algorithm uses. We want to be able to consider two algorithms and say that one is better than the other because it is
more efficient in its use of those resources or perhaps because it simply uses fewer

it is important to think more about what we really mean by computing resources. There are two different ways to look at
this.

One way is to consider the amount of space or memory an algorithm requires to solve the problem. The amount of space
required by a problem solution is typically dictated by the problem instance itself. Every so often, however, there are
algorithms that have very specific space requirements

we can analyze and compare algorithms based on the amount of time they require to execute. This measure is sometimes
referred to as the “execution time” or “running time” of the algorithm. (benchmark analysis)
We need a better way to characterize these algorithms with respect to execution time.

The benchmark technique computes the actual time to execute. It does not really provide us with a useful measurement,
because it is dependent on a particular machine, program, time of day, compiler, and programming language. Instead, we
would like to have a characterization that is independent of the program or computer being used. This measure would then
be useful for judging the algorithm alone and could be used to compare algorithms across implementations.

### Big-O notation

When trying to characterize an algorithm’s efficiency in terms of execution time. If each of these steps is considered
to be a basic unit of computation, then the execution time for an algorithm can be expressed as the number of steps
required to solve the problem

> Deciding on an appropriate basic unit of computation can be a complicated problem and will depend on how the algorithm is implemented

We can denote this by a function, call it T. 𝑇(𝑛) is the time it takes to solve a problem of size n. The parameter 𝑛
is often referred to as the “size of the problem,”

We can then say that the sum of the first 100, 000 integers is a bigger instance of the summation problem than the sum
of the first 1, 000. Because of this, it might seem reasonable that the time required to solve the larger case would be
greater than for the smaller case. Our goal then is to show how the algorithm’s execution time changes with respect to
the size of the problem

We can take one step further. It turns out that the exact number of operations is not as important as determining the
most dominant part of the 𝑇(𝑛) function. In other words, as the problem gets larger, some portion of the 𝑇(𝑛)
function tends to overpower the rest. This dominant term is what, in the end, is used for comparison

The **order of magnitude** function describes *the part of 𝑇(𝑛) that increases the fastest as the value of 𝑛
increases*. Order of magnitude is often called **Big-O notation** (for “order”) and written as
**𝑂(𝑓(𝑛))**. It provides a useful approximation to the actual number of steps in the computation.
*The function 𝑓(𝑛) provides a simple representation of the dominant part of the original 𝑇(𝑛)*

**EXAMPLE :**
Suppose that for some algorithm, the exact number of steps is **𝑇(𝑛) = 5𝑛^2 + 27𝑛 + 1005**. When 𝑛 is small, say 1
or 2, the constant 1005 seems to be the dominant part of the function. However, as 𝑛 gets larger, the 𝑛^2 term becomes
the most important. In fact, when 𝑛 is really large, the other two terms become insignificant in the role that they
play in determining the final result. Again, to approximate 𝑇(𝑛) as 𝑛 gets large, we can ignore the other terms and
focus on 5n^2 In addition, the coefficient 5 becomes insignificant as 𝑛 gets large. We would say then that the function
𝑇(𝑛) has an order of magnitude **𝑓(𝑛) = 𝑛^2**, or simply that it is **𝑂(𝑛2)**.

sometimes the performance of an algorithm depends on the exact values of the data rather than simply the size of the
problem. For these kinds of algorithms we need to characterize their performance in terms of **best case**,
**worst case**, or **average case** performance. The worst case performance refers to a particular data set where the
algorithm performs especially poorly. Whereas a different data set for the exact same algorithm might have
extraordinarily good performance. However, in most cases the algorithm performs somewhere in between these two
extremes (average case). It is important for a computer scientist to understand these distinctions so they are not
misled by one particular case

As a final example, suppose that we have the fragment of Python code shown below. a = 5 b = 6 c = 10 for i in range(n):
for j in range(n):
x = i * i y = j * j z = i * j for k in range(n):
w = a * k + 45 v = b * b d = 33

The number of assignment operations is the sum of four terms. The first term is the constant 3, representing the three
assignment statements at the start of the fragment. The second term is 3n^2, since there are three statements that are
performed n^2 times due to the nested iteration. The third term is 2𝑛, two statements iterated 𝑛 times. Finally, the
fourth term is the constant 1, representing the final assignment statement. This gives us 𝑇(𝑛) = 3 + 3n^2 + 2𝑛 + 1 =
3n^2 + 2𝑛 + 4.

By looking at the exponents, we can easily see that the 𝑛^2 term will be dominant and therefore this fragment of code
is 𝑂(n^2). Note that all of the other terms as well as the coefficient on the dominant term can be ignored as 𝑛 grows
larger

### Performance of Python Data Structure

Big-O performance for the operations on Python lists and dictionaries

##### Lists

The designers of Python had many choices to make when they implemented the list data structure. To help them make the
right choices they looked at the ways that people would most commonly use the list data structure and they optimized
their implementation of a list so that the most common operations were very fast.

Two common operations are indexing and assigning to an index position. Both of these operations take the same amount of
time no matter how large the list becomes. When an operation like this is independent of the size of the list they
are **𝑂(1)**. There are two ways to create a longer list. You can use the append method or the concatenation operator.
The append method is 𝑂(1). However, the concatenation operator is **𝑂(𝑘)** where 𝑘 is the *size of the list that is
being concatenated*.

Big-O efficiency of all the basic list operations

- Operation Big-O efficiency
- indexing O(1)
- index assignment O(1)
- append O(1)
- pop O(1)
- pop(i)                O(n)
- insert(i, item)       O(n)
- del operator O(n)
- iteration O(n)
- contains O(n)
- get slice[x:y]        O(k)
- set slice O(n+k)
- reverse O(n)
- concatenate O(k)
- sort O(nlogn)
- multiply O(nk)

##### Dictionaries

The thing that is most important to notice right now is that the get item and set item operations on a dictionary are
𝑂(1). Another important dictionary operation is the contains operation. Checking to see whether a key is in the
dictionary or not is also 𝑂(1)

- Operation Big-O efficiency
- copy O(n)
- get or set item O(1)
- delete item O(1)
- contains (in)         O(1)
- iteration O(n)

the efficiencies we provide in the table are for average performance

### Asymptotic Analysis in details

**The RAM Model of Computation :**

- Each “simple” operation (+, -, =, if, call) takes 1 step.
- Loops and subroutine calls are not simple operations. They depend upon the size of the data and the contents of a
  subroutine
- Each memory access takes exactly 1 step.

We measure the run time of an algorithm by counting the number of steps.

**Exact Analysis is Hard :** Get a function for Best, worst, and average are difficult to deal with precisely because
the details are very complicated. It's easier to talk about *upper and lower bounds* of the function.

- g(n) = O(f(n)) means C × f(n) is an upper bound on g(n).
- g(n) = Ω(f(n)) means C×f(n) is a lower bound on g(n).
- g(n) = Θ(f(n)) means C1 × f(n) is an upper bound on g(n) and C2 × f(n) is a lower bound on g(n).

C, C1, and C2 are all constants independent of n. The definitions imply a constant n0 *beyond which* they are satisfied.
We do not care about small values of n.

##### Formal definitions

- f(n) = O(g(n)) if there are positive constants n0 and c such that to the right of n0, the value of f(n) always lies on
  or below c · g(n).
- f(n) = Ω(g(n)) if there are positive constants n0 and c such that to the right of n0, the value of f(n) always lies on
  or above c · g(n).
- f(n) = Θ(g(n)) if there exist positive constants n0, c1, and c2 such that to the right of n0, the value of f(n) always
  lies between c1 · g(n) and c2 · g(n) inclusive.

> Think of the equality as meaning in the set of functions.

##### Academia vs Industry

Academics use big 0, big 0 (theta), and big O (omega) to describe runtimes.

**O (big 0):** In academia, big O describes an upper bound on the time. An algorithm that prints all the values in an
array could be described as O(N), but it could also be described as O(N2), O(N3), or 0( 2^N) (or many other big O times)
. The algorithm is at least as fast as each of these; therefore they are upper bounds on the runtime. This is similar to
a less-than-or-equal-to relationship

**Ω (big omega):** In academia, Ω is the equivalent concept but for lower bound. Printing the values in an array is Ω(N)
as well as Ω(log N) and Ω(1). After all, you know that it won't be faster than those runtimes.

0 (big theta): In academia, 0 means both O and Ω. That is, an algorithm is 0(N) if it is both O(N) and Ω(N). 0 gives a
tight bound on runtime

In industry (and therefore in interviews), people seem to have merged 0 and O together. Industry's meaning of big O is
closer to what academics mean by 0, in that it would be seen as incorrect to describe printing an array as O(N2).
Industry would just say this is O(N).

##### Best Case, Worst Case, and Expected Case

We can actually describe our runtime for an algorithm in three different ways.

We rarely ever discuss best case time complexity, because it's not a very useful concept. After all, we could take
essentially any algorithm, special case some input, and then get an O ( 1) time in the best case.

*What is the relationship between best/worst/expected case and big 0/theta/omega?*

It's easy for candidates to muddle these concepts (probably because both have some concepts of"higher':
"lower" and "exactly right"), but there is no particular relationship between the concepts. Best, worst, and expected
cases describe the big O (or big theta) time for particular inputs or scenarios. Big 0, big omega, and big theta
describe the upper, lower, and tight bounds for the runtime.

##### Laws of Big O

**Drop the Constants :** It is very possible for O(N) code to run faster than 0(1) code for specific inputs. Big O just
describes the rate of increase. For this reason, we drop the constants in runtime. An algorithm that one might have
described as O(2N) is actually O(N).

f you're going to count the number of instructions, then you'd have to go to the assembly level and take into account
that multiplication requires more instructions than addition, how the compiler would optimize something, and all sorts
of other details. This would be horrendously complicated.

**Drop the Non-Dominant Terms :** You should drop the non-dominant terms.

- O(N^2 + N) becomesO(N^2).
- O(N + log N) becomesO(N).

We might still have a sum in a runtime. For example, the expression0(B^2 + A) cannot be reduced (without some special
knowledge of A and B).

**Amortized Time :**  An Arraylist is implemented with an array. When the array hits capacity, the Arraylist class will
create a new array with double the capacity and copy all the elements over to the new array. How do you describe the
runtime of insertion?

The array could be full. If the array contains N elements, then inserting a new element will take O(N) time. You will
have to create a new array of size 2N and then copy N elements over. This insertion will take O ( N)
time. However, we also know that this doesn't happen very often. The vast majority of the time insertion will be inO(l)
time.

We need a concept that takes both into account. This is what amortized time does. It allows us to describe that, yes,
this worst case happens every once in a while. But once it happens, it won't happen again for so long that the cost is "
amortized'.

**Recursive Runtimes :** . What's the runtime of this code?

    int f(int n) { 
        if (n <= 1) {
            return 1;
        } 
        return f(n - 1) + f(n - 1);
    } 

Rather than making assumptions, let's derive the runtime by walking through the code. Suppose we call f ( 4). This calls
f ( 3) twice. Each of those calls to f ( 3) calls f ( 2), until we get down to f ( 1 ). How many calls are in this tree?

The tree will have depth N. Each node (i.e., function call) has two children. Therefore, each level will have twice as
many calls as the one above it. This gives us O(2^N).

> Try to remember this pattern. When you have a recursive function that makes multiple calls, the runtime will often 
> (but not always) look like O(branches^depth), where branches is the number of times each recursive call branches

> As you may recall, the base of a log doesn't matter for big O since logs of different bases are only different by a 
> constant factor. However, this does not apply to exponents. The base of an exponent does matter. Compare 2^n and 8^n. 
> If you expand 8^n, you get (2^3)^n, which equals (2^3n), which equals 2^2n * 2^n. As you can see, 8^n and 2^n are 
> different by a factor of 2^2n. That is very much not a constant factor

