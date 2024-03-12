#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new Square

        Args:
            size (int): size of new Square.
            x (int): x coordinate of new Square.
            y (int): y coordinate of new Square.
            id (int): identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def __str__(self):
        """Return print() and str() representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
