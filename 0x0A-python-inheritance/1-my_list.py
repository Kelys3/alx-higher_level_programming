#!/usr/bin/python3
"""Defining a class MyList that inherits from list
"""


class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
        """a public instance method that prints the list, sorted in ascending
        order.
        all elements of the list are assumed to be of type int
        """
        print(sorted(self))
