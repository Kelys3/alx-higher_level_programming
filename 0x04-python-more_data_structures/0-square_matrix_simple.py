#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        new_row = [y ** 2 for y in row]
        square_matrix.append(new_row)
    return square_matrix
