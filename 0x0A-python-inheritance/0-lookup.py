#!/usr/bin/python3
"""
Module 0
Contain the loohup function that return the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Return a list object"""
    return dir(obj)
