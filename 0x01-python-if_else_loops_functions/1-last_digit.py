#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
last = number % 10
if last != 0 and last < 6:
print("last digit of {0:d} is {1:d}".format(number, last), end=" ")
print("and is less than 6 and not 0")
elif last > 5:
print("last digit of {0:d} is {1:d}".format(number, last), end=" ")
print("and is greater than 5")
else:
print("last digit of {0:d} is 0 and is 0".format(number, last))
