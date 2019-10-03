#!/usr/bin/python3
class Square:
    """ Initialize square class instance with size """
    def __init__(self, size=0, position=(0, 0)):
        """ instance whith size and check for exceptions """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2 and type(position[0]) == int and position[0] >= 0 and type(position[1]) == int and position[1] >= 0:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ setter position """
        if type(value, value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2 and type(position[0]) == int and position[0] >= 0 and type(position[1]) == int and position[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints a square made up of # """
        if self.__size != 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print("_", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """ prints a square made up of # """
        a = ""
        if self.__size != 0:
            a = '\n' * self.__position[1]
            for i in range(self.__size):
                a = a + "_" * self.__position[0]
                a = a + "#" * self.__size
                if i < self.__size - 1:
                    a = a + '\n'
            return (a)
        else:
            return ("")

    def __repr__(self):
        """ print square made up of # """
        return self.__str__()
