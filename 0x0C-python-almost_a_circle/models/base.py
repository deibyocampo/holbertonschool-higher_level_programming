#!/usr/bin/python3
""" create Base class"""


import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return __import__('json').dumps(list_dictionaries)

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
    def save_to_file_csv(cls, list_objs):
        """ writes the CVS string representation """
        file_name = ("{}.csv".format(cls.__name__))
        json_list = []
        if list_objs:
            for ls in list_objs:
                json_list.append(cls.to_dictionary(ls))
        with open(file_name, mode="w") as f:
            f.write(cls.to_json_string(json_list))

    @classmethod
    def load_from_file_csv(cls):
        """ files to instance CVS """
        file_name = cls.__name__ + ".cvs"
        my_list = []

        if my_list is None:
            return ([])
        try:
            with open(file_name, mode="r") as f:
                read_file = f.readline()
                from_json = cls.from_json_string(read_file)
            for element in from_json:
                my_list.append(cls.create(**element))
            return my_list
        except FileNotFoundError:
            return (my_list)
