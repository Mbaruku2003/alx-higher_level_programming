#!/usr/bin/python3
"""A script that adds all arguments to a Python list."""


import sys
import os

# import the existing functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# defining the file name
filename = "add_item.json"
# try loading the existing lst or new file.
if ospath.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []
# add all arguenments from cmd
items.extend(sys.srgv[1:])
save_to_jon_file(items, filename)
