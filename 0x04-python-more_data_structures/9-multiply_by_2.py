#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''func that returns a dict with all values mult by 2'''
    new_dict = []
    for j in a_dictionary:
        new_dict[j] = a_dictionary[j] * 2
    return (new_dict)
