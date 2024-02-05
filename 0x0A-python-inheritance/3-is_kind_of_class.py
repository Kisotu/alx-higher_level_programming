#!/usr/bin/python3
'''Task 3 -  Same class or inherit from'''


def is_kind_of_class(obj, a_class):
    '''Checks if object is instance or inherited instance of a class.
    Args:
        obj (any): object to check.
        a_class (type): The class to match obj.
    Returns:
        True - if obj matches
        Otherwise - False.
    '''
    if isinstance(obj, a_class):
        return True
    return False
