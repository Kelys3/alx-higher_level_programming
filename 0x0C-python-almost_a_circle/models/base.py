#!/usr/bin/python3
"""This module describes a class Base which is going to be the base for
all other classes
"""
import json
import csv
import tkinter
import turtle


class Base:
    """Defining the parent class. All other classes will inherit from it."""
    __nb_objects = 0
    """private class attribute"""
    def __init__(self, id=None):
        """class constructor defined with a public instance attribute id
        Args:
            id (int): a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        Return: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes JSON string representation of list_objs
        to a file
        Args:
            list_objs: list of instances that inherit from Base
        """

        filename = str(cls.__name__) + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: a string representing a list of dictionaries
        Return:
            a list representation, json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                json_list = Base.from_json_string(file.read())
                cls_instances = [cls.create(**cls_dict) for
                                 cls_dict in json_list]
                return cls_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of rectangles/squares as a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding="UTF-8") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads from csv
        """
        filename = cls.__name__ + ".csv"
        li = []
        try:
            with open(filename, "r", encoding="UTF-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    li.append(obj)
        except Exception:
            pass
        return li

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares."""
        turtle.Screen().screensize(800, 600)
        turtle.Screen().title("Turtle Drawing")
        turtle.speed(1)
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        t = turtle.Turtle()

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.color("blue")
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("green")
            for _ in range(4):
                t.forward(square.width)
                t.left(90)

        t.hideturtle()
        screen.mainloop()
