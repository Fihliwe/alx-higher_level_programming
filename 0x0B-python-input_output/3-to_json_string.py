#!/usr/bin/python3
'''module for function to_json_string'''
import json


def to_json_string(my_obj):
    '''returns the json rep of obj'''
    return (json.dumps(my_obj))
