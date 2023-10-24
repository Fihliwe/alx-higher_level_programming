#!/usr/bin/python3

"""Defines the class of a Square"""

class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes the size of the square

        Args:
            size(int): size of square.
        """

        self.__size = size

    @property
    """property for size"""

    def size(self):
        """retrieve the current size"""

        return (self.__size)

    @size.setter
    """setter for the size of square"""

    def size(self, value):
        """ sets the size of the square"""

        self.__size = value

        if value != int():
            raise TypeError("size must be an integer")
        
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates th area of the square"""
        
        return (self.__size * self.size)

    def my_print(self):
        """prints # character to stdout"""

        if size == 0:
            print("")

        else:
            print("#")


