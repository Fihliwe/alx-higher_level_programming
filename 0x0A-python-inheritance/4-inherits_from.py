#!/usr/bin/python3
''' module for inherits_from function'''

def inherits_from(obj, a_class):
    '''return true if obj is insatnce or otherwise'''

    return False if type(obj) is a_class else isinstance(obj, a_class)
