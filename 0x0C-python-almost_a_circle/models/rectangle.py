#!/usr/bin/python3
"""Defines a class for rectangle creation"""


class Rectangle(Base):
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

    @property
    def width(self):
        """Getter for retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for setting width"""
        self.__width = value

    @property
    def height(self):
        """Getter for retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for setting height"""
        self.__height = value

    @property
    def x(self):
        """Getter for retrieving the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for setting x"""
        self.__x = value

    @property
    def y(self):
        """Getter for retrieving the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for setting y"""
        self.__y = value
