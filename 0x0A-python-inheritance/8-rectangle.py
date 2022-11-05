#!/usr/bin/python3
"""defines a base Geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A representation of geometry class"""


class Rectangle(BaseGeometry):
    """creating a class rectangle"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
