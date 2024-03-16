#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        leo = len(my_list)
        length = leo - 1
        for i in range(length, -1, -1):
            print("{}".format(my_list[i]))
