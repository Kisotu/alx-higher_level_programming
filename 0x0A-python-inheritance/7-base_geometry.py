#!/usr/bin/python3
'''Task 7 - Integer validator'''


class BaseGeometry:
    '''Base geometry class'''

    def area(self):
        '''Not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate a parameter as an integer.
        Args:
            name (str): name of integer
            value (int): parameter to validate.
        Raises:
            TypeError: If not integer.
            ValueError: If <= 0.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
