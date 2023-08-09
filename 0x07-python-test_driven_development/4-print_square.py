#!/usr/bin/python3
"""

This module contains a function that prints a square with the character #

"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size length of the square

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer
                   If size is a float
                   If size is less than 0
        
        ValueError: If size is less than 0



    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
