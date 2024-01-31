#!/usr/bin/python3
"""

This module is a function that divides the numbers of matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the numbers of a matrix

    Args:
        matrix: list of a lists of numbers
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: numbers aren't lists
                   numbers aren't integers/floats
                   If div is not an integer/float number
                   If lists of the matrix don't have same size

        ZeroDivisionError: If div by is zero

    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for numb in elems:
            if not type(numb) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
