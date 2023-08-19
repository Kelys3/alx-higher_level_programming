#!/usr/bin/python3
"""This module defines a class Rectangle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiaiation with private instance attributes width, height
        x, y and id inherited from Base. id will be called with super() to
        be able to use it.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """public method that returns the area value of the Rectangle
        instance"""
        return self.height * self.width

