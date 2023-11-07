#!/usr/bin/python3
'''Module for function write_file'''


def write_file(filename="", text=""):
    ''' writes a string to a text file'''
    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
