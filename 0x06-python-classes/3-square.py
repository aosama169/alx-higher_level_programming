#!/usr/bin/python3
""" class Squar that define square"""


class Square:
    """ class Square that define square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of squar

    def area(self):
        """returns area

        Returns:
            ares
        """
        return self.__size**2
