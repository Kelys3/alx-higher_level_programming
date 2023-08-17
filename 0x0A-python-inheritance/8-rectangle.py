#!/usr/bin/python3
"""This module describes the class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a subclass that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height
        Args:
        width (int): the breadth of the Rectangle
        height (int): the length of the Rectangle
        width and height are private instance attributes
        width and height are positive integers validated
        by integer_validator
        """
        super().integer_validator('height', height)
        self.__height = height
        super().integer_validator('width', width)
        self.__width = width
