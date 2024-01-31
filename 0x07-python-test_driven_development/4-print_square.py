#!/usr/bin/python3
'''Task 3 - Print a square'''


def print_square(size):
    '''Print a square with the # character.

    Args:
        size (int): dimensions of the square.
    Raises:
        TypeError: If not integer.
        ValueError: If < 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
