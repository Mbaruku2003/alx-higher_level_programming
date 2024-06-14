#!/usr/bin/python3
"""Defines a class."""


class Square:
    """defining an instant"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the valu of size."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the position."""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value."""

        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Define the area."""

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
