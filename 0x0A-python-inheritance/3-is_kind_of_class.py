#!/usr/bin/python3
"""This module defines the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    this function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class which is a_class.
    Otherwise this function should return False
    """
    return isinstance(obj, a_class)
