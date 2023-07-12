#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) < 123:
            alphabet = ord(a) - 32
        else:
            alphabet = ord(a)
        print("{:c}".format(alphabet), end='')
    print()
