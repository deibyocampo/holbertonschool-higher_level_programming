#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        square_args = ["id", "size", "x", "y"]
        if args:
            for idx, value in enumerate(args):
                setattr(self, square_args[idx], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
