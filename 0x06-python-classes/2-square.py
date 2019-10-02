#!/usr/bin/python3
class Square:
    """ size validation """
    def __init__(self, size=0):
        """ private instance attribute
        Argument
        Exception
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
