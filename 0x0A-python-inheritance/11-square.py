#!/usr/bin/python3
"""This module describes a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining class Square."""

    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): The size of the new square.
            size is a private attribute
            size is a positive integer validated by
            integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """implementing the area method"""
        return (self.__size ** 2)

    def __str__(self):
        """Implementing print() and str() to return the Square description
        [Square] <width>/<height>
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
