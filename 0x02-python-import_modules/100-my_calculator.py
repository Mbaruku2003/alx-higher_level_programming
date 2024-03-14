#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    leo = len(argv)
    if leo != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="")
        exit (1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == '+':
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == "\\":
        print(f"{a} {operator} {b} = {add(a, b)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit (1)
