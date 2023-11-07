#!/usr/bin/python3
'''module for the function of from_json_string'''
import json


def from_json_string(my_str):
    '''returns obj with json string'''
    return (json.loads(my_str))
