#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status. """
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html_body = response.read()
print("Body response:")
print("\t- type:", type(html_body))
print("\t- content:", html_body)
print("\t- utf8 content:", html_body.decode('utf-8'))
