# question1
# Return a list of two-element lists in which the i-th element is [s[i], t[i]].
def couple(s, t):
    """
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    return [[a, b] for a, b in zip(s, t)]

# question2
# Design a function that returns the values of the largest and second largest elements in the incoming list 
# and returns them as tuples.
def largest_and_second(x):
    """
    >>> t = [1, 3, 5, 7, 10]
    >>> largest_and_second(t)
    (10, 7)
    """
    assert len(x) >= 2
    "*** YOUR CODE HERE ***"
    m1, m2 = (x[0], x[1]) if  x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:    
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return (m1, m2)