#!/usr/bin/python3
""" This module describes a function that reads from a file """


def read_file(filename=""):
    """ this function reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
