#!/usr/bin/python3

"""Define base geometry class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as an int

        Args:
            name (str): The name of parameter
            value (int): The parameter to validate
        Raises:
            TypeError: If value is not int
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
