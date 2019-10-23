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

    @staticmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(
                    [e.to_dictionary() for e in list_objs]))
