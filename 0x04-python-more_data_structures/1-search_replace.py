#!/usr/bin/python3
def search_replace(my_list, search, replace):
    leo = my_list[:]
    for index, element in enumerate(my_list):
        if element == search:
            leo[index] = replace
    return leo
