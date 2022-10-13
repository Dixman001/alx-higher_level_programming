#!/usr/bin/python3
'''Define a square'''


class Square:
    '''square representation'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize square

        Args:
            size (int): represent the size of a square.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''get the current size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''get the current position of square'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if is instance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value


    def area(self):
        '''
        Calculate the area of square
        Returns: the size of square
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''prints the stdout of the square with character #'''
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(' ', end="") for j in range(0, self.__position[0])]
            [print('#', end="") for k in range(0, self.__size)]
            print("")
