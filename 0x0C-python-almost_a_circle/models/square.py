#!/usr/bin/python3
'''"Defines a Square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Init square'''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''square size getter'''

        return self.width

    @size.setter
    def size(self, value):
        '''Square size setter'''

        self.width = value
        self.height = value

    def __str__(self):
        '''module string rep of square'''

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''Update square'''

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''return dictonary'''

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
