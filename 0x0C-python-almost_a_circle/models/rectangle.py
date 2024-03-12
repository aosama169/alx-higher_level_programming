#!/usr/bin/python3
"""Define rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
            x (int): x coordinate of new Rectangle.
            y (int): y coordinate of new Rectangle.
            id (int): identity of new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set get x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set get y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#` character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle

        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key value pairs of attributes
        """
        if args and len(args) != 0:
            tmp = 0
            for arg in args:
                if tmp == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif tmp == 1:
                    self.width = arg
                elif tmp == 2:
                    self.height = arg
                elif tmp == 3:
                    self.x = arg
                elif tmp == 4:
                    self.y = arg
                tmp += 1

        elif kwargs and len(kwargs) != 0:
            for ky, val in kwargs.items():
                if ky == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif ky == "width":
                    self.width = val
                elif ky == "height":
                    self.height = val
                elif ky == "x":
                    self.x = val
                elif ky == "y":
                    self.y = val

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
