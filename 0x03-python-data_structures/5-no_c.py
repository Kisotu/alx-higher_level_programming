#!/usr/bin/python3
def no_c(my_string):
    c_less_string = my_string.translate({ord(k): None for k in 'cC'})
    return c_less_string
