#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leo = len(argv) - 1
    if leo <= 0:
        print("{:d} arguements".format(leo))
    elif leo == 1:
        print("{:d} argument:".format(leo))
        print("{:d}: {:s}".format(leo, argv[leo]))
    else:
        print("{:d} arguments:".format(leo))
        leo = leo + 1
        for leo in range(1,7):
            print("{:d}: {:s}".format(leo, argv[leo]))
