#!/usr/bin/python3
"""Define a class named Sqaure"""

class Square:
    """Represents a Square

    Args:
        size(int): size of square.
        """

    def __init__(self, size=0):
        """Initializes the size of Sqaure"""

        self.__size = size

        if size != int():
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

    

    """Returns the curent square area"""
    
    def area(self):
        """calculate the area of the square"""
        return (self.__size * self.__size)
