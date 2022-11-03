#!/usr/bin/python3
"""
this module prints a full name

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name> <last name>)

    Args:
        first_name (str)
        last_name (str)

    raises:
        TypeError: if a name is not string
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"my name is {first_name} {last_name}")
