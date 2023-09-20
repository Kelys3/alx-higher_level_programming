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

    def display(self):
        """public method that prints in stdout the Rectangle
        instance with the character #. x and y are not handled."""
        if self.width == 0 or self.height == 0:
            return
        for _ in range(self.y):
            print()
        for len in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()

    def __str__(self):
        """overriding the __str__ method to return [Rectangle] (<id>)
        <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """public method that updates the class Rectangle by assigning
        an argument to each attribute
        Args:
        *args (int): new arguments assigned to attributes
            1st argument = id attribute
            2nd argument = width attribute
            3rd argument = height attribute
            4th argument = x attribute
            5th argument = y attribute
        **kwargs (dict): key/value pairs of attributes
        """
        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    self.id = arg
                elif attr == 1:
                    self.width = arg
                elif attr == 2:
                    self.height = arg
                elif attr == 3:
                    self.x = arg
                elif attr == 4:
                    self.y = arg
                attr += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
