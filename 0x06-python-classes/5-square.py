#!/usr/bin/python3
'''Define a square'''


class Square:
    '''square representation'''

    def __init__(self, size=0):
        '''Initialize square

        Args:
            size (int): represent the size of a square.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

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

    def area(self):
        '''
        Calculate the area of square
        Returns: the size of square
        '''

        return (self.__size ** 2)

    def my_print(self):
        '''prints the stdout of the square with character #'''
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print('#' * self.__size)
