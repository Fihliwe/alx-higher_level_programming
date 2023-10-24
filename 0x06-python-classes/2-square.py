#!/usr/bin/python3

"""Defines a class named Square"""

class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes the size of the Sqaure

        Args:
            size(int): this is the size of the square

            """
        
        self.__size = size

        if size != int():
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
