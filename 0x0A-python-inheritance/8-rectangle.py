#!/usr/bin/python3
"""
Module 8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that initializes with and height of rectangle"""
    def __init__(self, width, height):
        """validate and initialize width and height"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
