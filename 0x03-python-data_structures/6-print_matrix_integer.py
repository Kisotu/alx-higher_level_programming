#!/usr/bin/pytho3
def print_matrix_integer(matrix=[[]]):
    for h_vertix in matrix:
        for v_vertix in h_vertix:
            print("{:d}".format(v_vertix), end=" " if v_vertix != h_vertix[-1] else "")
        print()
