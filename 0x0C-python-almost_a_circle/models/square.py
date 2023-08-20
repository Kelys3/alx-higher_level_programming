#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square defined"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation with private attributes size, x and y. id is
        inherited from Base. all attributes are inherited from rectangle.
        To access attributes we use the super() call to
        instantiate the Rectangle method.
        width and height are assigned to size
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """overloading string method"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update the class by assigning attributes
        Args:
        *args: list of arguments-no-keyworded arguments
            1st arg = id
            2nd arg = size
            3rd arg = x
            4th arg = y
        **kwargs (dict): with key/value pairs. if *args exists
        and is not empty, **kwargs is skipped.
        """
        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    self.id = arg
                elif attr == 1:
                    self.size = arg
                elif attr == 2:
                    self.x = arg
                elif attr == 3:
                    self.y = arg
                attr += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
