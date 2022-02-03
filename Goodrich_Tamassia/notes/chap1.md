## Python language

Python is formally an **interpreted language**. Commands are executed through a piece of software known as the **Python
interpreter**. The interpreter receives a command, evaluates that command, and reports the result of the command.

The programmer typically defines a series of commands in advance and saves those commands in a plain text file known as
source code or a script.

Commands from a predefined script saved in a file (e.g., demo.py) are executed by invoking the interpreter with the
filename as an argument (e.g., python demo.py).

Python’s syntax relies heavily on the use of whitespace. Individual statements are typically concluded with a newline
character. Whitespace is also key in delimiting the bodies of control structures in Python. Specifically, a block of
code is indented to designate it as the body of a control structure, and nested control structures use increasing
amounts of indentation.

> Python is an **object-oriented language** and classes form the basis for all data types.

**Assignment statement :**

    temperature = 98.6

This command establishes temperature as an **identifier** (also known as a **name**), and then associates it with the
**object** expressed on the right-hand side of the equal sign.

The semantics of a Python identifier is most similar to a *reference variable* in Java or a *pointer variable*
in C++.

> *Each identifier is implicitly associated with the memory address of the object to which it refers*

A Python identifier may be assigned to a special object named **None**, serving a similar purpose to a null reference in
Java or C++.

Python is a **dynamically typed language**, as there is no advance declaration associating an identifier with a
particular data type. An identifier can be associated with any type of object, and it can later be reassigned to another
object of the same (or different) type.

> Although an identifier has no declared type, the object to which it refers has a definite type

In this case, the identifier `temperature` is associated with an instance of the float class having that value.

A programmer can establish an **alias** by assigning a second identifier to an existing object.

    original = temperature

Identifiers `temperature` and `original` are aliases for the same object.

Once an alias has been established, either name can be used to access the underlying object. If that object supports
behaviors that affect its state, changes enacted through one alias will be apparent when using the other alias (because
they refer to the same object). However, if one of the names is reassigned to a new value using a subsequent assignment
statement, that does not affect the aliased object, rather it breaks the alias.

    temperature = temperature + 5.0

The execution of this command begins with the evaluation of the expression on the right-hand side of the `=` operator.
That expression, `temperature + 5.0`, is evaluated based on the existing binding of the name `temperature`, and so the
result has value 103.6, that is, `98.6 + 5.0`.

That result is stored as a new floating-point instance, and only then is the name on the left-hand side of the
assignment statement, temperature, (re)assigned to the result. This had no effect on the value of the existing float
instance that identifier `original` continues to reference.

> The temperature identifier has been assigned to a new value, while original continues to refer to the previously existing value.

### Creating and Using Objects

The process of creating a new instance of a class is known as **instantiation**. In general, the syntax for
instantiating an object is to invoke the **constructor** of a class.

Python supports traditional functions and Python’s classes may also define one or more **methods** (also known as **
member functions**), which are invoked on a specific instance of a class using the dot (“.”)
operator

When using a **method** of a class, it is important to understand its behavior. Some methods return information about
the state of an object, but do not change that state. These are known as **accessors**. Other methods, such as the sort
method of the list class, do change the state of an object. These methods are known as **mutators** or **update
methods**.

A class is **immutable** if each object of that class has a fixed value upon instantiation that cannot subsequently be
changed. For example, the float class is immutable. Once an instance has been created, its value cannot be changed (
although an identifier referencing that object can be reassigned to a different value).

The **int** class is designed to represent integer values with arbitrary magnitude. if f represents a floating-point
value, the syntax int(f) produces the *truncated* value of f. If s represents a string, then int(s) produces the
integral value that string represents. For example, the expression int('137') produces the integer value 137. If an
invalid string is given as a parameter, as in int('hello'), a ValueError is raised.

