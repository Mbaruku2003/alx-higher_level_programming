#!/usr/bin/python3
"""Define a class Myint."""


class MyInt(int):
    """Define ne."""
    def __ne__(self, other):
        return super().__ne__(other)
    def __eq__(self, other):
        return super().__eq__(other)
