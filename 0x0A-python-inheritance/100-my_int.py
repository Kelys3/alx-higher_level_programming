#!/usr/bin/python3
""" this module describes a class MyInt that inherits from int"""


class MyInt(int):
    """ Defining class MyInt. A rebel that has == and != inverted"""

    def __init__(self, value):
        """instantiation with value"""
        self.value = value

    def __eq__(self, other):
        """reverses the equal to method. That means what
        was == now becomes !=
        """
        return self.value != other

    def __ne__(self, other):
        """reverses the not equal to method. That means what was != now
        becomes ==
        """
        return self.value == other