The **list**, **tuple**, and **str** classes are **sequence types**  in Python, representing a collection of values in
which the order is significant. The list class is the most general, representing a sequence of arbitrary objects (akin
to an “array” in other languages). The tuple class is an **immutable** version of the list class, benefiting from a
streamlined internal representation. The str class is specially designed for representing an immutable sequence of text
characters. We note that *Python does not have a separate class for characters*; they are just strings with length one

A list is a **referential structure**, as it technically stores a sequence of **references** to its elements.

Python’s **set** class represents the mathematical notion of a set, namely a collection of elements, without duplicates,
and without an inherent order to those elements. The major advantage of using a set, as opposed to a list, is that it
has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data
structure known as a hash table

> Note: only instances of immutable types can be added to a Python set.

It is possible to maintain a set of tuples, but not a set of lists or a set of sets, as lists and sets are mutable. The
**frozenset** class is an immutable form of the set type, so it is legal to have a set of frozensets.

### Expressions, Operators, and Precedence

The `and` and `or` operators short-circuit, in that they do not evaluate the second operand if the result can be
determined based on the value of the first operand. This feature is useful when constructing Boolean expressions in
which we first test that a certain condition holds (such as a reference not being None), and then test a condition that
could have otherwise generated an error condition had the prior test not succeeded

Python supports the following operators to test two notions of equality:

    is --> same identity
    is --> not different identity
    == --> equivalent
    != --> not equivalent

The expression `a` is `b` evaluates to True, precisely when identifiers a and b are aliases for the same object. The
expression a == b tests a more general notion of equivalence. If identifiers a and b refer to the same object, then
`a == b` should also evaluate to True. Yet `a == b` also evaluates to True when the identifiers refer to different
objects that happen to have values that are deemed equivalent. The precise notion of equivalence depends on the data
type.

In most programming situations, the equivalence tests == and != are the appropriate operators; use of is and is not
should be reserved for situations in which it is necessary to detect true aliasing

Each of Python’s built-in sequence types (str, tuple, and list) support the following operator syntaxes:

    s[j] --> element at index j
    s[start:stop] --> slice including indices [start,stop)
    s[start:stop:step] --> slice including indices start, start + step, start + 2step,..., up to but not equalling or stop
    s+t --> concatenation of sequences
    k*s --> shorthand for s + s + s + ... (k times)
    val in s --> containment check
    val not in s --> non-containment check

Python also supports the use of **negative indices**, which denote a distance from the end of the sequence; index −1
denotes the last element, index −2 the second to last, and so on.

Lists also support a syntax, `del s[j]`, that removes the designated element from the list. Slice notation can also be
used to replace or delete a sublist.

The notation val in s can be used for any of the sequences to see if there is an element equivalent to val in the
sequence. For strings, this syntax can be used to check for a single character or for a larger substring, as with 'amp'
in 'example' .

All sequences define comparison operations based on **lexicographic order**, performing an element by element comparison
until the first difference is found.

### Functions

Each time a function is called, Python creates a dedicated **activation record** that stores information relevant to the
current call. This activation record includes what is known as a **namespace**  to manage all identifiers that have
local scope within the current call. The namespace includes the function’s parameters and any other identifiers that are
defined locally within the body of the function. An identifier in the local scope of the function caller has no relation
to any identifier with the same name in the caller’s scope (although identifiers in different scopes may be aliases to
the same object). I

To be a successful programmer, one must have clear understanding of the mechanism in which a programming language passes
information to and from a function. In the context of a **function signature**, the identifiers used to describe the
expected parameters are known as **formal parameters**, and the objects sent by the caller when invoking the function
are the **actual parameters**.

Parameter passing in Python follows the semantics of the standard **assignment statement**.

When a function is invoked, each identifier that serves as a formal parameter is assigned, in the function’s local
scope, to the respective actual parameter that is provided by the caller of the function. The communication of a return
value from the function back to the caller is similarly implemented as an assignment.

An advantage to Python’s mechanism for passing information to and from a function is that objects are not copied. This
ensures that the invocation of a function is efficient, even in a case where a parameter or return value is a complex
object.

