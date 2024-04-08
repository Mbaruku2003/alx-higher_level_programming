#!/usr/bin/python3
"""Define a rectangle."""


class Rectangle:
    """Define an instance attribute."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        perlength = self.__height * 2
        perwidth = self.__width * 2
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (perlength + perwidth)

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return("")
        for heighting in range(0, self.__height):
            for widthing in range(0, self.__width):
                rect.append("#")
            if heighting != self.height - 1:
                print("\n")
            return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        print("Bye rectangle...")
