#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    truelength = length - 1
    for i in range(truelength, -1, -1):
        print("{:}".format(my_list[i]), end="\n")
