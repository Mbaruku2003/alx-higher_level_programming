#!/usr/bin/python3
"""Defines a class."""


class Square:
    """defining an instant"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the valu of size."""

        return self._size

    @size.setter
    def size(self, value):
        """Sets the value of size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        """Gets the position."""

        return self._position

    @position.setter
    def position(self, value):
        """Sets the position value."""

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Define the area."""

        return (self._size * self._size)

    def my_print(self):
        """Prints in stdout the square with the character #."""

        if self._size == 0:
            print("")
            return

        [print("") for i in range(0, self._position[1])]
        for i in range(0, self._size):
            print(" " * self._position[0] + "#" * self._size)
