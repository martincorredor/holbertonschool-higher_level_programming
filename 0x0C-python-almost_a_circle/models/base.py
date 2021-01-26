#!/usr/bin/python3
"""
Module base.py
"""


import json


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation
        of a list of instances(objects) to a file.
        """
        json_file = cls.__name__ + ".json"
        empty_list = []

        if list_objs is not None:
            for run in list_objs:
                empty_list.append(run.to_dictionary())

        with open(json_file, "w") as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation"""
        if json_string is None or json_string == 0:
            json_string = "[]"
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
        This method creates a "dummy" instance and updates the
        value of the attributes with those of the given dictionary
        and returns a new object with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj_dummy = Rectangle(26, 19)

        elif cls is Square:
            obj_dummy = Square(31)

        else:
            obj_dummy = None

        obj_dummy.update(**dictionary)
        return obj_dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        json_file = cls.__name__ + ".json"
        empty_list = []

        if path.isfile(json_file):
            with open(json_file, "r") as f:
                dictionary = cls.from_json_string(f.read())
            for element in dictionary:
                empty_list.append(cls.create(**element))
        return empty_list
