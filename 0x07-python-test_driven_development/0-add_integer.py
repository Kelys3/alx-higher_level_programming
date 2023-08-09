#!/usr/bin/python3
"""

This is a module created to write a function that adds two integers

"""


def add_integer(a, b=98):
    """ Function that adds two integers and/or floats

    Args:
        a: first number
        b: second number

    Returns:
        The sum of the two given integers and/or floats 

    Raises:
        TypeError: If a or b are not integers and/or floats

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
