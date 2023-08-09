#!/usr/bin/python3
"""

This module is contains a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
        Elements in the matrix must be either integers or floats

    Args:
        matrix: list of a lists of integers or floats
        div: a number(integer or float) which divides the matrix

    Returns:
        A new matrix

    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elements of the lists are not integers/floats
                   If div is not an integer/float number
                   If the row of the matrix are not of the same size

        ZeroDivisionError: If div is zero


    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    size_count = 0
    msg_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(error_msg)

        if size_count != 0 and len(elements) != size_count:
            raise TypeError(msg_size)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(error_msg)

        size_count = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
