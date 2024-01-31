#!/usr/bin/python3
'''Task 1 - Divide a matrix'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix.
    Args:
        matrix: array of arrays
        div (int/float): divisor
    Raises:
        TypeError: If non-numbers.
        TypeError: If rows of different sizes.
        TypeError: If not an int or float.
        ZeroDivisionError: If 0.
    Returns:
        new matrix, the result of the division.
    '''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
