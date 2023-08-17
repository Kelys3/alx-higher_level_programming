#!/usr/bin/python3
"""This module describes a function that appends to a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file

    Args:
        filename: filename
        text: text to write
    Return:
        the number of characters added

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
