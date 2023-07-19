#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for member in list_keys:
        if value == a_dictionary.get(member):
            del a_dictionary[member]
    return a_dictionary
