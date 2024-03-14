#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    string = 0
    length = len(argv)
    for count in range(1, length):
        string += int(argv[count])
    print("{}".format(string))
