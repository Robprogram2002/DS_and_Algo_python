## Algorithm Analysis

we are interested in the design of “good” data structures and algorithms. Simply put, a **data structure** is a
systematic way of organizing and accessing data, and an **algorithm** is a step-by-step procedure for performing some
task in a finite amount of time. These concepts are central to computing, but to be able to classify some data
structures and algorithms as “good,” we must have precise ways of analyzing them.

Running time is a natural measure of “goodness,” since time is a precious resource—computer solutions should run as fast
as possible. In general, the running time of an algorithm or data structure operation increases with the input size,
although it may also vary for different inputs of the same size. Also, the running time is affected by the hardware
environment (e.g., the processor, clock rate, memory, disk) and software environment (e.g., the operating system,
programming language) in which the algorithm is implemented and executed.

We are interested in characterizing an algorithm’s running time as a function of the input size. But what is the proper
way of measuring it?

To analyze the running time of an algorithm without performing experiments, we perform an analysis directly on a
high-level description of the algorithm. We define a set of primitive operations such as the following:

- Assigning an identifier to an object
- Determining the object associated with an identifier
- Performing an arithmetic operation (for example, adding two numbers)
- Comparing two numbers
- Accessing a single element of a Python list by index
- Calling a function (excluding operations executed within the function)
- Returning from a function.

Formally, a primitive operation corresponds to a low-level instruction with an execution time that is constant. Ideally,
this might be the type of basic operation that is executed by the hardware, although many of our primitive operations
may be translated to a small number of instructions. Instead of trying to determine the specific execution time of each
primitive operation, we will simply count how many primitive operations are executed, and use this number t as a measure
of the running time of the algorithm.

This operation count will correlate to an actual running time in a specific computer, for each primitive operation
corresponds to a constant number of instructions, and there are only a fixed number of primitive operations. The
implicit assumption in this approach is that the running times of different primitive operations will be fairly similar.
Thus, the number, t, of primitive operations an algorithm performs will be proportional to the actual running time of
that algorithm.

> To capture the order of growth of an algorithm’s running time, we will associate, with each algorithm, a function f(n)
> that characterizes the number of primitive operations that are performed as a function of the input size n

An algorithm may run faster on some inputs than it does on others of the same size. Thus, we may wish to express the
running time of an algorithm as the function of the input size obtained by taking the average over all possible inputs
of the same size. Unfortunately, such an average-case analysis is typically quite challenging. Therefore, we will
characterize running times in terms of the worst case of the algorithm.

In algorithm analysis, we focus on the growth rate of the running time as a function of the input size n, taking a
“big-picture” approach.