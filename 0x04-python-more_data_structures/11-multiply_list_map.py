#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''function that returns a list with values multiplied by a number'''
    return (list(map((lambda i: i * number), my_list)))
