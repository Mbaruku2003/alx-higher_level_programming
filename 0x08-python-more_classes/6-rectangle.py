#!/usr/bin/python3
"""Define a class."""


class Rectangle:
    """Define an instance."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
        return (self.__height * self.__width)

    def perimeter(self):
        heighting = self.__height * 2
        widthing = self.__width * 2
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (heighting + widthing)

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for j in range(self.__height):
            for k in range(self.__width):
                rect.append("#")
            if j != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
