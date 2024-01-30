#!/usr/bin/python3
'''task 3 - rectangle class'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''init rectnagle object
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''sets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''area of the Rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''perimeter of the Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''Return the printable instance of the rectangle.
        reps the rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
