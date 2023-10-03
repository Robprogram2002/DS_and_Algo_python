# A very common example to show the details of implementing a user-defined class is to construct
# a class to implement the abstract data type Fraction.

# A fraction such as 3/5 consists of two parts. The top value, known as the numerator, can be
# any integer. The bottom value, called the denominator, can be any integer greater than 0 (negative fractions have a
# negative numerator). Although it is possible to create a floating point approximation for any fraction, in this case
# we would like to represent the fraction as an exact value.

# The operations for the Fraction type will allow a Fraction data object to behave like any
# other numeric value. We need to be able to add, subtract, multiply, and divide fractions. We
# also want to be able to show fractions using the standard “slash” form

#  In addition, all fraction methods should return results in their lowest terms so that no matter what
# computation is performed, we always end up with the most common form.

class Fraction:
    # self is a special parameter that will always be used as a reference back to the object itself. It must
    # always be the first formal parameter; however, it will never be given an actual parameter value
    # upon invocation.
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # The notation self.num in the constructor defines the fraction object
    # to have an internal data object called num as part of its state. Likewise, self.den creates
    # the denominator. The values of the two formal parameters are initially assigned to the state,
    # allowing the new fraction object to know its starting value.


# To create an instance of the Fraction class, we must invoke the constructor. This happens
# by using the name of the class and passing actual values for the necessary state
# (Note that we never actually invoke **__init__**)

my_fraction = Fraction(3, 5)

# The next thing we need to do is implement the behavior that the abstract data type requires. Let's see what is return
# if we print the variable

print(my_fraction)


# The Fraction object, does not know how to respond to this request to print. The print
# function requires that the object convert itself into a string so that the string can be written to the
# output

# The only choice my_fraction has is to show the actual reference that is stored in the variable
# (the address itself). This is not what we want

# There are two ways we can solve this problem. One is to define a method called show that will
# allow the Fraction object to print itself as a string.

# Unfortunately, this does not work in general. In order
# to make printing work properly, we need to tell the Fraction class how to convert itself into
# a string. This is what the print function needs in order to do its job.

# In Python, all classes have a set of standard methods that are provided but may not work properly. One of these,
# __str__, is the method to convert an object into a string. The default implementation for this method is to return
# the instance  address string as we have already seen.

# What we need to do is provide a “better” implementation for this method. We will say that this
# implementation OVERRIDES the previous one, or that it redefines the method’s behavior.

# To do this, we simply define a method with the name __str__ and give it a new implementation.


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # @overrides
    def __str__(self):
        return str(self.num) + "/" + str(self.den)


my_f = Fraction(3, 5)
print("I ate", my_f, "of the pizza")
print(my_f.__str__())
print(my_f)

# We can override many other methods for our new Fraction class. Some of the most
# important of these are the basic arithmetic operations. We would like to be able to create two
# Fraction objects and then add them together using the standard “+” notation

# At this point, if we try to add two fractions, we will get an error.

fraction1 = Fraction(1, 3)
fraction2 = Fraction(1, 4)


# print(fraction1 + fraction2)  # remove comment to see the error message

# If you look closely at the error, you see that the problem is that the “+” operator does not
# understand the Fraction operands. We can fix this by providing the Fraction class with a
# method that overrides the addition method. In Python, this method is called __add__ and it
# requires two parameters. The first, self, is always needed, and the second represents the other
# operand in the expression.


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        #  The addition function returns a new Fraction
        # object with the numerator and denominator of the sum
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)


# In order to be sure that our results are always in the lowest terms, we need a helper
# function that knows how to reduce fractions. This function will need to look for the greatest
# common divisor, or GCD. We can then divide the numerator and the denominator by the GCD
# and the result will be reduced to lowest terms.

# The best-known algorithm for finding a greatest common divisor is Euclid’s Algorithm
# We will simply provide an iterative implementation here.


def gcd(m, n):
    while m % n != 0:
        old_n = n
        old_m = m

        m = old_n
        n = old_m % old_n

    return n


print(gcd(20, 10))


# Note that this implementation of the GCD algorithm only works when
# the denominator is positive. This is acceptable for our fraction class because we have said that
# a negative fraction will be represented by a negative numerator.

# Now we can use this function to help reduce any fraction.


def __add__(self, other_fraction):
    new_num = self.num * other_fraction.den + self.den * other_fraction.num
    new_den = self.den * other_fraction.den
    common = gcd(new_num, new_den)
    return Fraction(new_num // common, new_den // common)


# Assume we have two Fraction objects, f1 nd f2. f1 == f2 will only be True if they are references to the same object.
# Two different objects with the same numerators and denominators would not be equal under this implementation
# This is called **shallow equality**

# We can create **deep equality**  –- equality by the same value, not the same reference -- by overriding the __eq__
# method. The __eq__ method is another standard method available in any class. The __eq__ method compares two objects
# and returns True if their values are the same, False otherwise

# (Note : there are other relational operators that can be overridden. For example,
# the __le__ method provides the less than or equal functionality)

# Remember Shallow-equality vs Deep-equality

# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
# is better if all fractions are reduced to lower terms right from the start when they are created

def check_parameter_sanity(value, is_denominator):
    if not isinstance(value, int):
        raise RuntimeError("Constructor parameters must be of type integer")
    elif is_denominator is True and value <= 0:
        raise RuntimeError("Denominator parameter cannot be lower or equal to zero")
    return


class Fraction:

    def __init__(self, top, bottom):
        check_parameter_sanity(top, False)
        check_parameter_sanity(bottom, True)
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def show(self):
        print(self.num, "/", self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def set_num(self, number):
        check_parameter_sanity(number, False)
        self.num = number

    def set_den(self, number):
        check_parameter_sanity(number, True)
        self.den = number

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den  # (a/b)/(c/d) = (a/b)(d/c)
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __lt__(self, other_fraction):
        # a/b < c/d if and only if ad < bc
        return self.num * other_fraction.den < self.den * other_fraction.num

    def __gt__(self, other):
        # a/b > c/d if and only if ad > bc
        return self.num * other.den > self.den * other.num

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


if __name__ == '__main__':
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    z = Fraction(2, 4)
    print(x + y)
    print(x == y)
    print(x == z)
    print(x >= y)
    print(x <= y)
    print(x - y)
    print(x * y)
    print(x / y)

    # fraction1 = Fraction(2, -4)
    # fraction2 = Fraction(23, 0)
    # fraction3 = Fraction("something great", 123)

    print(x.get_den())
    print(y.get_num())
    z.set_num(-2)
    # z.set_den(0)
    z.set_den(20)
    print(z)
