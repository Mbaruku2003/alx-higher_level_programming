#!/usr/bin/python3
"""Define a class."""


class Rectangle:
    """Define the instantation method."""

    def __init__(self, width=0, height=0):
        """Initialises a new rectangle.

        Args:
        @width (int): the width of new triangle.
        @height: the height of the height of the new triangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
