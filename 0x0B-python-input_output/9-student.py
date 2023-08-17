#!/usr/bin/python3
"""Module description of to_json functiontat defines a student based
on certain instance attributes the Student class
"""


class Student:
    """
    This class defines a student by public
    instance attributes: first_name, last_name
    and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates first_name, last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns dictionary description """
        return self.__dict__.copy()
