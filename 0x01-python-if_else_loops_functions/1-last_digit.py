#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
if last != 0 and last < 6:
    print("last digit of {0:d} is {1:d} and is less than 6 and not 0".format(number, last))
elif last > 5:
    print("last digit of {0:d} is {1:d} and is greater than 5".format(number, last))
else:
    print("last digit of {0:d} is {1:d} and is 0".format(number, last))
