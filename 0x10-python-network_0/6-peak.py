#!/usr/bin/python3
"""Module that contain find_peak function"""


def find_peak(list_of_integers):
    """Sort a list, find and return the maxime value in the list"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None