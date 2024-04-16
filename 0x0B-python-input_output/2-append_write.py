#!/usr/bin/python3
"""Define the function."""


def append_write(filename="", text=""):
    """Open the file and append."""

    with open(filename, "a" or "w", encoding="utf-8") as f:
        return f.write(text)
