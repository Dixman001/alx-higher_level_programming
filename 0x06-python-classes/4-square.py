#!/usr/bin/python3
'''Define a square'''


class Square:
    '''square representation'''

    def __init__(self, size=0):
        '''Initialize square

        Args:
            size (int): represent the size of a square.
        '''
        self.size = size

    @property
    def size(self):
        '''get the current size of square'''
        return (self__.size)

    @size.setter
    def size(self, value)
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''return the area'''
        return (self.__size * self.__size)
