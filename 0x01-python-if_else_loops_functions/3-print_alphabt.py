#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != chr(101) and chr(i) != chr(113):
        print("{:c}".format(i), end='')
