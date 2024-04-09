#!/usr/bin/python3
"""Define a class."""


class LockedClass:
    """Prevent user from creating new attributes
    that are not "firstname"
    """
    __slots__ = ["firstname"]
