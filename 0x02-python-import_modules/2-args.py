#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leo = len(argv) - 1
    if leo < 1:
        print("{} arguements.".format(leo))
    elif leo == 1:
        print("{} argument:".format(leo))
    else:
        print("{} arguments:".format(leo))

    for numbering in range(leo):
        print("{}: {:s}".format(numbering + 1, argv[numbering + 1]))
