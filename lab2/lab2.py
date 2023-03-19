# Lambda

# question 1
"""
Define a function that squares all the even numbers in a given list and returns the new list.
Using the lambda function and you can use the map function.
"""
def square_even_numbers(n):
    """
    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> square_even_numbers(numbers)
    [4, 16, 36, 64]
    """
    "*** YOUR CODE HERE ***"
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, n)))


# question 2
"""
Doubles all even elements and adds 1 to all odd elements in a list of integers.
Using the lambda function and you can use the map function.
"""
def rule_numbers(n):
    """
    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> rule_numbers(numbers)
    [2, 4, 4, 8, 6, 12, 8, 16, 10]
    """
    "*** YOUR CODE HERE ***"
    return list(map(lambda x: x * 2 if x % 2 == 0 else x + 1, n))


# question3
"""
Write a function lambda_curry2 that will curry any two argument function using lambdas.
Refer to the textbook for more details about currying.
"""
def lambda_curry2(func):
    """
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)