#!/usr/bin/python3
""" class Square that define square"""


class Square:
    """ class Square that define square"""
    def __init__(self, size=0):
        """ init square

        Args:
            value (int): size of squar
        """
        self.size = size

    @property
    def size(self):
        """int: private size

        Returns:
            Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size int

        Args:
            value (int): size of square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of squar

    def area(self):
        """returns area

        Returns:
            area
        """
        return self.__size**2
