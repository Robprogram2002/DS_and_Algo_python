def test1():
    l = []

    for i in range(1000):
        l = l + [i]


def test2():
    l = []

    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


# To capture the time it takes for each of our functions to execute we will use Python’s timeit
# module. The timeit module is designed to allow Python developers to make cross-platform
# timing measurements by running functions in a consistent environment and using timing mechanisms that are as similar
# as possible across operating systems.

# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

# If the above line is excluded, you need to replace Timer with
# timeit.Timer when defining a Timer object
t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")
