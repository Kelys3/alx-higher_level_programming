#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_newdict = a_dictionary.copy()
    list_dictkeys = list(my_newdict.keys())
    for value in list_dictkeys:
        my_newdict[value] *= 2
    return my_newdict
