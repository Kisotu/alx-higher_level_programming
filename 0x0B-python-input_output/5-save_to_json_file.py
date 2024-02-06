#!/usr/bin/python3
'''Task 5 - Save object to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''Write object to text file using JSON representation'''
    with open(filename, "w") as k:
        json.dump(my_obj, k)
