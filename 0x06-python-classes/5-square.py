#!/usr/bin/python3
"""Defines a class named Square"""

class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes the size of the square

        Args:
            size(int): size of square.
            """

        self.__size = size       

    @property
    def size(self):
        """get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """conditoins for size of sqaure"""
        self.__size = value

        if value != int():
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints # to the stdout"""

        if size == 0:
            print("")

        else:
            print("#")
