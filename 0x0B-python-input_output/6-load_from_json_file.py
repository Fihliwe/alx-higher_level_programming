#!/usr/bin/python3
'''module for function load_from_json_file'''
import json


def load_from_json_file(filename):
    ''' creates a obj fro a json file'''
    with open(filename) as f:
        json.loads(f)
