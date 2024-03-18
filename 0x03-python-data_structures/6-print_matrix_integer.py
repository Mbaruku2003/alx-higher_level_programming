#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for each_row in matrix:
        for each_element in each_row:
            if each_element != each_row[-1]:
                print("{:d}".format(each_element), end=" ")
            else:
                print("{:d}".format(each_element), end="")
        print()
