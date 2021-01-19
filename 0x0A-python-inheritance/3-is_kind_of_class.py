#!/usr/bin/python3
"""
Module 3
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    
    This function return True f the object is an instance of,
    or if the object is an instance of a class that inherited from, the specified class
    """
    return isinstance(obj) == a_class

