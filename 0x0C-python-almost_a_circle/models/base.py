#!/usr/bin/python3
"""This module describes a class Base which is going to be the base for
all other classes
"""


class Base:
    """Defining the parent class. All other classes will inherit from it."""
    __nb_objects = 0
    """private class attribute"""
    def __init__(self, id=None):
        """class constructor defined with a public instance attribute id
        Args:
            id (int): a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
