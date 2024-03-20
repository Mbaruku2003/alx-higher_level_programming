#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    if a_dictionary:
        for key, v in a_dictionary.items():
            new_dictionary.update({key: v * 2})
    return new_dictionary
