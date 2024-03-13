#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        leo = chr(i - 32)
        print("{}".format(leo), end="")
    else:
        leo = chr(i)
        print("{}".format(leo), end="")
