#!/usr/bin/python3
'''task 4'''


class Square():
    '''Square class - Access and update private attribute '''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(size, value):
        if (type(value) is not int):
            raise TypeError("size mnust be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
