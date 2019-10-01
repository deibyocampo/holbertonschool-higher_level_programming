#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
        print("Inside result: {}".format(x))
        return x
    except ZeroDivisionError:
        print("Inside result:", None)
