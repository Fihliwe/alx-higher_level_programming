#!/usr/bin/python3

"""rectangle module"""



class Rectangle:
    """class for rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle


        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.

            """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """define width and return it"""
        return (self.__width)

    @setter.width
    def width(self, value):
        """define width with value and set it"""

        value = self.__width
        if value != int():
            raise TypeError("width must be an integer")
        
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """define height and return it"""
        return(self.__height)

    @setter.height
    def height(self, value):
        """define height with value and set it"""
        value = self.__height
        if value != int():
            raise TypeError("height must be an integer")
        
        elif value < 0:
            raise ValueError("height must be >= 0")

