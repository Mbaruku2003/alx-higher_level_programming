#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
once = abs(number) % 10
if number < 0:
    sign = "-"
else:
    sign = ""
print(f"Last digit of {number} is {sign}{once}", end=" ")
if number % 10 > 5:
    print(f"and is greater than 5")
elif number % 10 == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
