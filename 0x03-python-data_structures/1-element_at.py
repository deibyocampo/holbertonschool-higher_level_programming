#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)

    for i in my_list:
        if i == idx:
            return my_list[i]
        if idx < 0 and idx > a:
            return ("None")
