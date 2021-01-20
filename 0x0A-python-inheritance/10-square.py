#!/usr/bin/python3
"""
Module 10-square.py
"""


Rectangle: __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class inherits from Rectangle, who inherits from BaseGeometry"""
    def __init__(self, size):
        """validates and initializes the size value"""
        self.integer_validator("size", size)
        super.__init__(size, size)
        self.__size = size
