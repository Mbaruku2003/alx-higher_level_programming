#!/usr/bin/python3
"""Define our class."""
import json

class Base:
    """ Define the private attribute."""

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
