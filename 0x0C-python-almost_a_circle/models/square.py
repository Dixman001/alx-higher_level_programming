#!/usr/bin/python3
""" """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ """
        return self.__width

    @size.setter
    def size(self, value):
        """ """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            rise ValueError("size must be > 0")
        self.__width = value
        self.__height = value
