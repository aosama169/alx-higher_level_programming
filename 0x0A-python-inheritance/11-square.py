#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tu Feb 6 2024

@author: Ahmed Osama
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    Square class shape inheirt from Base Geometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with and height

        Returns:
            Return width and height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        function that calculates area of the Square
        """
        return self.__size ** 2
