#!/usr/bin/python3
"""Defines a base class for object creation with id assignment"""


class Base:
    """
    Base class for object creation.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor assigning an id for the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
