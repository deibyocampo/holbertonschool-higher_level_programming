#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers % 10 > numbers / 10:
        if numbers < 89:
            print("{:02d}".format(numbers), end=", ")
        else:
            print("{:02d}".format(numbers))
