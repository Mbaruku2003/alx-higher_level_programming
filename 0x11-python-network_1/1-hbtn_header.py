#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the value. """
import urllib.request
import sys


def fetch_request_id(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)
