#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[i ** 2 for i in row] for row in matrix]
    return square_matrix
