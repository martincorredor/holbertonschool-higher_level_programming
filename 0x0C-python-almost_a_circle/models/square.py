#!/usr/bin/python3
"""Module square.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines an square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id, x, y, width, height)
        self.size = size

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id,
                self.__x, self.__y, self.size)
