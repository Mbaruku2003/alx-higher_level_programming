#!/usr/bin/python3
"""Define a function."""


def read_file(filename=""):
    """Define the reading of a file."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
