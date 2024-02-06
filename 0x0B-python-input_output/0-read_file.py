#!/usr/bin/python3
'''Task 0 - Read file'''


def read_file(filename=""):
    '''functio that reads & prints the contents of a UTF8 text file to stdout
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
