#!/usr/bin/python3
'''task 4 - Eval is magic'''


class Rectangle:
    '''class rectangle'''

    def __init__(self, width=0, height=0):
        '''init the rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets the width of the Rectangle'''
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
        '''gets height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''the area of the Rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''perimeter of the Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''printable representation of the Rectangle.
        reps the rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for k in range(self.__height):
            [rect.append('#') for n in range(self.__width)]
            if k != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''string representation of the Rectangle'''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
