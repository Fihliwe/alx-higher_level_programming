#!/usr/bin/python3
'''Module for function append_write'''


def append_write(filename="", text=""):
    '''appends a string to the end of a file'''
    with open(filename, "a", encoding="UTF-8") as f:
        return (f.write(text))
