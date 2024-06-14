#!/usr/bin/python3
"""Defines a class."""


class Square:
    """defining an instant"""
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self._size * self._size)

    def my_print(self):
        if self._size == 0:
            print("")
            return

        [print("") for i in range(0, self._position[1])]
        for i in range(0, self._size):
            print(" " * self._position[0] + "#" * self._size)
