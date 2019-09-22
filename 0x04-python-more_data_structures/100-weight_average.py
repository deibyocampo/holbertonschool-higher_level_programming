#!/usr/bin/python3
def weight_average(my_list=[]):
    divn = 0
    div = 1
    n_li = []
    for x, y in my_list:
        divn += y * x
        n_li.append(y)
    if len(n_li) > 0:
        div = 0
    for num in n_li:
        div += num
    return divn /div