Example,

    prizes = count(grades, A )

Just before the function body is executed, the actual parameters, grades and A , are implicitly assigned to the formal
parameters, data and target, as follows:

    data = grades
    target = 'A'

These assignment statements establish identifier `data` as an alias for `grades` and `target` as a name for the string
literal A .

**Mutable Parameters :** Python’s parameter passing model has additional implications when a parameter is a mutable
object. Because the formal parameter is an alias for the actual parameter, the body of the function may interact with
the object in ways that change its state. As an aside, we note that reassigning a new value to a formal parameter with a
function body, such as by setting data = [ ], does not alter the actual parameter; such a reassignment simply breaks the
alias.

There are many legitimate cases in which a function may be designed (and clearly documented) to modify the state of a
parameter. As a concrete example, we present the following implementation of a method named scale that’s primary purpose
is to multiply all entries of a numeric data set by a given factor.

    def scale(data, factor):
        for j in range(len(data)):
            data[j] = factor

Python provides means for functions to support more than one possible calling signature. Such a function is said to be
**polymorphic**. Most notably, functions can declare one or more default values for parameters, thereby allowing the
caller to invoke a function with varying numbers of actual parameters.

The traditional mechanism for matching the actual parameters sent by a caller, to the formal parameters declared by the
function signature is based on the concept of **positional arguments**.

Python supports an alternate mechanism for sending a parameter to a function known as a **keyword argument**. A keyword
argument is specified by explicitly assigning an actual parameter to a formal parameter by name.

### Exception Handling

Exceptions are unexpected events that occur during the execution of a program. An exception might result from a logical
error or an unanticipated situation. In Python, **exceptions** (also known as **errors**) are objects that are **
raised** (or **thrown**) by code that encounters an unexpected circumstance. The Python interpreter can also raise an
exception should it encounter an unexpected condition, like running out of memory. A raised error may be **caught** by a
surrounding context that “handles” the exception in an appropriate fashion. If uncaught, an exception causes the
interpreter to stop executing the program and to report an appropriate message to the console. In this section, we
examine the most common error types in Python, the mechanism for catching and handling errors that have been raised, and
the syntax for raising errors from within user-defined blocks of code.

Python includes a rich hierarchy of exception classes that designate various categories of errors. The **Exception**
class serves as a base class for most other error types. An instance of the various subclasses encodes details about a
problem that has occurred.

An exception is thrown by executing the raise statement, with an appropriate instance of an exception class as an
argument that designates the problem

When checking the validity of parameters sent to a function, it is customary to first verify that a parameter is of an
appropriate type, and then to verify that it has an appropriate value. For example, the sqrt function in Python’s math
library performs error-checking that might be implemented as follows:

    def sqrt(x):
        if not isinstance(x, (int, float)):
            raise TypeError( x must be numeric )
        elif x < 0:
            raise ValueError( x cannot be negative )
        # do the real work here...

Checking the type of an object can be performed at run-time using the built-in function, isinstance. In simplest form,
`isinstance(obj, cls)` returns True if object, `obj`, is an instance of class, cls, or any subclass of that type. In the
above example, a more general form is used with a tuple of allowable types indicated with the second parameter.

How much error-checking to perform within a function is a matter of debate. Checking the type and value of each
parameter demands additional execution time and, if taken to an extreme, seems counter to the nature of Python

One philosophy for managing exceptional cases is to “**look before you leap.**” The goal is to entirely avoid the
possibility of an exception being raised through the use of a proactive conditional test. Revisiting our division
example, we might avoid the offending situation by writing:

    if y != 0:
        ratio = x / y
    else:
        ... do something else ...

A second philosophy, often embraced by Python programmers, is that “**it is easier to ask for forgiveness than it is to
get permission.**” This quote is attributed to Grace Hopper, an early pioneer in computer science. The sentiment is that
we need not spend extra execution time safeguarding against every possible exceptional case, as long as there is a
mechanism for coping with a problem after it arises. In Python, this philosophy is implemented using a **try-except**
control structure.

    try:
        ratio = x / y
    except ZeroDivisionError:
        ... do something else ...

