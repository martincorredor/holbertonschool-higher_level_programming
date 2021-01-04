#!/usr/bin/python3
def safe_print_integer(value):
    """This function prints the value only if is an integer"""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
