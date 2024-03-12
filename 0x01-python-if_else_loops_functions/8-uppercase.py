#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        character = letter
        if ord(character) >= 97 and ord(character) <= 122:
            character = chr(ord(letter) - 32)
        print("{}".format(character), end='')
    print()
