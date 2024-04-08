#!/usr/bin/python3
"""Define a class."""


class Rectangle:
    """Define the instantation method."""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """define the instantation module."""
    @property
    def width(self):
        return self.__width

    """setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """Define height module."""
    @property
    def height(self):
        return self.__height

    """Define the setter."""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