the “try” block is the primary code to be executed. Although it is a single command in this example, it can more
generally be a larger block of indented code. Following the try-block are one or more “except” cases, each with an
identified error type and an indented block of code that should be executed if the designated error is raised within the
try-block.

The relative advantage of using a try-except structure is that the non-exceptional case runs efficiently, without
extraneous checks for the exceptional condition. However, handling the exceptional case requires slightly more time when
using a try-except structure than with a standard conditional statement. For this reason, the try-except clause is best
used when there is reason to believe that the exceptional case is relatively unlikely, or when it is prohibitively
expensive to proactively evaluate a condition to avoid the exception.

Exceptions are objects that can be examined when caught. To do so, an identifier must be established with a syntax as
follows:

    try:
        fp = open( sample.txt )
    except IOError as e:
        print( Unable to open the file: , e)

In this case, the name, e, denotes the instance of the exception that was thrown, and printing it causes a detailed
error message to be displayed. If we want to handle two or more types of errors in the same way, we can use a single
except-statement, as in the following example:

    try:
        age = int(input( Enter your age in years: ))
        if age <= 0:
            print( Your age must be positive )
    except (ValueError, EOFError):
        print( Invalid response )

> Note that when an error is raised within the try-block, the remainder of that body is immediately skipped.

In order to provide different responses to different types of errors, we may use two or more except-clauses as part of a
try-structure. In our previous example, an EOFError suggests a more insurmountable error than simply an errant value
being entered. In that case, we might wish to provide a more specific error message, or perhaps to allow the exception
to interrupt the loop and be propagated to a higher context.

    try:
        age = int(input( Enter your age in years: ))
        if age <= 0:
            print( Your age must be positive )
    except ValueError:
        print( That is an invalid age specification )
    except EOFError:
        print( There was an unexpected error reading input. )
        raise                                                   # let s re-raise this exception

A try-statement can have a **finally clause**, with a body of code that will always be executed in the standard or
exceptional cases, even when an uncaught or re-raised exception occurs. That block is typically used for critical
cleanup work, such as closing an open file.

### Iterators and Generators

User defined types may also support iteration. In Python, the mechanism for iteration is based upon the following
conventions:

- An **iterator** is an object that manages an iteration through a series of values. If variable, i, identifies an
  iterator object, then each call to the built-in function,
  `next(i)`, produces a subsequent element from the underlying series, with a
  `StopIteration` exception raised to indicate that there are no further elements.
- An **iterable** is an object, obj, that produces an iterator via the syntax `iter(obj)`.

By these definitions, an instance of a list is an iterable, but not itself an iterator. With `data = [1, 2, 4, 8]`, it
is not legal to call `next(data)`. However, an iterator object can be produced with syntax, `i = iter(data)`, and then
each subsequent call to `next(i)` will return an element of that list. The for-loop syntax in Python simply automates
this process, creating an iterator for the give iterable, and then repeatedly calling for the next element until
catching the `StopIteration` exception.

More generally, it is possible to create multiple iterators based upon the same iterable object, with each iterator
maintaining its own state of progress. However, iterators typically maintain their state with indirect reference back to
the original collection of elements. For example, calling iter(data) on a list instance produces an instance of the list
iterator class. That iterator does not store its own copy of the list of elements. Instead, it maintains a current index
into the original list, representing the next element to be reported. Therefore, if the contents of the original list
are modified after the iterator is constructed, but before the iteration is complete, the iterator will be reporting the
updated contents of the list

Python also supports functions and classes that produce an implicit iterable series of values, that is, without
constructing a data structure to store all of its values at once.

    range(1000000)

The above function does not return a list of numbers; it returns a *range object* that is iterable. This object
generates the million values one at a time, and only as needed. Such a **lazy evaluation technique** has great
advantage.

