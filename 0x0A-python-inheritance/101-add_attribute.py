#!/usr/bin/python3
"""Define a class."""


def add_attribute(obj, attr_name, attr_value):
    """Define an attribute."""

    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute{}".format(attr_name))

    setattr(obj, attr_name, attr_value)
