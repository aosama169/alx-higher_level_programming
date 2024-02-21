#!/usr/bin/python3
""" empty class Rectangle that define rectangle
"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instante optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width int
        """
        return self.__width

    @property
    def height(self):
        """height int
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
