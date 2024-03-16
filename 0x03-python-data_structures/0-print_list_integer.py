#!/usr/bin/python3
def print_list_integer(my_list=[]):
    leo = len(my_list) + 1
    for i in range(1, leo):
        print("{}".format(i), end="\n")
