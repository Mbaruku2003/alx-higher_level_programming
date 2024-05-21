#!/usr/bin/python3
"""Defines the function."""


def add_integer(a, b=98):
    """Returns a and b as integers.
    Floatsare typecated t integrs before additio
    Rases:
    TypeError if a or b  is not an iteger or float.
    """
    if ((not isinstance(a, float)) and (not isinstance(a, int))):
        raise TypeError("a must be an integer")
    if ((not  isintance(b, float)) and (not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
