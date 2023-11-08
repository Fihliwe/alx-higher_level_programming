#!/usr/bin/python3
'''module for student'''


class Student:
    '''defines a stdudent'''

    def __init__(self, first_name, last_name, age):
        '''initializing public instances'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' that retrieves a dictionary representation of a Student instance'''
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, i) for i in attrs if hasattr(self, i)}
        return (self.__dict__)

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for i, j in json.items():
            setattr(self, i, j)
