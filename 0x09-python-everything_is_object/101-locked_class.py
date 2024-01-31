#!/usr/bin/python3
'''A locked class'''


class LockedClass:
    '''
    Prevent the user from dynamically creating new
    instance attributes except if  called 'first_name'.
    '''

    __slots__ = ["first_name"]
