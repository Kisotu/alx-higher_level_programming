#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for dict_key in list(a_dictionary):
        if a_dictionary[dict_key] == value:
            del a_dictionary[dict_key]
    return a_dictionary
