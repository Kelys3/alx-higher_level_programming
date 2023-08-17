#!/usr/bin/python3
"""This module describes a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object

    Args:
        my_obj (str): object
    Return:
        the JSON representation of an object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
