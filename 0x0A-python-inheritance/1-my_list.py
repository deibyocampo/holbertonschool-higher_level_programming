#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ class that inheritnace from list """
    def print_sorted(self):
        """ print list in sorted """
        print(sorted(self))
