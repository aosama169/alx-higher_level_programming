#!/usr/bin/python3
""" empty class Rectangle define rectangle
"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height int"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width int
        """
        return self.__width

    @property
    def height(self):
        """ height int
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ rectangle area int"""
        return self.__width * self.__height

    def perimeter(self):
        """ rectangle perimiter int"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
