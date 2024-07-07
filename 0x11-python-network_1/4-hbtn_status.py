#!/usr/bin/python3
""" Fteches using package requests. """
import requests


def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status()
