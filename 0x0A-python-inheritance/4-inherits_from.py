#!/usr/bin/python3
"""Define a method."""


def inherits_from(obj, a_class):
    """returns True or False if object is aninstance."""

    return isinstance(obj, a_class) and type(obj) != a_class
