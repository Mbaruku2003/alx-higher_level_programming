#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length_of_my_list = len(my_list)
    if idx > length_of_my_list:
        return my_list
    elif idx < 0:
        return my_list
    del my_list[idx]
    return (my_list)
