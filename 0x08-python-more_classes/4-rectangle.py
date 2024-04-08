#!/usr/bin/python3
"""Define a class."""


class Rectangle:
    """Define the attributes."""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        per_length = self.__width * 2
        per_height = self.__height * 2
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return per_length + per_height

    def __str__(self):
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for widthing in range(self.__width):
            for heighting in range(self.__height):
                rect.append("#")
            if widthing != self.__width - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
