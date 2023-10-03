## Getting Starter

The science of computing is concerned with using computers to solve problems.  The complexity of large problems
and the corresponding complexity of the solutions can tend to overshadow the fundamental
ideas related to the problem-solving process.

### What is  CS?
Computer science is the study of problems, problem-solving, and the solutions that come out
of the problem-solving process. Given a problem, a computer scientist’s goal is to develop an
**algorithm**, a step-by-step list of instructions for solving any instance of the problem that might
arise

>  Algorithms are solutions. Computer science can be thought of as the study of algorithms.

However, we must be careful to include the fact that some problems may not have a solution. Although proving this statement
is beyond the scope of this text, the fact that some problems cannot be solved is important for
those who study computer science. We can fully define computer science, then, by including
both types of problems and stating that computer science is the study of solutions to problems
as well as the study of problems with no solutions

We say that a problem is **computable** if an algorithm exists for solving it. An alternative
definition for computer science, then, is to say that:

> computer science is the study of problems that are and that are not computable, the study of the existence and the
> nonexistence of algorithms.

In any case, you will note that the word “computer” did not come up at all. *Solutions
are considered independent from the machine*. (Although computers play an important supporting role as a tool in the
discipline, they are just that – tools.)

Computer science, as it pertains to the problem-solving process itself, is also the study of
**abstraction**. Abstraction allows us to view the problem and solution in such a way as to
separate the so-called logical and physical perspectives.

the user of the abstraction, sometimes also called the client, does not need to know the details as long as the user
is aware of the way the interface works. This interface is the way we as users communicate with the underlying
complexities of the implementation


> *math.sqrt(16)* This is an example of **procedural abstraction**. We do not necessarily know how the square
root is being calculated, but we know what the function is called and how to use it. This is sometimes referred to as a
“black box” view of a process. We simply describe the interface: the name of the function, what is needed (the parameters),
and what will be returned. The details are hidden inside

### What is Programming?
**Programming** is the process of taking an algorithm and encoding it into a notation, a programming language, so that
it can be executed by a computer. Although many programming languages and many different types of computers exist,
the important first step is the need to have the solution. Without an algorithm there can be no program.

*Computer science is not the study of programming*. Programming, however, is an important
part of what a computer scientist does. Programming is often the way that we create a representation for our solutions.
Therefore, this language representation and the process of creating it becomes a fundamental part of the discipline.

> *Algorithms describe the solution to a problem in terms of the data needed to represent the
problem instance and the set of steps necessary to produce the intended result. Programming
languages must provide a notational way to represent both the process and the data. To this
end, languages provide control constructs and data types*.

##### Control constructs & Data Types

Allow algorithmic steps to be represented in a convenient yet unambiguous
way. At a minimum, algorithms require constructs that perform sequential processing, selection
for decision-making, and iteration for repetitive control. As long as the language provides these
basic statements, it can be used for algorithm representation.

All data items in the computer are represented as strings of binary digits. In order to give these
strings meaning, we need to have **data types**. *Data types provide an interpretation for this
binary data so that we can think about the data in terms that make sense with respect to the
problem being solved.*

> These low-level, built-in data types (sometimes called the **primitive data types**) provide the building blocks
>for algorithm development.

**Example :** Strings of binary digits in the computer’s memory can be interpreted as integers and given the typical meanings
that we commonly associate with integers (16, -2, 654).

>  In addition, a data type also provides a description of the operations that the data items can participate in

These simple, language-provided constructs and data types, although certainly sufficient  to represent complex solutions,
are typically at a disadvantage as we work through the problem-solving process.

##### DATA STRUCTURES & ABSTRACT DATA TYPES

> To manage the complexity of problems and the problem-solving process, computer scientists
use abstractions to allow them to focus on the “big picture” without getting lost in the details.
By creating models of the problem domain, we are able to utilize a better and more efficient
problem-solving process. These models allow us to describe the data that our algorithms will
manipulate in a much more consistent way with respect to the problem itself.

**Example : procedural abstraction.**  a process that hides the details of a particular
function to allow the user or client to view it at a very high level.

We now turn our attention to a similar idea, that of **data abstraction**. An **abstract data type**, sometimes
called an **ADT**, is a logical description of how we view the data and the operations that are allowed without regard
to how they will be implemented.

This means that we are concerned only with what the data
is representing and not with how it will eventually be constructed. By providing this level of
abstraction, we are creating an encapsulation around the data. The idea is that by encapsulating
the details of the implementation, we are hiding them from the user’s view. This is called
**information hiding**.

