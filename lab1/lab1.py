# Python basics(if,for,while)
# question 1
"""
Write a function falling, which is a "falling" factorial that takes two arguments, n and k, 
and returns the product of k consecutive numbers, starting from n and working downwards.
When k is 0, the function should return 1.
"""
def falling(n, k):
    """
    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"



# question 2
# Write a function that takes in a nonnegative integer and sums its digits. 
# (Using floor division and modulo might be helpful here!)
def sum_digits(y):
    """
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"



# question 3.1
# Write a function that takes in a number and determines if the digits contain two adjacent 8s.
def double_eights1(n):
    """
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"



# question 3.2
# Try another way to solve problem3.1
def double_eights2(n):
    "*** YOUR CODE HERE ***"


