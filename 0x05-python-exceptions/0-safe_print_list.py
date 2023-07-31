#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements += 1
        except (IndexError, TypeError):
            break
    print("")
    return (elements)
