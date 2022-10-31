#!/usr/in/python3
def add_integer(a, b=98):
    """Return the sum of two integers
    Args:
        a: arg 1
        b: arg 2
    Return:
        the sum of two args
    Raises:
        TypeError if any args is not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
