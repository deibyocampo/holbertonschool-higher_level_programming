#!/usr/bin/python3
class Square:
    """ Printing a square """
    def __init__(self, size=0):
        """ private instance attribute """
        self.__size = size

    def area(self):
        """ Area of a square """
        return self.__size * self.__size

    @property
    def size(self):
        """ sets the size of hte square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ instance method square character """
        if self.__size == 0:
            print()

        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
