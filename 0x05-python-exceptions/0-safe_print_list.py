#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_items = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_of_items += 1
        except IndexError:
            pass
    print()
    return(x)