We see lazy evaluation used in many of Python’s libraries. For example, the dictionary class supports methods keys( ),
values( ), and items( ), which respectively produce a “view” of all keys, values, or (key,value) pairs within a
dictionary. None of these methods produces an explicit list of results. Instead, the views that are produced are
iterable objects based upon the actual contents of the dictionary. An explicit list of values from such an iteration can
be immediately constructed by calling the list class constructor with the iteration as a parameter. We can similarly
construct a tuple or set instance based upon a given iterable

**Generators.** the most convenient technique for creating iterators in Python is through the use of generators. A
generator is implemented with a syntax that is very similar to a function, but instead of returning values, a **yield**
statement is executed to indicate each element of the series. As an example, consider the goal of determining all
factors of a positive integer. An implementation of a generator for computing those factors could be implemented as
follows:

    def factors(n): # generator that computes factors
      for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
          yield k # yield this factor as next result

If a programmer writes a loop such as for factor in factors(100):, an instance of our generator is created. For each
iteration of the loop, Python executes our procedure. until a yield statement indicates the next value. At that point,
the procedure is temporarily interrupted, only to be resumed when another value is requested. When the flow of control
naturally reaches the end of our procedure (or a zero-argument return statement), a StopIteration exception is
automatically raised. Although this particular example uses a single yield statement in the source code, a generator can
rely on multiple yield statements in different constructs, with the generated series determined by the natural flow of
control.

The results are only computed if requested, and the entire series need not reside in memory at one time. In fact, a
generator can effectively produce an infinite series of values.

### Additional Python Conveniences

##### Comprehension Syntax

A very common programming task is to produce one series of values based upon the processing of another series. Often,
this task can be accomplished quite simply in Python using what is known as a **comprehension syntax**. We begin by
demonstrating **list comprehension**, as this was the first form to be supported by Python. Its general form is as
follows:

    [ expression for value in iterable if condition ]

We note that both expression and condition may depend on value, and that the if-clause is optional. The evaluation of
the comprehension is logically equivalent to the following traditional control structure for computing a resulting list:

    result = [ ]
    for value in iterable:
      if condition:
        result.append(expression)

As an example consider the goal of producing a list of factors for an integer n. That task is accomplished with the
following list comprehension:

    factors = [k for k in range(1,n+1) if n % k == 0]

Python supports similar comprehension syntaxes that respectively produce a set, generator, or dictionary. We compare
those syntaxes using our example for producing the squares of numbers.

    [ k k for k in range(1, n+1) ] list comprehension
    { k k for k in range(1, n+1) } set comprehension
    ( k k for k in range(1, n+1) ) generator comprehension
    { k:k k for k in range(1, n+1) } dictionary comprehension

The generator syntax is particularly attractive when results do not need to be stored in memory. For example, to compute
the sum of the first n squares, the generator syntax, `total = sum(k k for k in range(1, n+1))`, is preferred to the use
of an explicitly instantiated list comprehension as the parameter.

##### Packing and Unpacking of Sequences

If a series of comma-separated expressions are given in a larger context, they will be treated as a single tuple, even
if no enclosing parentheses are provided. This behavior is called **automatic packing** of a tuple. One common use of
packing in Python is when returning multiple values from a function. If the body of a function executes the command,

    return x, y 

it will be formally returning a single object that is the tuple (x, y).

As a dual to the packing behavior, Python can automatically **unpack** a sequence, allowing one to assign a series of
individual identifiers to the elements of sequence. As an example, we can write

    a, b, c, d = range(7, 11)

which has the effect of assigning a=7, b=8, c=9, and d=10. This technique can be used to unpack tuples returned by a
function. This syntax can also be used in the context of a for loop, when iterating over a sequence of iterables. This
style of loop is quite commonly used to iterate through key-value pairs that are returned by the items( ) method of the
dict class, as in:

    for k, v in mapping.items( ):

##### Simultaneous Assignments

