#!/usr/bin/python3
"""
This class module prevents the creation of new instance attributes.
"""


class LockedClass:
    """
    A class that  prevents the creation of new instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Instance Initiation"""
        pass
