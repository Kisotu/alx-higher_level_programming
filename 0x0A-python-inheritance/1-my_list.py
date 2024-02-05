#!/usr/bin/python3
'''Task 1 - class that inherits from list'''


class MyList(list):
    '''inherits built in list class'''

    def print_sorted(self):
        '''prints sorted list in asc order'''
        print(sorted(self))
