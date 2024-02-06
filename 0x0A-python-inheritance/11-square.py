#!/usr/bin/python3
'''Task 11-  Square #2'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A square class that inherits class Rectangle'''

    def __init__(self, size):
        '''Initialize a new square.
        Args:
            size (int): The size of the new square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
