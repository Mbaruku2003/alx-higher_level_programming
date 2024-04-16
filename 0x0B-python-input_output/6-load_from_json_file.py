#!/usr/bin/python3
"""Define the function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file"."""

    with open(filename, "r", encoding="utf-8") as f:
        json.loads(f)
