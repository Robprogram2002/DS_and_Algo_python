## Recursion

Recursion is a technique by which a function makes one or more calls to itself during execution, or by which a data
structure relies upon smaller instances of the very same type of structure in its representation. Most modern
programming languages support functional recursion using the identical mechanism that is used to support traditional
forms of function calls. When one invocation of the function make a recursive call, that invocation is suspended until
the recursive call completes. Example,

     def factorial(n):
        if n == 0:
            return 1
        else:
            return n factorial(n−1)

We illustrate the execution of a recursive function using a **recursion trace**. Each entry of the trace corresponds to
a recursive call. Each new recursive function call is indicated by a downward arrow to a new invocation. When the
function returns, an arrow showing this return is drawn and the return value may be indicated alongside this arrow.

In Python, each time a function (recursive or otherwise) is called, a structure known as an **activation record** or
**frame** is created to store information about the progress of that invocation of the function. This activation record
includes a namespace for storing the function call’s parameters and local variables, and information about which command
in the body of the function is currently executing.

When the execution of a function leads to a nested function call, the execution of the former call is suspended and its
activation record stores the place in the source code at which the flow of control should continue upon return of the
nested call. This process is used both in the standard case of one function calling a different function, or in the
recursive case in which a function invokes itself. The key point is that there is a different activation record for each
active call.

#### Analyzing recursive functions

for each invocation of the function, we only account for the number of operations that are performed within the body of
that activation. We can then account for the overall number of operations that are executed as part of the recursive
algorithm by taking the sum, over all activations, of the number of operations that take place during each individual
activation. (As an aside, this is also the way we analyze a nonrecursive function that calls other functions from within
its body.)

To compute factorial(n), we see that there are a total of n+1 activations, as the parameter decreases from n in the
first call, to n−1 in the second call, and so on, until reaching the base case with parameter 0. It is also clear, given
an examination of the function body, that each individual activation of factorial executes a constant number of
operations. Therefore, we conclude that the overall number of operations for computing factorial(n) is O(n), as there
are n+1 activations, each of which accounts for O(1) operations.

Considering the running time of the binary search algorithm, we observe that a constant number of primitive operations
are executed at each recursive call of method of a binary search. Hence, the running time is proportional to the number
of recursive calls performed. We will show that at most `log n + 1` recursive calls are made during a binary search of a
sequence having n elements, leading to the following claim.

**Proposition:** The binary search algorithm runs in **O(log n)** time for a sorted sequence with n elements.

### Further Examples of Recursion

We organize our presentation by considering the maximum number of recursive calls that may be started from within the
body of a single activation.

- If a recursive call starts at most one other, we call this a **linear recursion**.
- If a recursive call may start two others, we call this a **binary recursion**.
- If a recursive call may start three or more others, this is **multiple recursion.**

A consequence of the definition of linear recursion is that any recursion trace will appear as a single sequence of
calls. Linear recursion can be a useful tool for processing a data sequence, such as a Python list. Suppose, for
example, that we want to compute the sum of a sequence, S, of n integers.

### Designing Recursive Algorithms

In general, an algorithm that uses recursion typically has the following form:

- **Test for base cases.** We begin by testing for a set of base cases (there should be at least one). These base cases
  should be defined so that every possible chain of recursive calls will eventually reach a base case, and the handling
  of each base case should not use recursion.
- **Recur.** If not a base case, we perform one or more recursive calls. This recursive step may involve a test that
  decides which of several possible recursive calls to make. We should define each possible recursive call so that it
  makes progress towards a base case.

To design a recursive algorithm for a given problem, it is useful to think of the different ways we might define
subproblems that have the same general structure as the original problem. If one has difficulty finding the repetitive
structure needed to design a recursive algorithm, it is sometimes useful to work out the problem on a few concrete
examples to see how the subproblems should be defined.

A successful recursive design sometimes requires that we redefine the original problem to facilitate similar-looking
subproblems. Often, this involved reparameterizing the signature of the function.

### Eliminating Tail Recursion

the usefulness of recursion comes at a modest cost. In particular, the Python interpreter must maintain activation
records that keep track of the state of each nested call. When computer memory is at a premium, it is useful in some
cases to be able to derive nonrecursive algorithms from recursive ones

some forms of recursion can be eliminated without any use of axillary memory. A notable such form is known as **tail
recursion**. A recursion is a tail recursion if any recursive call that is made from one context is the very last
operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing 
recursion. By necessity, a tail recursion must be a linear recursion


