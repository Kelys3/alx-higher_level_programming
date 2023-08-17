#!/usr/bin/python3

"""This module defines the class BaseGeometry."""


class BaseGeometry:
    """defines the class BaseGeometry."""

    def area(self):
        """Public instance method that raises an exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Another public instance method that validates the attribute value

        Args:
            name (str): The name of the parameter.
            value (int): The attribute to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
