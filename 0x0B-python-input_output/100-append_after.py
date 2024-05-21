#!/usr/bin/python3
"""Inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Read and write froma file to a new file."""

    try:
        with open(filename, "r") as new_file:
            lines = new_file.readlines()

        with open(filename, "w") as new_file:
            for line in lines:
                new_file.write(line)
                if search_string in line:
                    new_file(new_string + "\n")
