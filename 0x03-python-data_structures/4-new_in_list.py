#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    leo = len(my_list) - 1
    new_list = my_list.copy()
    if my_list:
        if idx < 0:
            return (new_list)
        elif idx > leo:
            return (new_list)
        new_list[idx] = element
        return (new_list)
