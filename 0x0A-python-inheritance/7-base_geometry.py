#!/usr/bin/python3
"""defines a base Geometry"""


class BaseGeometry:
    """A representation of geometry class"""

    def area(self):
        """exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