The combination of automatic packing and unpacking forms a technique known as **simultaneous assignment**, whereby we
explicitly assign a series of values to a series of identifiers, using a syntax:

    x, y, z = 6, 2, 5

In effect, the right-hand side of this assignment is automatically packed into a tuple, and then automatically unpacked
with its elements assigned to the three identifiers on the left-hand side. When using a simultaneous assignment, all of
the expressions are evaluated on the right-hand side before any of the assignments are made to the left-hand variables.
This is significant, as it provides a convenient means for swapping the values associated with two variables:

    j, k = k, 

With this command, j will be assigned to the old value of k, and k will be assigned to the old value of j. Without
simultaneous assignment, a swap typically requires more delicate use of a temporary variable, such as

    temp = j
    j=k
    k = temp

With the simultaneous assignment, the unnamed tuple representing the packed values on the right-hand side implicitly
serves as the temporary variable when performing such a swap.

### Scopes and Namespaces

The process of determining the value associated with an identifier is known as **name resolution**. Whenever an
identifier is assigned to a value, that definition is made with a specific **scope**. Top-level assignments are
typically made in what is known as **global scope**. Assignments made within the body of a function typically have scope
that is **local** to that function call. Therefore, an assignment, x=5, within a function has no effect on the
identifier, x, in the broader scope.

Each distinct scope in Python is represented using an abstraction known as a **namespace**. A namespace manages all
identifiers that are currently defined in a given scope.

Python implements a namespace with its own dictionary that maps each identifying string to its associated value. Python
provides several ways to examine a given namespace. The function, `dir`, reports the names of the identifiers in a given
namespace (i.e., the keys of the dictionary), while the function, `vars`, returns the full dictionary. By default, calls
to `dir( )` and `vars( )` report on the most locally enclosing namespace in which they are executed.

When an identifier is indicated in a command, Python searches a series of namespaces in the process of name resolution.
First, the most locally enclosing scope is searched for a given name. If not found there, the next outer scope is
searched, and so on.

#### First Class Objects

> In the terminology of programming languages, **first-class objects** are instances of a type that can be assigned to
> an identifier, passed as a parameter, or returned by a function.

All the basic data types such as int and list, are clearly first-class types in Python. In Python, functions and classes
are also treated as first-class objects.

This demonstrates the mechanism that is used by Python to allow one function to be passed as a parameter to another. In
terms of namespaces, an assignment such as scream = print, introduces the identifier, scream, into the current
namespace, with its value being the object that represents the built-in function, print. The same mechanism is applied
when a user defined function is declared.

    def count(data, target):

Such a declaration introduces the identifier, count, into the current namespace, with the value being a function
instance representing its implementation. In similar fashion, the name of a newly defined class is associated with a
representation of that class as its value.

### Modules and Import Statement

Python’s import statement loads definitions from a module into the current namespace. One form of an import statement
uses a syntax such as the following:

    from math import pi, sqrt

This command adds both pi and sqrt, as defined in the math module, into the current namespace, allowing direct use of
the identifier, pi, or a call of the function, sqrt(2). If there are many definitions from the same module to be
imported, an asterisk may be used as a wild card, as in,

    from math import *, 

but this form should be used sparingly. The danger is that some of the names defined in the module may conflict with
names already in the current namespace (or being imported from another module), and the import causes the new
definitions to replace existing ones.

Another approach that can be used to access many definitions from the same module is to import the module itself, using
a syntax such as:

    import math 

Formally, this adds the identifier, math, to the current namespace, with the module as its value. (Modules are also
first-class objects in Python.) Once imported, individual definitions from the module can be accessed using a
fully-qualified name, such as math.pi or math.sqrt(2).

It is worth noting that top-level commands with the module source code are executed when the module is first imported,
almost as if the module were its own script. There is a special construct for embedding commands within the module that
will be executed if the module is directly invoked as a script, but not when the module is imported from another script.
Such commands should be placed in a body of a conditional statement of the following form,

    if name == __main__ :

