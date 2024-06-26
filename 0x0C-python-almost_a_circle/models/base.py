#!/usr/bin/python3
"""Define our class."""
import json
import csv
from turtle import *


class Base:
    """Define the private attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as afile:
            if list_objs is None:
                afile.write("[]")
            else:
                new_list = []
                for objects in list_objs:
                    new_list.append(objects.to_dictionary())
                afile.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        with open(filename, "r") as csvf:
            if list_objs is None or list_objs ==[]:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        for obj in list_objs:
            writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r") as csvf:
                if cls.__name__ == "rectangle":
                    instance = ["id", "width", "height", "x", "y"]
                else:
                    instance = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvf, instance=instance)
                new_list_dicts = []
                converted_dict = []
                for i in list_dicts:
                    for key, value in i.items():
                        converted_dict[key] = int(value)
                    new_list_dicts.append(converted_dict)
                list_dicts = new_list_dicts
                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls, create(**d))
                return list_of_instances

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = Screen()
        screen.title("Rectangles and Squares")
        #create a turtle object
        turt = Turtle()

        #Draw Rectangles
        for rect in list_rectangles:
            turt = penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            turt.color("blue")
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
        for square in list_squares:
            turt.penup()
            turt.goto(square.x, square.y)
            turt.pendown()
            turt.color("red")
            for _ in range(4):
                turt.forward(square.size)
                turt.left(90)
        turt.hideturtle()
        screen.mainloop()
