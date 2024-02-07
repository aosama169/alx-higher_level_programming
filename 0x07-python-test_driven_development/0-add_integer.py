#!/usr/bin/python3
"""

This module has a function adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer

    Args:
        a: first num
        b: second num

    Returns:
        The addition of the two numbers

    Raises:
        TypeError: If a or b are not integer

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