> The user interacts with the interface, using the operations that have been specified by the abstract data
type. The abstract data type is the shell that the user interacts with. The implementation is
hidden one level deeper. The user is not concerned with the details of the implementation.

The *implementation of an abstract data type*, often referred to as a **data structure**, will require
that we provide a physical view of the data using some collection of programming constructs
and primitive data types.

 the separation of these two perspectives wil allow us to define the complex data models for our problems without giving any indication
as to the details of how the model will actually be built. This provides an **implementation-independent** view of the data.

>  Since there will usually be many different ways to implement
an abstract data type, this implementation independence allows the programmer to switch the
details of the implementation without changing the way the user of the data interacts with it.
The user can remain focused on the problem-solving process

### So, Why study Algorithms

Computer scientists learn by experience. We learn by seeing others solve problems and by
solving problems by ourselves. Being exposed to different problem-solving techniques and
seeing how different algorithms are designed helps us to take on the next challenging problem
that we are given. By considering a number of different algorithms, we can begin to develop
pattern recognition so that the next time a similar problem arises, we are better able to solve it.

Consider the example of sqrt seen earlier. It is entirely possible that there are many different ways to implement the
details to compute the square root function. We would like to have some way to compare these two solutions. Even though
they both work, one is perhaps “better” than the other. We might suggest that one is more efficient or that one simply works
faster or uses less memory. As we study algorithms, we can learn analysis techniques that allow us to compare and contrast
solutions based solely on their own characteristics, not the characteristics of the program or computer used to implement them.

In the worst case scenario, we may have a problem that is intractable, meaning that there is no
algorithm that can solve the problem in a realistic amount of time. It is important to be able
to distinguish between those problems that have solutions, those that do not, and those where
solutions exist but require too much time or other resources to work reasonably

There will often be trade-offs that we will need to identify and decide upon. As computer
scientists, in addition to our ability to solve problems, we will also need to know and understand solution evaluation techniques.

> In the end, there are often many ways to solve a problem.
Finding a solution and then deciding whether it is a good one are tasks that we will do over and
over again.

### Python
Python is a modern, easy-to-learn, object-oriented programming language. It has a powerful
set of built-in data types and easy-to-use control constructs. Since Python is an interpreted
language, it is most easily reviewed by simply looking at and describing interactive sessions.

 Python supports the **object-oriented programming paradigm**. This means
that Python considers data to be the focal point of the problem-solving process. In Python, as
well as in any other object-oriented programming language, *we define a class to be a description
of what the data look like (the state) and what the data can do (the behavior).* Classes are
analogous to abstract data types because a user of a class only sees the state and behavior of
a data item. Data items are called objects in the object-oriented paradigm. An object is an
instance of a class.

##### Built-in Atomic Data Types

Python has two main built-in numeric classes that implement the integer and floating point data types. These Python classes
are called **int** and **float**.

The boolean data type, implemented as the Python **bool** class, will be quite useful for
representing truth values. The possible state values for a boolean object are **True** and **False**
with the standard boolean operators, and, or, and not.

Boolean data objects are also used as results for **comparison operators** such as equality (==)
and greater than (>).

> In addition, relational operators and logical operators can be combined
together to form complex logical questions.

In Python, identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length.  A Python
**variable** is created when a name is used for the first time on the left-hand side of an **assignment statement**.

> *Assignment statements provide a way to associate a name with a
value. The variable will hold a **reference** to a piece of data and not the data itself.*

The assignment statement **the_sum = 0** creates a variable called the_sum and lets it hold the
reference to the data object 0.

> In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object
>is “assigned” to the name on the left-hand side

 If the type of the data changes (e.g the_sum = True)  so does the type of the variable.

 >  The assignment statement changes the reference being held by the variable. This is a dynamic characteristic of
Python. The same variable can refer to many different types of data.

**In summary :**

- Variables Hold References to Data Objects
- Assignment changes the Reference

##### Built-in Collection Data Types

Lists, strings, and tuples are ordered collections that are very similar in
general structure but have specific differences that must be understood for them to be used
properly. Sets and dictionaries are unordered collections.

> A list is an ordered collection of zero or more references to Python data objects. Lists are
written as comma-delimited values enclosed in square brackets. Lists are heterogeneous, meaning that the data
objects need not all be from the same class and the collection can be assigned to a variable

Note that when Python evaluates a list, the list itself is returned. However, in order to remember
the list for later processing, its reference needs to be assigned to a variable. Since lists are considered to be
sequentially ordered, they support a number of operations that can be applied to any Python sequence.

