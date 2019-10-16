#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """

    def __init__(self, width, height):
        """ constructor """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
