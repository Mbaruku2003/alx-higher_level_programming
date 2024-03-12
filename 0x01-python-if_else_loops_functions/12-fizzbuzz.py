#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 != 0:
            numbers = "Fizz"
            print("{}".format(numbers), end=" ")
        elif numbers % 5 == 0 and numbers % 3 != 0:
            numbers = "Buzz"
            print("{}".format(numbers), end=" ")
        elif ((numbers % 5 == 0) and (numbers % 3 == 0)):
            numbers = "FizzBuzz"
            print("{}".format(numbers), end=" ")
        else:
            print("{}".format(numbers), end=" ")
