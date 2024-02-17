#!/usr/bin/python3
"""Defines a base class for object creation with id assignment"""
class Base:
    """
    Base class for object creation.

    Attributes:
        __nb_onjects (int): Private class variable to keep trach of the number of objects created
        id (int): Instance variable representing the identifier of an object.
    Methods:
        __init__(self, id=None): Constructor method for initializing the class objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method

        Args:
            id (int, optional): Identifier for the object, if not provided a unique id will be assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
