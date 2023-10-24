#!/usr/bin/python3
"""Defines a class named Square"""

class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of the square

        Args:
            size(int): size of square.
            position(int): position of square
            """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set the position of the square"""

        self.__position = value
        if value != int(tuple([1])) and value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        """calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints # to the stdout"""

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__self)]
            print("")

            if self.__size == 0:
                print("")
