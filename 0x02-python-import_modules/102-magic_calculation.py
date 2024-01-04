#!/usr/bin/python3

import operator

def magic_calculation(a, b):
    if a < b:
        c = operator.add(a, b)
        for i in range(4, 6):
            c = operator.add(c, i)
        return (c)
    
    else:
        return (sub(a, b))
