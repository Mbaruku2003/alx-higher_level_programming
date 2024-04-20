#!/usr/bin/python3
"""Define the class square."""
from .rectangle import Rectangle

class Square(Rectangle):
    """Define the constructor."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.size = value
                if index == 2:
                   self.x = value
                if index == 3:
                    self.y = value
                else:
                    continue
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y =  value
                else:
                    break

    def to_dictionary(self):
        dictionary = {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
        return dictionary
