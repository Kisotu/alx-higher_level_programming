#!/usr/bin/python3
'''Task 2'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''method - init class object'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''gets width'''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''sets width'''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''gets height'''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''sets height'''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    '''Calculate area of Rect'''
    def area(self):
        return self.__height * self.__width

    '''Calculate perimeter'''
    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2
