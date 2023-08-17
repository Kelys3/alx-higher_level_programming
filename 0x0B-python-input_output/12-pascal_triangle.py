#!/usr/bin/python3
"""
This module describes the pascal_triangle function.
"""


def factorial(m):
    """
    Calculates the factorial of a number.
    """
    if m == 0:
        return 1
    else:
        return m * factorial(m - 1)


def pascal_triangle(n):
    """
    Returns a list of integers representing
    the Pascal's triangle of n.
    """
    p_res = []
    if n <= 0:
        return p_res
    for i in range(n):
        row = []
        for j in range(i+1):
            ans = factorial(i) // (factorial(j) * factorial(i-j))
            row.append(ans)
        p_res.append(row)
    return p_res
