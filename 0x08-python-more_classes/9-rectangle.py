#!/usr/bin/python3
'''Task 9 - A Square is a rectangle'''


class Rectangle:
    '''class: Rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        '''creates a square, a type of rectangle'''
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compares 2 rectangles'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return True
        else:
            return False

    def __init__(self, width=0, height=0):
        '''init instance of class Rectangle'''
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width getter'''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''width setter'''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''height getter'''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''height setter'''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''area of rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''perimeter of perimeter'''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''string representation of rectangle'''
        rect_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            rect_str += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        '''used by eval() to recreate new object'''
        rect_str = "Rectangle(" + str(self.__width) + ","
        rect_str += str(self.__height) + ")"
        return rect_str

    def __del__(self):
        '''dels instance of Rectangle class, and prints "bye" message'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
