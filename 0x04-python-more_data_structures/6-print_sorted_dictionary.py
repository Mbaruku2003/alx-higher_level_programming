#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    leo = []
    for a, k in a_dictionary.items():
        leo.append(a)
    leo.sort()
    for items in leo:
        print("{}: {}".format(items, a_dictionary[items]))
