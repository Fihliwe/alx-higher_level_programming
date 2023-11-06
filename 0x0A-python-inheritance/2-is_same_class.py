#!/usr/bin/python3
''' module for function is_same_class'''

def is_same_class(obj, a_class):
    '''returns true if instance and false for otherwise'''

    if type(obj) == a_class:
        return True
    else:
        return False
