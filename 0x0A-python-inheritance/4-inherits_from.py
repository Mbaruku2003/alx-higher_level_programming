#!/usr/bin/python3
"""Define a method."""

def inherits_from(obj, a_class):
    """Return True or False"""

    return (isinstance(obj, a_class) and type(obj) != a_class)
