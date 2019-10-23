#!/usr/bin/python3
""" Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square the class intherance Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ method to return string """
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update class to include args and kwargs """
        square_args = ["id", "size", "x", "y"]
        if args:
            for idx, value in enumerate(args):
                setattr(self, square_args[idx], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary representation of rectangle """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
