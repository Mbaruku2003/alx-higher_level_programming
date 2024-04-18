#!/usr/bin/python3
"""A script that adds all arguments to a Python list."""


import sys
import json


def main():
    """ getting arguenments and putting elsewhere."""

    arguenments_on_command_line = sys.argv[1:]
    a_list = []
    a_list.extend(arguenments_on_command_line)
    filename = "add_item.json"

    save_to_json_file(a_list, filename)
    loaded_list = load_from_json_file(filename)
    print(loaded_list)

    if __name__ == "__main__":
        main()
