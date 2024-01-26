#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Error code: {response.status_code}")
    except Exception as err:
        print(f"Error: {err}")
