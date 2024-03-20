#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    leo = []
    for row in matrix:
        leo.append(list(map(lambda x: x * x, row)))
    return leo
