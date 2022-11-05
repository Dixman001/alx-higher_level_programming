#!/usr/bin/python3
"""defines a base Geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
    """A representation of geometry class"""


class Rectangle(BaseGeometry):
    """creating a class rectangle"""

    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area():
        """returns the area of rectangle"""
        return sef.__width * self.__height

    def str():
        """string up"""
        string = "[" + str(self.__class__.__name__ + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
