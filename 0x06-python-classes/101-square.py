#!/usr/bin/python3
class Square:
    """ Initialize square class instance with size """
    def __init__(self, size=0, position=(0, 0)):
        """ instance whith size and check for exceptions """
        self.size = size
        self.position = position

    def area(self):
        """ area of a square instance """
        return self.__size * self.__size

    @property
    def size(self):
        """ getter size """
        return self.__size

    @property
    def position(self):
        """ getter position """
        return self.__position

    @size.setter
    def size(self, value):
        """ setter size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ setter position """
        if (len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must br a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints a square made up of # """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        """ prints a square made up of # """
        tmpstr = ""
        tmplist = []
        if self.__size == 0:
            tmpstr = ""
        else:
            for i in range(self.__size):
                tmplist.append("{}{}".format("_" * self.__position[0], "#" * self.__size))

            tmpstr = "\n" * self.__position[1] + "\n".join(tmplist)
        return tmpstr
