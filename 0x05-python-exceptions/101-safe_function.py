#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        stderr.write("Exeption: " + str(err) + "\n")
        return None
