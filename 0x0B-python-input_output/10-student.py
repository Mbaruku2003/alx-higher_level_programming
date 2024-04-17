#!/usr/bin/python3
"""Define a class student."""


class Student:
    """Define a cllass student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate a string."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Turns a string to json."""

        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):

            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
