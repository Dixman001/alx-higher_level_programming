#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """initializing the rectangle class
        args:
            width: represent the width of the rctangle
            height: represemts the heights of the rectangle
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than zoro
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retreives the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retreives the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
