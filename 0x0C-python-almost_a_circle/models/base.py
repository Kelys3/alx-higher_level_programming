#!/usr/bin/python3
"""This module describes a class Base which is going to be the base for
all other classes
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        Return: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            json.dumps(list_dictionaries)
