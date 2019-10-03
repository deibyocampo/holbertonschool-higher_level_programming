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

    def __init__(self, size=0, position=(0, 0)):
        """ sets the size of the square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    @property
    def position(self):
        """ Returns position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints a square of a certain size at a position """
        if self.size == 0:
            print()
            return
        for space in range(self.position[1]):
            print()

        for row in range(self.size):
            for space in range(self.position[0]):
                print(" ", end="")
            for col in range(self.size):
                print("#", end="")
            print()
