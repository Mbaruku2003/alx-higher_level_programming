#!/usr/bin/python3
"""Define the class."""
from .base import Base


class Rectangle(Base):
    """Define rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Define rectangle."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Define rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Define rectangle."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Define rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Define rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Define rectangle."""

        return self.__x

    @x.setter
    def x(self, value):
        """Define rectangle."""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Define rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        """Define rectangle."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Define rectangle."""

        return (self.__height * self.__width)

    def display(self):
        """Define rectangle."""

        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Define rectangle."""

        return ("[Rectangle] " + "{} {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Define rectangle."""

        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.__width = value
                if index == 2:
                    self.__height = value
                if index == 3:
                    self.__x = value
                if index == 4:
                    self.__y = value
                else:
                    continue
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """Define rectangle."""

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
