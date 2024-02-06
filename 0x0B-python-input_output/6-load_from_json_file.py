#!/usr/bin/python3
'''Task 6 - Create object from JSON file'''
import json


def load_from_json_file(filename):
    '''Create Object from a JSON file'''
    with open(filename) as k:
        return json.load(k)
