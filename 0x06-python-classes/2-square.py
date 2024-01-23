#!/usr/bin/python3
'''task 2 - instantiation with optional size: def __init__(self, size=0):'''


class Square():
    '''A square class with attribute validation'''

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
