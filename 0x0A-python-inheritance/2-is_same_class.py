#!/usr/bin/python3
"""This module defines the function is_same_class
"""


def is_same_class(obj, a_class):
    """this function returns True if the object is exactly an instance of the
    specified class; otherwise False
    """
    return (type(obj) == a_class)
