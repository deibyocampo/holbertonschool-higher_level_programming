#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        return ("[square]" + super().__str__()[11:])