Lists support a number of methods that will be used to build data structures.
- append -> Adds a new item to the end of a list  -> list.append(item)
- insert -> Inserts an item at the specify position in a list -> list.insert(index, item)
- pop -> Removes and returns the last item in a list  -> list.pop()
- pop -> Removes and returns the specify item in a list -> list.pop(index)
- sort -> Modifies a list to be sorted -> list.sort()
- reverse -> Modifies a list to be in reverse order -> list.reverse()
- del (keyword) -> Deletes the item in the specify position -> del list[index]
- index -> Returns the index of the first occurrence of item -> list.index(item)
- count -> Returns the number of occurrences of item -> list.count(item)
- remove -> Removes the first occurrence of item -> list.remove(item)

You can see that some of the methods, such as pop, return a value and also modify the list.
Others, such as reverse, simply modify the list with no return value.

**Notation note.** my_list.append(False) can be read as “ask the object my_list to perform its append method and send
it the value False.” Even simple data objects such as integers can invoke methods (e.g (54).__add__(21))

**Strings** are sequential collections of zero or more letters, numbers and other symbols. We call
these letters, numbers and other symbols **characters**.  Literal string values are differentiated
from identifiers by using quotation marks (either single or double).

Since strings are sequences, all of the sequence operations described above work as you would
expect. In addition, strings have a number of specific methods.

- find -> Returns the index of the first occurrence of item  -> string.find(item)
- split -> Splits a string into substrings at the specify character  -> string.split(s_char)

(If no division is specified, the split method looks for whitespace characters such as tab,
newline and space)

A major difference between lists and strings is that lists can be modified while strings cannot. This is referred to as
**mutability**. Lists are mutable; strings are immutable.

**Tuples** are very similar to lists in that they are heterogeneous sequences of data. The difference
is that a tuple is immutable, like a string. A tuple cannot be changed. Tuples are written as
comma-delimited values enclosed in parentheses. As sequences, they can use any operation
described above.

A **set** is an unordered collection of zero or more immutable Python data objects. Sets do not
allow duplicates and are written as comma-delimited values enclosed in curly braces. Sets are heterogeneous, and the
collection can be assigned to a variable. Even though sets are not considered to be sequential, they do support a few of the familiar
operations presented earlier.

Sets support a number of methods that should be familiar to those who have worked with them
in a mathematics setting. Note that union, intersection, issubset, and difference all have operators that can be
used as well.

**Methods**

- union -> Returns a new set with all elements from both sets  -> set1.union(set2)
- intersection -> Returns a new set with only the elements common to both sets  -> set1.intersection(set2)
- difference -> Returns a new set with all items from the first set not in second -> set1.difference(set2)
- issubset -> Asks whether all elements of one set are in the other -> set1.issubset(set2)
- add -> Adds item to the set -> set1.add(item)
- remove ->  Removes item from the set -> set1.remove(item)
- pop ->  Removes an arbitrary element from the set -> set1.pop()
- clear ->  Removes all elements from the set -> set1.clear()

**Operators**

- in -> Set membership -> x.in(set)
- len -> Returns the cardinality (i.e. the length) of the set  -> len(set)
- | -> Returns a new set with all elements from both sets  -> set1 | set2
- & -> Returns a new set with only the elements common to both sets  -> set1 & set2
- - -> Returns a new set with all items from the first set not in second -> set1 - set2
- <= ->  Asks whether all elements of the first set are in the second -> set1 <= set2

**Dictionaries** are collections of associated pairs of items where each pair consists of a key and a value.
We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair.
It is important to note that the dictionary is maintained in no particular order with respect to the
keys. The placement of a key is dependent on the idea of “hashing”.

Dictionaries have both methods and operators.

- keys -> dict.keys() -> Returns the keys of the dictionary in a dict_keys object
- values -> dict.values() -> Returns the values of the dictionary in a dict_values object
- items -> dict.items() -> Returns the key-value pairs in a dict_items object
- get -> dict.get(k) -> Returns the value associated with 𝑘, None otherwise
- get -> dict.get(k, alt) -> Returns the value associated with 𝑘, 𝑎𝑙𝑡 otherwise

The keys, values, and items methods all return objects that
contain the values of interest. You can use the list function to convert them to lists. You
will also see that there are two variations on the get method. If the key is not present in the
dictionary, get will return None. However, a second, optional parameter can specify a return
value instead.

##### String Formatting

A **formatted string** is a template in which words or spaces that will remain constant are combined with placeholders for variables
that will be inserted into the string. Example : *print(name, "is", age, "years old.")*  contains the words is and years old, but the
name and the age will change depending on the variable values at the time of execution.

