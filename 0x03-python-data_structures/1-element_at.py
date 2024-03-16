#!/usr/bin/python3
def element_at(my_list, idx):
    leo = len(my_list)
    trueindex = leo - 1
    if idx < 0:
        return (None)
    if idx > trueindex:
        return (None)
    else:
        return my_list[idx]
