#!/usr/bin/python3
'''task 8 - Compare Rectangles'''


class Rectangle:
    '''Rectangle class
    Attributes:
        number_of_instances (int): no of Rectangle instances.
        print_symbol (any) : symbol used for string representation.
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Inits a new Rectangle'''

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets width of the Rectangle'''
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
        '''Gets height of the Rectangle'''
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): first Rectangle.
            rect_2 (Rectangle): second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        '''printable representation of the Rectangle.
        Reps the rectangle with the # character'''

        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for i in range(self.__height):
            [recta.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        '''string representation of the Rectangle'''

        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        '''Print a message for every deletion of a Rectangle'''

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
