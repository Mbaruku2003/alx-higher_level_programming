#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    leo = len(argv)
    if leo != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="")
        exit (1)
    operator = argv[2]
    a = argv[1]
    b = argv[3]
    leo = int(a)
    mbaruk = int(b)
    if operator == '+':
        print(f"{leo} {operator} {mbaruk} = {add(a, b)}")
        exit(1)
    elif operator == '-':
        print(f"{leo} {operator} {mbaruk} = {add(a, b)}")
        exit(1)
    elif operator == '*':
        print(f"{leo} {operator} {mbaruk} = {add(a, b)}")
        exit (1)
    elif operator == "\\":
        print(f"{leo} {operator} {mbaruk} = {add(a, b)}")
        exit (1)
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit (1)
