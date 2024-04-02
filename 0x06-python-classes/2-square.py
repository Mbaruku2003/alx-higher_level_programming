#!/usr/bin/python3
"""We define a method Square."""


class Square:
    """We have created a square."""
    def __init__(self, size=0):
        """initializes the size of an object.
        Args:
        Size(int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
