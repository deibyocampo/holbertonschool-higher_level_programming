#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    n_list = set(my_list)
    for i in n_list:
        add += i
    return add
