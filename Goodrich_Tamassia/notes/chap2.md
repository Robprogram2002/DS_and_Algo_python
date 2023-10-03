## Object-Oriented-Programming

#### Object-Oriented Design Goal

Software implementations should achieve robustness, adaptability, and reusability.

**Robustness.** we want software to be robust, that is, capable of handling unexpected inputs that are not explicitly
defined for its application. For example, if a program is expecting a positive integer (perhaps representing the price
of an item) and instead is given a negative integer, then the program should be able to recover gracefully from this
error

**Adaptability.** Software needs to be able to evolve over time in response to changing conditions in its environment.
Thus, another important goal of quality software is that it achieves adaptability (also called **evolvability**).

**Reusability.**

#### Object-Oriented Design Principles

**Modularity.** Modern software systems typically consist of several components that must interact correctly in order
for the entire system to work properly. Modularity refers to an organizing principle in which different components of a
software system are divided into separate functional units.

Robustness is greatly increased because it is easier to test and debug separate components before they are integrated
into a larger software system. Furthermore, bugs that persist in a complete system might be traced to a particular
component, which can be fixed in relative isolation. The structure imposed by modularity also helps enable software
reusability. If software modules are written in a general way, the modules can be reused when related need arises in
other contexts.

**Abstraction.** Typically, describing the parts of a system involves naming them and explaining their functionality.
Applying the abstraction paradigm to the design of data structures gives rise to **abstract data types (ADTs)**. An ADT
is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them,
and the types of parameters of the operations. An ADT specifies **what** each operation does, but not **how** it does
it. We will typically refer to the collective set of behaviors supported by an ADT as its **public interface**

Python has a tradition of treating abstractions implicitly using a mechanism known as **duck typing**. As an interpreted
and dynamically typed language, there is no “compile time” checking of data types in Python, and no formal requirement
for declarations of abstract base classes. Instead, programmers assume that an object supports a set of known behaviors,
with the interpreter raising a run-time error if those assumptions fail.

More formally, Python supports abstract data types using a mechanism known as an **abstract base class (ABC)**. An
abstract base class cannot be instantiated , but it defines one or more common methods that all implementations of the
abstraction must have.

An ABC is realized by one or more **concrete classes** that inherit from the abstract base class while providing
implementations for those method declared by the ABC. Python’s abc module provides formal support for ABCs, although we
omit such declarations for simplicity. We will make use of several existing abstract base classes coming from Python’s
collections module.

**Encapsulation.** Different components of a software system should not reveal the internal details of their respective
implementations. One of the main advantages of encapsulation is that it gives one programmer freedom to implement the
details of a component, without concern that other programmers will be writing code that intricately depends on those
internal decisions. The only constraint on the programmer of a component is to maintain the public interface for the
component, as other programmers will be writing code that depends on that interface. Encapsulation yields robustness and
adaptability, for it allows the implementation details of parts of a program to change without adversely affecting other
parts, thereby making it easier to fix bugs or add new functionality with relatively local changes to a component.

With that said, Python provides only loose support for encapsulation.

#### Design Patterns

Computing researchers and practitioners have developed a variety of organizational concepts and methodologies for
designing quality object-oriented software that is concise, correct, and reusable.

A design pattern describes a solution to a “typical” software design problem. A pattern provides a general template for
a solution that can be applied in many different situations. It describes the main elements of a solution in an abstract
way that can be specialized for a specific problem at hand. It consists of a name, which identifies the pattern; a
context, which describes the scenarios for which this pattern can be applied; a template, which describes how the
pattern is applied; and a result, which describes and analyzes what the pattern produces.

These design patterns fall into two groups—patterns for solving algorithm design problems and patterns for solving
software engineering problems. The algorithm design patterns we discuss include the following:

• Recursion • Amortization • Divide-and-conquer • Prune-and-search, also known as decrease-and-conquer • Brute force •
Dynamic programming  
• The greedy method

Likewise, the software engineering design patterns we discuss include:

• Iterator • Adapter • Position • Composition • Template method • Locator • Factory method

### Software Development

Traditional software development involves several phases. Three major steps are:

