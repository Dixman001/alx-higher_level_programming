#!/usr/bin/python3
"""defines a base Geometry"""


Rectangle = __import__('9-rectangle.py').Rectangle
"""A representation of Square class"""


class Square(Rectangle):
    """creating a class square"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
