#!/usr/bin/python3
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

    def area(self):
        """ """
        return self.width * self.height

    def display(self):
        """ """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
                {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is none:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        def to_dictionary(self):
            """ """

            return {"id": self.id, "width": self.width,
                    "height": self.height, "x": self.x,
                    "y": self.y}