1. Design
2. Implementation
3. Testing and Debugging

##### Design

In this step we decide how to divide the workings of our program into classes, we decide how these classes will
interact, what data each will store, and what actions each will perform. Indeed, one of the main challenges that
beginning programmers face is deciding what classes to define to do the work of their program. There are some rules of
thumb that we can apply when determining how to design our classes:

• **Responsibilities**: Divide the work into different **actors**, each with a different responsibility. Try to describe
responsibilities using action verbs. These actors will form the classes for the program.

• **Independence**: Define the work for each class to be as independent from other classes as possible. Subdivide
responsibilities between classes so that each class has autonomy over some aspect of the program. Give data (as instance
variables) to the class that has jurisdiction over the actions that require access to this data

• **Behaviors**: Define the behaviors for each class carefully and precisely, so that the consequences of each action
performed by a class will be well understood by other classes that interact with it. These behaviors will define the
methods that this class performs, and the set of behaviors for a class are the **interface** to the class, as these form
the means for other pieces of code to interact with objects from the class.

As the design takes form, a standard approach to explain and document the design is the use of **UML (Unified Modeling
Language) diagrams** to express the organization of a program. UML diagrams are a standard visual notation to express
object-oriented software designs. One type of UML figure is known as a **class diagram**.

##### Testing and Debugging

(here is left info)

### Class Definitions

A class serves as the primary means for abstraction in object-oriented programming.

##### Operator Overloading and Python’s Special Methods

Python’s built-in classes provide natural semantics for many operators. For example, the syntax a+b invokes addition for
numeric types, yet concatenation for sequence types. When defining a new class, we must consider whether a syntax like
a+b should be defined when a or b is an instance of that class.

the author of a class may provide a definition using a technique known as **operator overloading**. This is done by
implementing a specially named method. In particular, the `+` operator is overloaded by implementing a method
named `__add-__`, which takes the right-hand operand as a parameter and which returns the result of the expression. That
is, the syntax, `a+b`, is converted to a method call on object `a` of the form, `a.__add__(b)`. Similar specially named
methods exist for other operators.

When a binary operator is applied to two instances of different types, as in 3 love me , Python gives deference to the
class of the *left* operand. In this example, it would effectively check if the int class provides a sufficient
definition for how to multiply an instance by a string, via the `__mull__` method. However, if that class does not
implement such a behavior, Python checks the class definition for the right-hand operand, in the form of a special
method named `__rmul__` (i.e., “right multiply”). This provides a way for a new user-defined class to support mixed
operations that involve an instance of an existing class (given that the existing class would presumably not have
defined a behavior involving this new class).

In addition to traditional operator overloading, Python relies on specially named methods to control the behavior of
various other functionality, when applied to user-defined classes. For example, the syntax, `str(foo)`, is formally a
call to the constructor for the string class. Of course, if the parameter is an instance of a user defined class, the
original authors of the string class could not have known how that instance should be portrayed. So the string
constructor calls a specially named method, `foo.__str__()`, that must return an appropriate string representation.

Similar special methods are used to determine how to construct an int, float, or bool based on a parameter from a
user-defined class. The conversion to a Boolean value is particularly important, because the syntax, if foo:, can be
used even when foo is not formally a Boolean value

Several other top-level functions rely on calling specially named methods. For example, the standard way to determine
the size of a container type is by calling the top-level len function. Note well that the calling syntax, len(foo), is
not the traditional method-calling syntax with the dot operator. However, in the case of a user-defined class, the
top-level len function relies on a call to a specially named len method of that class. That is, the call len(foo) is
evaluated through a method call, foo. len ( ). When developing data structures, we will routinely define the len method
to return a measure of the size of the structure.

**Implied Methods.** As a general rule, if a particular special method is not implemented in a user-defined class, the
standard syntax that relies upon that method will raise an exception. However, there are some operators that have
default definitions provided by Python, in the absence of special methods, and there are some operators whose
definitions are derived from others.

> if a container class provides implementations for both len and getitem , a default iteration is provided automatically  
> Furthermore, once an iterator is defined, default functionality of contains is provided.

