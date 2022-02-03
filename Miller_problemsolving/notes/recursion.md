## Recursion
> Recursion is a method of solving problems that involves breaking a problem down into smaller
and smaller subproblems until you get to a small enough problem that it can be solved trivially.
Usually recursion involves a function calling itself

**Example: Calculating the Sum of a List of Numbers**
Suppose that you want to calculate the sum of a list of numbers such as: [1, 3, 5, 7, 9].
How would you compute the sum of a list of numbers?

We might say the the sum of the list num_list is the sum of the first element of the list
(num_list[0]), and the sum of the numbers in the rest of the list (num_list[1 :]).
To state it in a functional form: list_sum(num_list) = first(num_list) + list_sum(rest(num_list))
In this equation first(num_list) returns the first element of the list and rest(num_list)
returns a list of everything but the first element.

### The Three Laws of Recursion

all recursive algorithms must obey three important laws:
1. A recursive algorithm must have a base case.

2. A recursive algorithm must change its state and move toward the base case.

3. A recursive algorithm must call itself, recursively.

First, a base case is the condition that allows the algorithm to stop recursing. A base
case is typically a problem that is small enough to solve directly. In the list_sum algorithm the
base case is a list of length 1.

To obey the second law, we must arrange for a change of state that moves the algorithm toward
the base case. A change of state means that some data that the algorithm is using is modified.

Usually the data that represents our problem gets smaller in some way

The final law is that the algorithm must call itself. This is the very definition of recursion

### Visualising Recursion

 it can still be difficult to find a mental model or a way of visualizing what is happening
in a recursive function. This can make recursion difficult for people to grasp

### Complex Recursive Problems

In this section we will look at some problems that are really difficult
to solve using an iterative programming style but are very elegant and easy to solve using
recursion

###### The Towers Of Hanoi
