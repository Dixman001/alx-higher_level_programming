#!/usr/bin/python3
"""
this module prints a square

"""


def print_square(size):
    '''This function prints a square using the character #

    Args:
        size (int)

    raises:
        TypeError: if a sizenis not an int
        TypeError: if size is a float and less than zero
        VaalueError: if size is less than zero
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for a in range(0, size):
        for b in range(size):
            print("#", end="")
        print("")
