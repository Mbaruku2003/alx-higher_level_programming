#!/usr/bin/python3
"""  takes in a URL and an email, sends a POST request to the passed URL. """
import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
