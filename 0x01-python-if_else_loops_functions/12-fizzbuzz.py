#!/usr/bin/python3
def fizzbuzz():
    num = 1
    for num in range(num, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(num), end=" ")