Using a formatted string, we write the previous statement as

> print("%s is %d years old." % (name, age))

The % operator is a string operator called the **format operator**. The left side of the expression holds the template or format string,
and the right side holds a collection of values that will be substituted into the format string.
Note that the number of values in the collection on the right side corresponds with the number
of % characters in the format string. Values are taken in order, left to right from the collection
and inserted into the format string

 The format string may contain one or more conversion specifications. A **conversion character** tells the format operator
 what type of value is going to be inserted into that position in the string.

- d,i -> Integer
- u -> Unsigned Integer
- f -> Floating point as m.ddddd
- e -> Floating point as m.ddddde+/-xx
- E -> Floating point as m.dddddE+/-xx
- c -> Single character
- s -> String, or any Python data object that can be converted to a string by using the str
function

- % -> Insert a literal % character

In addition to the format character, you can also include a **format modifier** between the % and
the format character. Format modifiers may be used to left-justify or right-justify the value
with a specified field width. Modifiers can also be used to specify the field width along with a
number of digits after the decimal point.

**Modifiers**
- number -> Example: %20d -> Put the value in a field width of 20
- - -> Example: %-20d -> Put the value in a field 20 characters wide, left-justified
- + -> Example: %+20d -> Put the value in a field 20 characters wide, right-justified
- 0 -> Example: %020d -> Put the value in a field 20 characters wide, fill in with leading zeros
- . -> Example: %20.2f -> Put the value in a field 20 characters wide with 2 characters to the right of the decimal point

The right side of the format operator is a collection of values that will be inserted into the
format string. The collection will be either a tuple or a dictionary. If the collection is a tuple,
the values are inserted in order of position. That is, the first element in the tuple corresponds
to the first format character in the format string. If the collection is a dictionary, the values
are inserted according to their keys

In addition to format strings that use format characters and format modifiers, Python strings
also include a **format method** that can be used in conjunction with a new **Formatter class**
to implement complex string formatting.

##### Control Structures

> algorithms require two important control structures: iteration and selection.

For iteration, Python provides a standard while statement and a very powerful for statement.
The while statement repeats a body of code as long as a condition is true.

The condition on the while statement is evaluated at the start of each repetition. If the condition is True, the body of the statement will
execute. It is easy to see the structure of a Python while statement due to the mandatory
indentation pattern that the language enforces.

The for statement can be used to iterate over the members of a collection, so long
as the collection is a sequence.

**Selection statements** allow programmers to ask questions and then, based on the result, perform
different actions. Most programming languages provide two versions of this useful construct:
the ifelse and the if

Selection constructs, as with any control construct, can be nested so that the result of one
question helps decide whether to ask the next.

Returning to lists, there is an alternative method for creating a list that uses iteration
and selection constructs. The is known as a **list comprehension**

>  A list comprehension allows you to easily create a list based on some processing or selection criteria.

##### Exception Handling

The other type of error, known as a logic error, denotes a situation where the program executes
but gives the wrong result. This can be due to an error in the underlying algorithm or an error in
your translation of that algorithm.

In some cases, logic errors lead to very bad situations such
as trying to divide by zero or trying to access an item in a list where the index of the item is
outside the bounds of the list. In this case, the logic error leads to a runtime error that causes
the program to terminate. These types of runtime errors are typically called **exceptions**.

Most of the time, beginning programmers simply think of exceptions as fatal runtime errors
that cause the end of execution. However, most programming languages provide a way to deal
with these errors that will allow the programmer to have some type of intervention if they so
choose. In addition, programmers can create their own exceptions if they detect a situation in
the program execution that warrants it.

> When an exception occurs, we say that it has been “raised.” You can “handle” the exception
that has been raised by using a **try** statement.

It is also possible for a programmer to cause a runtime exception by using the raise statement.

##### Object-Oriented Programming in Python

One of the most powerful features in an object-oriented programming language is the ability to allow a
programmer (problem solver) to create new classes that model data that is needed to solve the
problem.

> *Remember that we use abstract data types to provide the logical description of what a data
object looks like (its state) and what it can do (its methods). By building a class that implements
an abstract data type, a programmer can take advantage of the abstraction process and at the
same time provide the details necessary to actually use the abstraction in a program. Whenever
we want to implement an abstract data type, we will do so with a new class.*

The first method that all classes should provide is the constructor. The constructor defines the way in which data
objects are created.  In Python, the constructor method is always called **__init__**. 
