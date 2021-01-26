#!/usr/bin/python3
"""Module square.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines an square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kargs):
        """Assigns atributes"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kargs:
               self.id = kargs["id"]
            if "size" in kargs:
                self.size = kargs["size"]
            if "x" in kargs:
                self.x = kargs["x"]
            if "y" in kargs:
                self.y = kargs["y"]

    def to_dictionary(self):
        """
        Return a dict representation of this class
        """
        dic = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return dic
