#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        last = number % -10 
        last *= -1
    if number >= 0:
        last = number % 10
    print("{:d}".format(last), end="")
    return last
