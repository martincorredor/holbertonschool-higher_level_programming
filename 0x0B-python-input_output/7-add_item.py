#!/usr/bin/python3
"""Module "7-add_item.py"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)

def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
