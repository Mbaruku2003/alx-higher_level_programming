#!/usr/bin/python3
"""Defining the class."""


class Square:
    """Defining a method init"""
    def __init__(self, size):
        self.__size = size
    """Defining a property."""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Defining a new term area."""
    def area(self):
        return (self.size * self.size)
