#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.integer_validator("y", y)
        self.__y = y

    def area(self):
        return (self.width * self.height)

    def display(self):
        for fil in range(self.y):
            print()
        for fill in range(self.height):
            for col in range(self.x):
                print(" ", end="")
            for coll in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args, **kwargs):
        up_date = ["id", "width", "height", "x", "y"]
        if args:
            for idx, value in enumerate(args):
                setattr(self, up_date[idx], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
