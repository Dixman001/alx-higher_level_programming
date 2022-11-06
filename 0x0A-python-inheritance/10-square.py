#!/usr/bin/python3
"""defines a base Geometry"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """creating a class square"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area():
        """area define"""
        return self.__size * self.__size
