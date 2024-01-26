#!/usr/bin/python3
"""
Uses GitHub API to display user id using Basic Authentication
with a personal access token.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    auth = HTTPBasicAuth(username, token)
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
