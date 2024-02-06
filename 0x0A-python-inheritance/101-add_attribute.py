#!/usr/bin/python3
'''Task 13 - Can I?'''


def add_attribute(obj, att, value):
    '''Add a new attribute to an object if possible.
    Args:
        obj (any): Object to add an attribute.
        att (str): Name of attribute to add to obj.
        value (any): Value of attribute
    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
