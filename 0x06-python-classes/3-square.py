#!/usr/bin/python3
"""Defining a class."""


class Square:
    """Defining a method init."""
    def __init__(self, size=0):
        """Defining a new object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area."""
        return (self.__size * self.__size)
