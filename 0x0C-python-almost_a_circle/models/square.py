#!/usr/bin/python3
"""Define the class square."""
from .rectangle import Rectangle

class Square(Rectangle):
    """Define the constructor."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
