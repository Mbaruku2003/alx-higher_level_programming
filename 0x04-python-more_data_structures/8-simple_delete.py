#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        try:
            del a_dictionary[key]
        except keyError:
            pass
        return a_dictionary
