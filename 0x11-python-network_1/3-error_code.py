#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body. """
import urllib.request
import urllib.error
import sys


def url_content(url):
    try:
        # create a request to the url
        req = urllib.request.Request(url)
        # send a request to read the response
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e))


if __name__ == "__main__":
    url = sys.argv[1]
    url_content(url)
