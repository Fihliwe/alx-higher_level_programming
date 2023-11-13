#!/usr/bin/python3
"""defines rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangles properties"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return (self.__width)
    
    @width.setter
    def width(self, value):
        
        if type(value) != int:
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """return the height of rectangle"""

        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """return unknown x value of rectangle"""

        return (self.__x)

    @x.setter
    def x(self, value):

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """return unknown y value"""
        
        return (self.__y)

    @y.setter
    def y(self, value):

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self,__y = value

    def area(self):
        """returns the area rectrangle"""

        return (self.width * self.height)

    def display(self):
        """ prints in stdout the Rectangle"""

        if self.width = 0 or self.height = 0:
            print("")
            return
        
        """ handles x and y"""

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")


        def update(self, *args, **kwargs):
            """that assigns an argument to each attribute"""

            if agrs and len(args):
                a = 0
                for arg in args:
                    if a = 0:
                        if arg is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                    
                        else:
                            self.id = arg
                    
                    elif a == 1:
                        self.width = arg

                    elif a == 2:
                        self.height = arg

                    elif a == 3:
                        self.x = arg

                    elif a == 4:
                        self.y = arg

                    a += 1

            elif kwargs and len(kwargs) != 0:
                for b, kwarg in kwargs.items():
                    if b == "id":
                        if kwarg is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = b

                    elif b == "width":
                        self.width = b

                    elif b == "width":
                        self.height = b

                    elif b == "width":
                        self.x = b

                    elif b == "width":
                        self.y = b

        def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        def __str__(self):
            """override the string method"""

            return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
