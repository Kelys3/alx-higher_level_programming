#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_elm = 0
    for x in set(my_list):
        add_elm += x
    return add_elm
