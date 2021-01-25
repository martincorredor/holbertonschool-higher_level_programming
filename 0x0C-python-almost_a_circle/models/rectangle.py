#!/usr/bin/python3
"""Module rectangle.py"""


class rectangle(Base):
    """Class that defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super()._init__(id)
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
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
