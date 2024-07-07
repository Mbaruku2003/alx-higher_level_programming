#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the value of the variable. """
import sys
import requests


def fetch_requested_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_requested_id(url)
