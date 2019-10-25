#!/usr/bin/python3
class MyInt(int):
    def __init__(self, my_i):
        self.my_i = my_i

    def __eq__(self, int1):
        return self.my_i != int1

    def __ne__(self, int1):
        return self.my_i == int1
