#!/usr/bin/python3
"""Define a class."""


class Student:
    """Class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retreives a dictionary rpresentation."""
        return self.__dict__
