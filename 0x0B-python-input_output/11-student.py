#!/usr/bin/python3
"""Module description of to_json function that defines a student based
on certain instance attributes of the Student class
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

    def to_json(self, attrs=None):
        """ Method that returns dictionary description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            result = {}

            for name in range(len(attrs)):
                for elm in obj:
                    if attrs[name] == elm:
                        result[elm] = obj[elm]
            return result

        return obj

     def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]    
