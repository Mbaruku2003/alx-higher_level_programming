#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in matrix:
            for elements in rows:
                print("{:d}".format(elements), end=" " if elements != rows[-1] else "")
            print()
