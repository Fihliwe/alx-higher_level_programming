#!/usr/bin/python3
'''Module for clas MyList and function print_sorted'''

class MyList(list):
    ''' class for mylist that inherits for list'''

    def print_sorted(self):
        '''function to sort list in ascending order'''
        
        print(sorted(self))

