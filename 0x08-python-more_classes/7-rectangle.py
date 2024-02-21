#!/usr/bin/python3
""" class Rectangle that define rectangle
"""


class Rectangle:
    """ class rectangles"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instante with option width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ rectangle with the char int
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance of Rectangle deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
