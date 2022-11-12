#!/bin/usr/python3
""" """


class Rectangle(base):
    """ """


    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @propery
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__width = value

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self):
        """ """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__x = value

    @property
    def y(self):
        """ """
        return seelf.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be integer")
        if value <= 0:
            raise ValueError("value must be  > 0")
        self.__y = value
