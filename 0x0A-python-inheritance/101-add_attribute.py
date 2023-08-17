#!/usr/bin/python3
"""This module describes a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """This function adds a new attribute to an object if it is possible.
    Args:
        obj (any): The object to add an attribute to.
        name (str): The name of the attribute.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
