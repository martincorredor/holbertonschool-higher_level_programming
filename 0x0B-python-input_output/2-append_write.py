#!/usr/bin/python3
"""
Module 2-append_write.py
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file and
    Returns the number of characters added
    """
    with open(filename, mode="a") as f:
    return (f.write(text))
