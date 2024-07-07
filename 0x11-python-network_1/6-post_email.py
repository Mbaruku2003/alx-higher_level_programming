#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter. """
import sys
import requests


def send_post_rquests(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
