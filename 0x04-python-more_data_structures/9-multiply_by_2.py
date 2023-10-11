#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    2_dict = a_dictionary.copy()
    list_keys = list(2_dict.keys())

    for i in list_keys:
        2_dict[i] *= 2

    return (2_dict)
