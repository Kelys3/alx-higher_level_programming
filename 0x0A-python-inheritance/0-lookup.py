#!/usr/bin/python3
"""this module returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """a function that returns the list of available attributes"""
    return dir(obj)
