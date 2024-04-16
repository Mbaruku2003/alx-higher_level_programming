#!/usr/bin/python3
"""Define the function."""


def write_file(filename="", text=""):
    """Openn the file."""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