##### Iterators

In short, an iterator for a collection provides one key behavior: It supports a special method named next that returns
the next element of the collection, if any, or raises a StopIteration exception to indicate that there are no further
elements. Fortunately, it is rare to have to directly implement an iterator class. Our preferred approach is the use of
the generator syntax, which automatically produces an iterator of yielded values

### Inheritance

A hierarchical design is useful in software development, as common functionality can be grouped at the most general
level, thereby promoting reuse of code, while differentiated behaviors can be viewed as extensions of the general case,
In object-oriented programming, the mechanism for a modular and hierarchical organization is a technique known as
**inheritance**. This allows a new class to be defined based upon an existing class as the starting point. In
object-oriented terminology, the existing class is typically described as the **base class, parent class, or
superclass**, while the newly defined class is known as the **subclass** or **child class**.

There are two ways in which a subclass can differentiate itself from its superclass. A subclass may specialize an
existing behavior by providing a new implementation that **overrides** an existing method. A subclass may also **
extend**
its superclass by providing brand-new methods.

Another example of a rich inheritance hierarchy is the organization of various exception types in Python. y. The
**BaseException** class is the root of the entire hierarchy, while the more specific **Exception** class includes most
of the error types that we have discussed. Programmers are welcome to define their own special exception classes to
denote errors that may occur in the context of their application. Those user-defined exception types should be declared
as subclasses of Exception.

**Note.** Our `PredatoryCreditCard` subclass directly accesses the data `memberself._balance`, which was established by
the parent `CreditCard` class. The underscored name, by convention, suggests that this is a *nonpublic* member, so we
might ask if it is okay that we access it in this fashion. While general users of the class should not be doing so, our
subclass has a somewhat privileged relationship with the superclass. Several object-oriented languages (e.g., Java, C++)
draw a distinction for nonpublic members, allowing declarations of **protected** or **private** access modes. Members
that are declared as protected are accessible to subclasses, but not to the general public, while members that are
declared as private are not accessible to either. In this respect, we are using balance as if it were protected (but not
private).

Python does not support formal access control, but names beginning with a single underscore are conventionally akin to
protected, while names beginning with a double underscore (other than special methods) are akin to private. In choosing
to use protected data, we have created a dependency in that our `PredatoryCreditCard` class might be compromised if the
author of the `CreditCard` class were to change the internal design.

### Namespaces and Object-Orientation

A **namespace** is an abstraction that manages all of the identifiers that are defined in a particular scope, mapping
each name to its associated value. In Python, functions, classes, and modules are all first-class objects, and so the
“value” associated with an identifier in a namespace may in fact be a function, class, or module.

**Instance namespace.** Manages attributes specific to an individual object.

There is a separate **class namespace** for each class that has been defined. This namespace is used to manage members
that are to be shared by all instances of a class, or used without reference to any particular instance.

A class-level data member is often used when there is some value, such as a constant, that is to be shared by all
instances of a class. In such a case, it would be unnecessarily wasteful to have each instance store that value in its
instance namespace.

It is also possible to nest one class definition within the scope of another class. This is a useful construct, which we
will exploit several times in this book in the implementation of data structures. Nesting one class in the scope of
another makes clear that the nested class exists for support of the outer class. Furthermore, it can help reduce
potential name conflicts, because it allows for a similarly named class to exist in another context (for example
different nested node classes for a linked list or a tree )

Another advantage of one class being nested as a member of another is that it allows for a more advanced form of
inheritance in which a subclass of the outer class overrides the definition of its nested class

In traditional object-oriented terminology, Python uses what is known as dynamic dispatch (or dynamic binding) to
determine, at run-time, which implementation of a function to call based upon the type of the object upon which it is
invoked. This is in contrast to some languages that use static dispatching, making a compile-time decision as to which
version of a function to call, based upon the declared type of a variable

### Shallow and Deep Copying

Python provides a very convenient module, named copy, that can produce both shallow copies and deep copies of arbitrary
objects. This module supports two functions: the copy function creates a shallow copy of its argument, and the deepcopy
function creates a deep copy of its argument.