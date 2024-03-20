#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    if my_list:
        for i in my_list:
            unique_numbers.add(i)
    return sum(unique_numbers)
