#!/usr/bin/python3
"""Define a class Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Define its instantation."""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
