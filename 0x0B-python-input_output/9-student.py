#!/usr/bin/python3
'''module for student class'''


class Student:
    '''defines a Student'''

    def __init__(self, first_name, last_name, age):
        '''initializing the public instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            ''' that retrieves a dictionary representation of a Student instance'''
            return (self.__dict__)
