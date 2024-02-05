#!/usr/bin/python3
'''Task 2 - Exact same object'''


def is_same_class(obj, a_class):
    '''Check if object is exactly an instance of given class.
    Args:
        obj: object to check.
        a_class (type): class to match the type of obj
    Return:
        True if matching
        Otherwise - False.
    '''
    if type(obj) == a_class:
        return True
    return False
