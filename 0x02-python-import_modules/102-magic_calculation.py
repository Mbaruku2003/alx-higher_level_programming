#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = a + b
        for i in range(4, 6):
            c = c + i
    else:
        return sub(a, b)
