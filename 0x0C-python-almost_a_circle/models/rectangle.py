#!/usr/bin/python3
"""Defines a class for rectangle creation"""


class Recatangle(Base):
    """
    Rectangle class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor initializing the Rectangle objects
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        def width(self):
            """Getter for retrieving width"""
            return self.__width

        def width(self, value):
            """Setter for setting width"""
            self.__width = value

        def heigth(self):
            """Getter for retrieving height"""
            return self.__height

        def height(self, value):
            """Setter for setting height"""
            self.__height = value

        def width(self):
            """Getter for retrieving the x coordinate"""
            return self.__x

        def width(self, value):
            """Setter for setting x"""
            self.__x = value

        def width(self):
            """Getter for retrieving the y coordinate"""
            return self.__y

        def width(self, value):
            """Setter for setting y"""
            self.__y = value
