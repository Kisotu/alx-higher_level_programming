#!/usr/bin/python3
'''Task 8 - Class to JSON'''


def class_to_json(obj):
    '''Return the dictionary description of a simple data structure
    for JOSN serialization of obj'''
    return obj.__dict__
