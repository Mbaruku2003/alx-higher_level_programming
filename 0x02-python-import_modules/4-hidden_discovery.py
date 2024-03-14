#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    moddef = dir()
    for length_moddef in range(0, len(moddef)):
        if moddef[length_moddef][:2] != "__":
            print("{:s}".format(moddef))
