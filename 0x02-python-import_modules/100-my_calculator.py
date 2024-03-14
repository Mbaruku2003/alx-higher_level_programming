#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    leo = len(argv)
    if leo != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="")
        print()
        exit(1)
    operator = argv[2]
    a = argv[1]
    b = argv[3]
    if opearator != add or sub or mul or div:
        print("Unknown operator. Available operators: +, -, * and /", end="")
        print()
        exit(1)
    leo = int(a)
    mbaruk = int(b)
    if operator is add:
        result = a + b
        print("{} + {} = {}".format(leo, mbaruk, result), end="")
        print()
        exit(1)
    elif operator is sub:
        result = a - b
        print("{} + {} = {}".format(leo, mbaruk, result), end="")
        print()
        exit(1)
    elif operator is mul:
        result = a * b
        print("{} * {} = {}".format(leo, mbaruk, result), end="")
        print()
        exit (1)
    else:
        result = a / b
        print("{} / {} = {}".format(leo, mbaruk, result), end="")
        print()
        exit (1)

