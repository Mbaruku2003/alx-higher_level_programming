#!/usr/bin/python3
"""Define the function."""
import json


def from_json_string(my_str):
    """Decodes object to original type."""

    return json.loads(my_str)
