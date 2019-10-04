#!/usr/bin/python3
"""An addition module
add_integer adds two integers together

"""


def add_integer(a, b=98):
    """ Return a + b
    Args: a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
