#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]

    ops = {
            "+": add(a, b),
            "-": sub(a, b),
            "*": mul(a, b),
            "/": div(a, b)}

    if sign in ops.keys():
        print("{:d} {} {:d} = {:d}".format(a, sign, b, ops[sign]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
