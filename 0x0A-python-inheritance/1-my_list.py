#!/usr/bin/python3
"""
Module 1
Contain 
MyList class that inherits from list class
"""


class MyList(list):
    """class inherit from list"""
    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
