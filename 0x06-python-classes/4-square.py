#!/usr/bin/python3
"""Defining the class."""


class Square:
    """Defining a method init"""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """gets a size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defining a new term area"""
        return (self.__size * self.__size)
