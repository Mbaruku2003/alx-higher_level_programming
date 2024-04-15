#!/usr/bin/python3
"""Define a class."""


class BaseGeometry:
    """Define an area."""

    def area(self):
        """Define area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define another method."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
