#!/usr/bin/python3
""" takes in a letter and sends a POST request to a url. """
import requests
import sys


def search_for_user(letter):
    payload = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        result = response.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__manin__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_for_user(letter)
