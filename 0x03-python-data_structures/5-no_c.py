#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        anewstring = my_string.translate({ord('C') : None})
        anothernewstring = anewstring.translate({ord('c') : None})
        return (anothernewstring)
    return (my_string)
