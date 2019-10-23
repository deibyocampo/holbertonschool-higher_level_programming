#!/usr/bin/python3
""" create Base class"""


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Assign the public instance atribute id """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
