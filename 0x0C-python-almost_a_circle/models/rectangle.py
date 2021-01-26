#!/usr/bin/python3
"""Module rectangle.py"""
from models.base import Base

class Rectangle(Base):
    """Class that defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def display(self):
        """Prints the rectangle instance with # character"""
        for i in range(self.__y):
            print()
        for j in range(self.height):
            for k in range(self.__x):
                print(" ", end="")
            for m in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """Assigns an argument to each attribute"""
        if args:
            i = len(args)
            if 0 in range(i):
                self.id = args[0]
            if 1 in range(i):
                self.__width = args[1]
            if 2 in range(i):
                self.__height = args[2]
            if 3 in range(i):
                self.__x = args[3]
            if 4 in range(i):
                self.__y = args[4]
        else:
            if "id" in kargs:
                self.id = kargs["id"]
            if "width" in kargs:
                self.__width = kargs["width"]
            if "height" in kargs:
                self.__height = kargs["height"]
            if "x" in kargs:
                self.__x = kargs["x"]
            if "y" in kargs:
                self.__y = ["y"]

    
