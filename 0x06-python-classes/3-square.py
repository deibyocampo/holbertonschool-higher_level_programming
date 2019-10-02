#!/usr/bin/python3
class Square:
    """ class of square """
    def __init__(self, size=0):
        """ private instance attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of a square """
        return self.__size * self.__size
