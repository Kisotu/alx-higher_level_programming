#!/usr/bin/python3
'''Task 9 - Full Rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class inheriting BaseGeometry class'''

    def __init__(self, width, height):
        '''Instantiate a new rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Gets areas of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Returns print() and str() rep of Rectangle'''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
