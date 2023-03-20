# Function and High-order functions

# question 1
# Write a function that takes an integer n as an argument and returns a list of n Fibonacci numbers.
# You can use the result.append() command to add the results of each loop to the list.
def fibonacci_list(n):
    """
    >>> fibonacci_list(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    "*** YOUR CODE HERE ***"



# question2.1
# Return the number of positive factors that n has.
def count_factors(n):
    """
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    "*** YOUR CODE HERE ***"



# question2.2
"""
Returns a function with one parameter N that counts all the numbers from 1 to N 
that satisfy the two-argument predicate function Condition, where
the first argument for Condition is N and the second argument is the number from 1 to N.
"""
def count_cond(condition):
    """
    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6
    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"



# question3
"""
Define a function cycle that takes in three functions f1, f2, f3, as arguments. 
cycle will return another function that should take in an integer argument n and return another function. 
That final function should take in an argument x and cycle through applying f1, f2, and f3 to x, 
depending on what n was. Here's what the final function should do to x for a few values of n:
n = 0, return x
n = 1, apply f1 to x, or return f1(x)
n = 2, apply f1 to x and then f2 to the result of that, or return f2(f1(x))
n = 3, apply f1 to x, f2 to the result of applying f1, and then f3 to the result of applying f2, or f3(f2(f1(x)))
n = 4, start the cycle again applying f1, then f2, then f3, then f1 again, or f1(f3(f2(f1(x))))
And so forth.
Hint: most of the work goes inside the most nested function.
"""
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"


