#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.test)
