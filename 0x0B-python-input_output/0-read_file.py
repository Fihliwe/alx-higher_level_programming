#!/usr/bin/python3

'''Module for read_file function'''

def read_file(filename=""):
    '''reads file and print to stdout'''

    with open(filename, encoding="UTF-8" as f:
            print(f.read(), end="")
