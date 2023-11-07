#!/usr/bin/python3
''' module for function save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    '''writes obj to a text file using json rep'''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
