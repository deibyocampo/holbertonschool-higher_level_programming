#!/usr/bin/python3

def add_integer(a, b=98):
    """ a and b must integers or floats,
        otherwise raise error diferent date
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
