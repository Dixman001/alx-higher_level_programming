#!/usr/bin/python3
'''Define a square'''


class Square:
    '''square representation'''

    def __init__(self, size=0):
        '''Initialize square

        Args:
            size (int): represent the size of a square.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''return the area'''
        return (self.__size * self.__size)
