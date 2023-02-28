def falling(n, k):
    """Compute the falling factorial of n to depth k."""
    "*** YOUR CODE HERE ***"
    result = 1
    for i in range(k):
        result *= n
        n -= 1
    return result

print(falling(6,3))