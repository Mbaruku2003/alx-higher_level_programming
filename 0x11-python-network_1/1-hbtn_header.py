#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header."""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as responses:
    headers = responses.headers
    x_requested_id = headers.get('X-Requested-Id')
print(x_requested_id)
