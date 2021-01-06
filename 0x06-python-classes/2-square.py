#!/usr/bin/python3
"""
Module 2-square
Define class Square
"""


class Square:
    """
    Define a square
    Args:
        size : Side of a square
    """
    def __init__(self, size = 0):
        """Class to defines a square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        
