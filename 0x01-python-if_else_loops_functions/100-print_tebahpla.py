#!/usr/bin/python3
for alphabet in range(122, 97, -2):
    print("{:c}{:c}".format(alphabet, alphabet-33), end="")
