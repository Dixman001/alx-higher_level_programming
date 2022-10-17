#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle"""

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
        rectangle.number_of_instances += 1

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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__height, self.__width)

    def __del__(self):
        """prints a message for every deleted object"""
        print("Bye rectangle...")
        rectangle.number_of_instances -= 1
