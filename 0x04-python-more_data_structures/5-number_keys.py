#!/usr/bin/python3
def number_keys(a_dictionary):
    numb = 0
    dict_keys = list(a.dictionary.keys())

    for k in dict_keys:
        numb += k

    return numb
