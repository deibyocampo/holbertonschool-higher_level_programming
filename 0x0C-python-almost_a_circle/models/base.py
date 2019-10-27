#!/usr/bin/python3
""" create Base class"""


import json


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
    def to_json_string(list_dictionaries):
        """ string of dictionary to JSON """
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        file_name = ("{}.json".format(cls.__name__))
        json_list = []
        if list_objs:
            for ls in list_objs:
                json_list.append(cls.to_dictionary(ls))
        with open(file_name, mode="w") as f:
            f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """ string JSON to dictionary """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to instance """
        if cls.__name__ == "Rectangle":
            create = cls(1, 1)
        elif cls.__name__ == "Square":
            create = cls(1)
        create.update(**dictionary)
        return (create)

    @classmethod
    def load_from_file(cls):
        """ files to instance """
        try:
            with open(cls.__name__ + 'json', encoding='utf-8') as f:
                ls = cls.from_json_string(f.readline())
        except FileNotFoundError:
            ls = []
        finally:
            return [cls.create(**e) for e in ls]
