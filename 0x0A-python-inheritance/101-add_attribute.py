#!/usr/bin/python3
"""Define a class."""


def add_attribute(obj, attr_name, attr_value):
    """Define an attribute."""

    if hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
