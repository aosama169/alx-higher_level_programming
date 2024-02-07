#!/usr/bin/python3.5
"""

composed by a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies two matrices

    Args:
        m_a: matrix a1
        m_b: matrix b1

    Returns:
        result of the multiply

    """

    return (np.matmul(m_a, m_b))
