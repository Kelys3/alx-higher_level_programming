#!/usr/bin/python3
"""
This module describes a JSON string function that returns an object
(Python data structure)
"""

import json


def from_json_string(my_str):
    """this function returns an object represented by a JSON string
    Args:
        my_str (str) = the string
    Return:
        the object represented by a JSON string
    """
    return json.loads(my_str)
