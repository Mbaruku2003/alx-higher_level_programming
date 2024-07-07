#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response. """
import requests
import sys


def fetch_url_content(url):
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url_content(url)
