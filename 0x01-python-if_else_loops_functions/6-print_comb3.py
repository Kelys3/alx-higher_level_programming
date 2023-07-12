#!/usr/bin/python3
for i in range(0, 9):
    for c in range(i + 1, 10):
        if i != 8:
            print("{}{}".format(i, c), end=", ")
        else:
            print("{}{}".format(i, c))
