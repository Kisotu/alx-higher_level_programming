#!/usr/bin/python3
'''Task 10 - Square #1'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A square class'''

    def __init__(self, size):
        '''Init a new square.
        Args:
            size (int): The size of the new square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
