#!/usr/bin/python3
'''Task 100 - My integer'''


class MyInt(int):
    '''MyInt is a rebel. MyInt has == and != operators inverted'''

    def __eq__(self, value):
        '''Override == operator with != behavior'''
        return self.real != value

    def __ne__(self, value):
        '''Override != operator with == behavior'''
        return self.real == value
