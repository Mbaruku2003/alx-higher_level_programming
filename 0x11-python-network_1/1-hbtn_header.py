#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value."""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.headers
    x_requested_id = headers.get('X-Request-Id')
    print(x_requested_id)
