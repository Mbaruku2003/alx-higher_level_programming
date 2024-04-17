#!/usr/bin/python3
"""Define a class student."""


class Student:
    """Define instantation."""

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.fisrt_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):

        if  (type(attrs) == list and 
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
